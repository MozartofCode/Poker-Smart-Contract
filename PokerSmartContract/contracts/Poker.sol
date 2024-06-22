// SPDX-License-Identifier: MIT
// @ Author: Bertan Berker
// @ Filename: Poker.sol


pragma solidity ^0.8.2;

import './PlayLib.sol';
import './CardLib.sol';

contract Poker {

    struct Player {
        uint256 balance;
        CardLib.Card[2] hand;
        uint256 currentBet;
    }

    Player player1;
    Player player2;
	CardLib.Card[52] deck;
    CardLib.Card[5] table;

    // This is the constructor for the contract
    constructor(uint256 _balance1, uint256 _balance2) {
        CardLib.Card[52] memory tempDeck = CardLib.createDeck();
        for (uint i = 0; i < tempDeck.length; i++) {
            deck[i] = tempDeck[i];
        }
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

    function setPlayer1Hand(CardLib.Card[2] memory _hand) public {
        for (uint i = 0; i < 2; i++) {
            player1.hand[i] = _hand[i];
        }
    } 

    function setPlayer2Hand(CardLib.Card[2] memory _hand) public {
        for (uint i = 0; i < 2; i++) {
            player2.hand[i] = _hand[i];
        }
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

    function getPlayer1Hand() public view returns (CardLib.Card[2] memory) {
        return player1.hand;
    }
    
    function getPlayer2Hand() public view returns (CardLib.Card[2] memory) {
        return player2.hand;
    }   

    // Miscellaneous Functions
    function getNewDeck() public {
        CardLib.Card[52] memory tempDeck = CardLib.createDeck();
        for (uint i = 0; i < tempDeck.length; i++) {
            deck[i] = tempDeck[i];
        }
        
        // Initialize hands and table
        for (uint i = 0; i < player1.hand.length; i++) {
            player1.hand[i] = CardLib.Card("", "");
        }
        
        for (uint i = 0; i < player2.hand.length; i++) {
            player2.hand[i] = CardLib.Card("", "");
        }
        
        for (uint i = 0; i < table.length; i++) {
            table[i] = CardLib.Card("", "");
        }

        player1.currentBet = 0;
        player2.currentBet = 0;

    }

    function endOfHand(Player memory _player1, Player memory _player2) public {
        // End of River
        if (PlayLib.chooseWinner(_player1, _player2, table)) {
            // Player1 wins
            player1.balance += player1.currentBet;
        }

        else{
            // Player2 wins
            player2.balance -= player2.currentBet;
        }
    }

}