// SPDX-License-Identifier: MIT
// @ Author: Bertan Berker
// @ Filename: CardLib.sol
// This is a library that the Poker smart contract imports for card gameplay

pragma solidity ^0.8.2;

library CardLib{

	struct Card {
		string rank;
		string suit;
	}
	
	function createCard(string memory _rank, string memory _suit) public pure returns (Card memory) {
    	Card memory card = Card({
            rank: _rank,
            suit: _suit
        });
        return card;
    }

	function createDeck() public pure returns (Card[] memory) {

		



	}





}