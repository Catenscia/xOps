// Code generated by the multiversx-sc build system. DO NOT EDIT.

////////////////////////////////////////////////////
////////////////// AUTO-GENERATED //////////////////
////////////////////////////////////////////////////

// Init:                                 1
// Endpoints:                           10
// Async Callback:                       1
// Total number of exported functions:  12

#![no_std]

// Configuration that works with rustc < 1.73.0.
// TODO: Recommended rustc version: 1.73.0 or newer.
#![feature(lang_items)]

multiversx_sc_wasm_adapter::allocator!();
multiversx_sc_wasm_adapter::panic_handler!();

multiversx_sc_wasm_adapter::endpoints! {
    esdt_minter
    (
        init => init
        getEsdtIdentifier => esdt_identifier
        getAirdropAmount => airdrop_amount
        getInterestPercentage => interest_percentage
        upgrade => upgrade
        claimAirdrop => claim_airdrop
        claimInterests => claim_interests
        addInterestAddress => add_interest_address
        removeInterestAddress => remove_interest_address
        issueToken => issue_token
        addAirdropAmount => add_airdrop_amount
    )
}

multiversx_sc_wasm_adapter::async_callback! { esdt_minter }
