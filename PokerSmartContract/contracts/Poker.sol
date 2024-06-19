// SPDX-License-Identifier: MIT
// @ Author: Bertan Berker
// @ Filename: Poker.sol


pragma solidity ^0.8.2;


contract Poker {

    struct Player {
        uint256 balance;
        string[] hand;
        uint256 currentBet;
    }

    Player player1;
    Player player2;

    constructor(uint256 _balance1, uint256 _balance2) {
        player1.balance = _balance1;
        player2.balance = _balance2;
    }



























}