from multiversx_sdk_core import Address
from multiversx_sdk_core.transaction_builders import DefaultTransactionBuildersConfiguration

from mxops.execution import token_managment


def test_fungible_issue_payload():
    # Given
    builder_config = DefaultTransactionBuildersConfiguration(
        chain_id='D'
    )
    builder = token_managment.FungibleTokenIssueBuilder(
        builder_config,
        Address.from_bech32('erd17jcn20jh2k868vg0mm7yh0trdd5mxpy4jzasaf2uraffpae0yrjsvu6txw'),
        'MyToken',
        'MTK',
        1000000,
        3,
        can_pause=True,
        can_upgrade=True
    )

    # When
    payload = builder.build_payload()

    # Then
    assert payload.data == (b'issue'
                            b'@4d79546f6b656e'
                            b'@4d544b'
                            b'@0f4240'
                            b'@03'
                            b'@63616e5061757365@74727565'
                            b'@63616e55706772616465@74727565'
                            )


def test_non_fungible_issue_payload():
    # Given
    builder_config = DefaultTransactionBuildersConfiguration(
        chain_id='D'
    )
    builder = token_managment.NonFungibleTokenIssueBuilder(
        builder_config,
        Address.from_bech32('erd17jcn20jh2k868vg0mm7yh0trdd5mxpy4jzasaf2uraffpae0yrjsvu6txw'),
        'MyToken',
        'MTK',
        can_upgrade=True,
        can_transfer_nft_create_role=True
    )

    # When
    payload = builder.build_payload()

    # Then
    assert payload.data == (b'issueNonFungible'
                            b'@4d79546f6b656e'
                            b'@4d544b'
                            b'@63616e55706772616465@74727565'
                            b'@63616e5472616e736665724e4654437265617465526f6c65@74727565'
                            )


def test_semi_fungible_issue_payload():
    # Given
    builder_config = DefaultTransactionBuildersConfiguration(
        chain_id='D'
    )
    builder = token_managment.SemiFungibleTokenIssueBuilder(
        builder_config,
        Address.from_bech32('erd17jcn20jh2k868vg0mm7yh0trdd5mxpy4jzasaf2uraffpae0yrjsvu6txw'),
        'MyToken',
        'MTK',
        can_burn=True,
        can_upgrade=True,
        can_transfer_nft_create_role=True
    )

    # When
    payload = builder.build_payload()

    # Then
    assert payload.data == (b'issueSemiFungible'
                            b'@4d79546f6b656e'
                            b'@4d544b'
                            b'@63616e4275726e@74727565'
                            b'@63616e55706772616465@74727565'
                            b'@63616e5472616e736665724e4654437265617465526f6c65@74727565'
                            )


def test_meta_fungible_issue_payload():
    # Given
    builder_config = DefaultTransactionBuildersConfiguration(
        chain_id='D'
    )
    builder = token_managment.MetaFungibleTokenIssueBuilder(
        builder_config,
        Address.from_bech32('erd17jcn20jh2k868vg0mm7yh0trdd5mxpy4jzasaf2uraffpae0yrjsvu6txw'),
        'MyToken',
        'MTK',
        3,
        can_burn=True,
        can_upgrade=True,
        can_transfer_nft_create_role=True
    )

    # When
    payload = builder.build_payload()

    # Then
    assert payload.data == (b'registerMetaESDT'
                            b'@4d79546f6b656e'
                            b'@4d544b'
                            b'@03'
                            b'@63616e4275726e@74727565'
                            b'@63616e55706772616465@74727565'
                            b'@63616e5472616e736665724e4654437265617465526f6c65@74727565'
                            )
