// SPDX-License-Identifier: MIT
// @ Author: Bertan Berker
// @ Filename: Poker.sol


pragma solidity ^0.8.2;

import './PlayLib.sol';
import './CardLib.sol';

contract Poker {

    struct Player {
        uint256 balance;
        string[] hand;
        uint256 currentBet;
    }

    Player player1;
    Player player2;
	CardLib.Card[] deck;

    // This is the constructor for the contract
    constructor(uint256 _balance1, uint256 _balance2) {
        player1.balance = _balance1;
        player2.balance = _balance2;
    }


    // These are the setters for the contract
    function setPlayer1Balance(uint256 _balance) public {
        player1.balance = _balance;
    }

    function setPlayer2Balance(uint256 _balance) public {
        player2.balance = _balance;
    }

    function setPlayer1CurrentBet(uint256 _bet) public {
        player1.currentBet = _bet;
    }

    function setPlayer2CurrentBet(uint256 _bet) public {
        player2.currentBet = _bet;
    }

    function setPlayer1Hand(string[] memory _hand) public {
        player1.hand = _hand;
    } 

    function setPlayer2Hand(string[] memory _hand) public {
        player2.hand = _hand;
    } 


    // These are the getters for the contract
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