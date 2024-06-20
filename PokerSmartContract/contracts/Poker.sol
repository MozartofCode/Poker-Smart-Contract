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

    function getPlayer1Balance() public view returns (uint256){
        return player1.balance;
    }

    function getPlayer2Balance() public view returns (uint256) {
        return player2.balance;
    }

    function getPlayer1CurrentBet() public view returns (uint256) {
        return player1.currentBet;
    }

    function getPlayer2CurrentBet() public view returns (uint256) {
        return player2.currentBet;
    }

    function getPlayer1Hand() public view returns (string[] memory) {
        return player1.hand;
    }
    
    function getPlayer2Hand() public view returns (string[] memory) {
        return player2.hand;
    }   































}