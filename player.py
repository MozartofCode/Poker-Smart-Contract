# @Filename: player.py
# @Author: Bertan Berker
# This file has the functionality that I need to make moves (player)

class Player:
    def __init__(self):
        self.hand = []
        self.money = 1000
    
    def bet_big_blind(self, big_blind):
        self.money -= big_blind
    
    def bet_small_blind(self, small_blind):
        self.money -= small_blind
    
    def bet(self, bet):
        self.money -= bet
    
    def win(self, table_money):
        self.money += table_money
    
    def call(self, bet):
        self.money -= bet
    
    def raise_bet(self, bet):
        self.money -= bet

    def fold(self):
        return
    
    def check(self):
        return
    

    

         