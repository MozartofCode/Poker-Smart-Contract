
import random

class Deck:

    # Initializing a deck of cards
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank + ' of ' + suit)


    # Shuffling the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)
    

    # Dealing one card from the deck
    # :return: the card or None if not possible
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
        

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
    
    def raise_bot(self, bet):
        self.money -= bet
         


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
    
    def raise_player(self, bet):
        self.money -= bet


class Game:

    def __init__(self):
        
        self.player = Player()
        self.bot = Bot()
        self.deck = Deck()
        self.pot = 0
        self.big_blind = 50
        self.small_blind = 25
        self.table = []
        self.players_bet = 0
        self.bots_bet = 0

    def deal_cards(self):
        for _ in range(2):
            self.bot.hand.append(self.deck.deal_card())
            self.player.hand.append(self.deck.deal_card())
            
    def clear_hands(self):
        self.pot = 0
        self.bot.hand = []
        self.player.hand = []
        self.table = []

    def deal_flop(self):
        # Burn one 
        self.deck.deal_card()
        # Deal
        for _ in range(3):
            self.table.append(self.deck.deal_card())
    

    def deal_turn_river(self):
        # Burn one 
        self.deck.deal_card()
        # Deal
        self.table.append(self.deck.deal_card())

    def evaluate_hands(self):
        
        ph = self.player.hand
        bh = self.bot.hand

         