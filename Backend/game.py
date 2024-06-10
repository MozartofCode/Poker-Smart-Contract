
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


    def choose_winner(self):
        player = self.evaluate_hand_player()
        bot = self.evaluate_hand_bot()

        


    def evaluate_hand_player(self):
        ph = self.player.hand
        bh = self.bot.hand
        table = self.table


    def evaluate_hand_bot(self):
        ph = self.player.hand
        bh = self.bot.hand
        table = self.table






    def is_royal_flush(self, cards):
        
        if not self.is_straight_flush(cards):
            return False
        
        ranks = []

        for card in cards:
            rank = card.split(" of ")[0]
            ranks.append(rank)
        
        if "Ace" not in ranks:
            return False
        
        if "King" not in ranks:
            return False
        
        if "Queen" not in ranks:
            return False
        
        if "Jack" not in ranks:
            return False
        
        if "10" not in ranks:
            return False
        
        return True

    
    def is_straight_flush(self, cards):
        return self.is_flush(cards) and self.is_straight(cards)
    
    def is_four_of_kind(self, cards):
        ranks = dict()

        for card in cards:
            rank = card.split(" of ")[0]
            
            if rank in ranks:
                ranks[rank] += 1
            else:
                ranks[rank] = 1
            
        for rank in ranks.keys():
            if ranks[rank] == 4:
                return True
            
        return False

    
    def is_full_house(self, cards):
        ranks = dict()

        for card in cards:
            rank = card.split(" of ")[0]
            
            if rank in ranks:
                ranks[rank] += 1
            else:
                ranks[rank] = 1
        
        two_pair = False
        three_kind = False

        for rank in ranks.keys():
            if ranks[rank] == 3:
                three_kind = True
            elif ranks[rank] == 2:
                two_pair = True
            
        return three_kind and two_pair
    

    
    def is_flush(self, cards):
        suits = dict()

        for card in cards:
            suit = card.split(" of ")[1]

            if suit in suits:
                suits[suit] += 1
            else:
                suits[suit] = 1

        for suit in suits.keys():
            if suits[suit] == 5:
                return True
        
        return False


    def is_straight(self, cards):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        values = {rank: index for index, rank in enumerate(ranks)}
        sorted_cards = sorted([values[card.split(" of ")[0]] for card in cards])
        for i in range(len(sorted_cards) - 4):
            if sorted_cards[i:i+5] == list(range(sorted_cards[i], sorted_cards[i]+5)):
                return True
        return False
        

    
    def is_three_of_kind(self, cards):
        ranks = dict()

        for card in cards:
            rank = card.split(" of ")[0]
            
            if rank in ranks:
                ranks[rank] += 1
            else:
                ranks[rank] = 1
            
        for rank in ranks.keys():
            if ranks[rank] == 3:
                return True
            
        return False
    

    def is_two_pair(self, cards):
        ranks = dict()

        for card in cards:
            rank = card.split(" of ")[0]
            
            if rank in ranks:
                ranks[rank] += 1
            else:
                ranks[rank] = 1
        
        pair_num = 0

        for rank in ranks.keys():
            if ranks[rank] == 2:
                pair_num += 1
            
        return pair_num == 2
        

    def is_pair(self, cards):
        ranks = dict()

        for card in cards:
            rank = card.split(" of ")[0]
            
            if rank in ranks:
                ranks[rank] += 1
            else:
                ranks[rank] = 1
        
        pair_num = 0

        for rank in ranks.keys():
            if ranks[rank] == 2:
                pair_num += 1
            
        return pair_num == 1
        

    def get_high_card(self, cards):
        ranks = []

        for card in cards:
            rank = card.split(" of ")[0]
            ranks.append(rank)
        
        if "Ace" in ranks:
            return "Ace"
        
        elif "King" in ranks:
            return "King"
        
        elif "Queen" in ranks:
            return "Queen"
        
        elif "Jack" in ranks:
            return "Jack"

        elif "10" in ranks:
            return "10"

        elif "9" in ranks:
            return "9"

        elif "8" in ranks:
            return "8"

        elif "7" in ranks:
            return "7"

        elif "6" in ranks:
            return "6"

        elif "5" in ranks:
            return "5"

        elif "4" in ranks:
            return "4"

        elif "3" in ranks:
            return "3"

        elif "2" in ranks:
            return "2"         