// Code generated by the multiversx-sc build system. DO NOT EDIT.

////////////////////////////////////////////////////
////////////////// AUTO-GENERATED //////////////////
////////////////////////////////////////////////////

// Init:                                 1
// Endpoints:                           30
// Async Callback (empty):               1
// Total number of exported functions:  32

#![no_std]

// Configuration that works with rustc < 1.73.0.
// TODO: Recommended rustc version: 1.73.0 or newer.
#![feature(lang_items)]

multiversx_sc_wasm_adapter::allocator!();
multiversx_sc_wasm_adapter::panic_handler!();

multiversx_sc_wasm_adapter::endpoints! {
    data_store
    (
        init => init
        my_usize => my_usize
        my_u8 => my_u8
        my_u16 => my_u16
        my_u32 => my_u32
        my_u64 => my_u64
        my_isize => my_isize
        my_i8 => my_i8
        my_i16 => my_i16
        my_i32 => my_i32
        my_i64 => my_i64
        my_token_identifier => my_token_identifier
        my_managed_address => my_managed_address
        my_biguint => my_biguint
        my_bigint => my_bigint
        my_option_biguint => my_option_biguint
        my_vec_biguint => my_vec_biguint
        my_enum_with_everything => my_enum_with_everything
        view_optional_1 => view_optional_1
        get_init_params => get_init_params
        upgrade => upgrade
        get_upgrade_params => get_upgrade_params
        test_1 => test_1
        test_2 => test_2
        get_test_2_params => get_test_2_params
        test_3 => test_3
        get_test_3_params => get_test_3_params
        test_4 => test_4
        get_test_4_params => get_test_4_params
        view_test_1 => view_test_1
        view_test_2 => view_test_2
    )
}

multiversx_sc_wasm_adapter::async_callback_empty! {}
