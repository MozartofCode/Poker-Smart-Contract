# @Author: Bertan Berker
# @Filename: CLI.py
# This is the CLI that interacts with the blockchain and the Gemini API
#
#

import json
from web3 import Web3
import ast


class Game_State:
    def __init__(self, table_cards, your_cards, player_recent_move, pot, game_situation, bot_money, player_money):
        self.table_cards = table_cards
        self.your_cards = your_cards
        self.player_recent_move = player_recent_move      
        self.pot = pot
        self.game_situation = game_situation
        self.bot_money = bot_money
        self.player_money = player_money




# Player is always big blind in this version
def main():
    print("Welcome to world series of poker championships...")
    print("Let's play some poker!")


    # Connecting to Ganache
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    print("Connection to Ganache successful?: " + str(web3.is_connected()))

    # Replace with the address of the deployed contract
    contract_address = ''

    # Replace with the path to your contract's JSON file
    with open('PokerSmartContract/build/contracts/Poker.json') as f:
        contract_json = json.load(f)
        contract_abi = contract_json['abi']

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    web3 = web3
    contract = contract
    web3.eth.default_account = web3.eth.accounts[0]


    # Set big and small bling
    big_blind = contract.functions.getBigBlind().call()
    small_blind = contract.functions.getSmallBlind().call()


    while contract.functions.getPlayer1Balance().call() > 0 and contract.functions.getPlayer2Balance().call() > 0:

        


    # Deal cards for bot and player


    # Bot moves pre-flop
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    










if __name__ == "__main__":
    main()