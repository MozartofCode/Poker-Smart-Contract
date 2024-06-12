# @Filename: bot.py
# @Author: Bertan Berker
# The poker playing bot is going to learn how to play and make decisions based on
# Q-learning (Reinforcement Learning)
# This is the functionality of the bot that is going to play against me (player)

class Bot:
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
    




