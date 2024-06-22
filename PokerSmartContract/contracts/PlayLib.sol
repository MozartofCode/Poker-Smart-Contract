// SPDX-License-Identifier: MIT
// @ Author: Bertan Berker
// @ Filename: PlayLib.sol
// This is a library that the Poker smart contract imports for gameplay

pragma solidity ^0.8.2;

library PlayLib{

	// GETTING WHAT IT IS (FLUSH, FULL HOUSE...)
	// CHOOSING WINNER
	// True if player1 is winner, False if player2 is winner
	function chooseWinner(Player _player1, Player _player2) public pure returns (bool) {
		return true;
	} 


	//
	//
	// :param _hand: The two cards in your hand
	// :param _table: The five cards at the middle of the table
	function getHandRanking(string[] memory _hand, string[] memory _table) public pure returns (string memory) {
		return "";


	}

}