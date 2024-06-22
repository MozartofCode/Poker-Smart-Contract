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

	function createDeck() public pure returns (Card[52] memory) {

		Card[52] memory deck;
		ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
		uint count = 0;

		for (uint i = 0; i < ranks.length; i++) {	
			for (uint j = 0; j < suits.length; j++) {
				Card card = Card({
            		rank: "Ace",
            		suit: "Spades"
        		});

				deck[count] = card;
				count += 1;
			}
		}
    	
		shuffleDeck(deck);    
        return deck;
	
	}

	// Function to shuffle the deck using Fisher-Yates algorithm
	function shuffleDeck(Card[] memory deck) internal pure {
        uint n = deck.length;
        for (uint i = n - 1; i > 0; i--) {
            uint j = uint(keccak256(abi.encodePacked(block.timestamp, i))) % (i + 1);
            Card memory temp = deck[i];
            deck[i] = deck[j];
            deck[j] = temp;
        }
    }





}