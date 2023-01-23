"""
author: Etienne Wallet

This module contains the cli for the execution subpackage
"""
from argparse import _SubParsersAction, Namespace
import os
from pathlib import Path
from mxops.config.config import Config
from mxops.data import path
from mxops.data.data import ScenarioData

from mxops.enums import NetworkEnum
from mxops.execution.scene import execute_directory, execute_scene
from mxops import errors


def add_subparser(subparsers_action: _SubParsersAction):
    """
    Add the data subparser to a parser

    :param subparsers_action: subparsers interface for the parent parser
    :type subparsers_action: _SubParsersAction[ArgumentParser]
    """
    scenario_parser = subparsers_action.add_parser('execute')
    scenario_parser.add_argument('-s',
                                 '--scenario',
                                 type=str,
                                 required=True,
                                 help=('Name of the scenario in which the '
                                       'scene(s) will be executed'))
    scenario_parser.add_argument('-n',
                                 '--network',
                                 type=NetworkEnum,
                                 required=True,
                                 help=('Name of the network in which the '
                                       'scene(s) will be executed'))
    scenario_parser.add_argument('elements',
                                 nargs='+',
                                 type=str,
                                 help='Path to scene file and/or scene directory')


def execute_cli(args: Namespace):
    """
    Execute the data cli by following the given parsed arguments

    :param args: parsed arguments
    :type args: Namespace
    """
    if args.command != 'execute':
        raise ValueError(f'Command execute was expected, found {args.command}')

    path.initialize_data_folder()
    Config.set_network(args.network)
    try:
        ScenarioData.load_scenario(args.scenario)
    except errors.UnknownScenario:
        ScenarioData.create_scenario(args.scenario)
        ScenarioData.get().save()

    for element in args.elements:
        element_path = Path('./' + element)
        if os.path.isfile(element_path):
            execute_scene(element_path)
        elif os.path.isdir(element_path):
            execute_directory(element_path)
        else:
            raise ValueError(f'{element_path} is not a file nor a directory')
