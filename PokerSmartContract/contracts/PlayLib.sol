// SPDX-License-Identifier: MIT
// @ Author: Bertan Berker
// @ Filename: PlayLib.sol
// This is a library that the Poker smart contract imports for gameplay

pragma solidity ^0.8.2;

import './CardLib.sol';

library PlayLib{

	// This function chooses the winner of the hand
	// :param _player1: player1
	// :param _player2: player2
	// :param _table: cards on table
	// :return: True if player1 is winner, False if player2 is winner
	function chooseWinner(Player _player1, Player _player2, CardLib.Card[] memory _table) public pure returns (bool) {
		
		player1Rank = getHandRanking(_player1.hand, _table);
		player2Rank = getHandRanking(_player2.hand, _table);
		
		if player1Rank < player2Rank {
			return true;
		}

		else if player2Rank < player1Rank {
			return false;
		}

		else {
			return tieBreaker(_player1.hand, _player2.hand, _table);
		}
	} 


	// This function gets the hand ranking of a player like Flush, Royal Flush, Full House etc
	// :param _hand: The two cards in your hand
	// :param _table: The five cards at the middle of the table
	// :return: The index of the ranking
	// []
	function getHandRanking(CardLib.Card[] memory _hand, CardLib.Card[] memory _table) public pure returns (uint256) {
		return 0;
	}


	// This function gets the winner if both players have the same ranking (both straight etc. but highest of five wins)
	// :param _player1Hand: Player1's hand
	// :param _player2Hand: Player2's hand
	// :param _table: The cards on the table
	// :return: True if player1 is winner, false if player2 is winner
	// If there is an actual tie then returns true but changes the bets to 0 for no change
	function tieBreaker(CardLib.Card[] memory _player1Hand, CardLib.Card[] memory _player2Hand, CardLib.Card[] memory _table) public pure returns (bool) {
		return true;
	}

}