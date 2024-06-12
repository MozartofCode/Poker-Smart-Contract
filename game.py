# @Filename: game.py
# @Author: Bertan Berker
# This file has game related functionalities used for game play

import random
from bot import Bot
from player import Player

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

        ranking = ["RF", "SF", "FK", "FH", "F", "S", "TK", "TP", "P", "HC"]
        
        bot_index = 0
        player_index = 0

        for i in range(len(ranking)):
            if bot[0] == ranking[i]:
                bot_index = i
            
            if player[0] == ranking[i]:
                player_index = i
        
        if bot_index < player_index:
            return "bot"

        elif player_index < bot_index:
            return "player"
        
        else:
            # Both have the same thing, looking at the best 5 cards
            return self.find_best(player + self.table, bot + self.table, bot[bot_index])


    def find_best(self, player_cards, bot_cards, value):

        if value in ["SF", "S"]:
            
            player_high = 0
            bot_high = 0

            ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
            values = {rank: index for index, rank in enumerate(ranks)}
            sorted_cards = sorted([values[card.split(" of ")[0]] for card in player_cards])
            for i in range(len(sorted_cards) - 4):
                if sorted_cards[i:i+5] == list(range(sorted_cards[i], sorted_cards[i]+5)):
                    
                    sc = [self.get_value(sorted_cards[i])]
                    sc.append(self.get_value(sorted_cards[i+1]))
                    sc.append(self.get_value(sorted_cards[i+2]))
                    sc.append(self.get_value(sorted_cards[i+3]))
                    sc.append(self.get_value(sorted_cards[i+4]))

                    player_high = max(sc)

            ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
            values = {rank: index for index, rank in enumerate(ranks)}
            sorted_cards = sorted([values[card.split(" of ")[0]] for card in bot_cards])
            for i in range(len(sorted_cards) - 4):
                if sorted_cards[i:i+5] == list(range(sorted_cards[i], sorted_cards[i]+5)):

                    sc = [self.get_value(sorted_cards[i])]
                    sc.append(self.get_value(sorted_cards[i+1]))
                    sc.append(self.get_value(sorted_cards[i+2]))
                    sc.append(self.get_value(sorted_cards[i+3]))
                    sc.append(self.get_value(sorted_cards[i+4]))

                    bot_high = max(sc)

            if player_high > bot_high:
                return "player"
            
            elif player_high < bot_high:
                return "bot"
    
            else:
                return "draw"
                        
        
        elif value in ["FK", "TK", "FH"]:
            
            for c in range(len(player_cards)):
                player_cards[c] = player_cards[c].split(" of ")[0]
            
            for c in range(len(bot_cards)):
                bot_cards[c] = bot_cards[c].split(" of ")[0]
            
            # Looking at a Three of a kind is enough

            player_pairs = dict()
            bot_pairs = dict()

            for i in range(len(player_cards)):
                for j in range(i, len(player_cards)):
                    if player_cards[i] == player_cards[j] and player_pairs[player_cards[i]] == 1:
                        player_pairs[player_cards[i]] = 2
                    elif player_cards[i] == player_cards[j] and player_pairs[player_cards[i]] == 2:
                        player_pairs[player_cards[i]] = 3
                    else:
                        player_pairs[player_cards[i]] = 1
            
            for i in range(len(bot_cards)):
                for j in range(i, len(bot_cards)):
                    if bot_cards[i] == bot_cards[j] and bot_pairs[bot_cards[i]] == 1:
                        bot_pairs[bot_cards[i]] = 2
                    elif bot_cards[i] == bot_cards[j] and bot_pairs[bot_cards[i]] == 2:
                        bot_pairs[bot_cards[i]] = 3
                    else:
                        bot_pairs[bot_cards[i]] = 1

            pp = 0
            bp = 0

            for key in player_pairs.keys():
                if player_pairs[key] == 3:
                    pp.append(self.get_value(key))
            
            for key in bot_pairs.keys():
                if bot_pairs[key] == 3:
                    bp.append(self.get_value(key))
            
            # Looking at the two separate pairs
            if pp > bp:
                return "player"

            elif pp < bp:
                return "bot"

            else:
                return "draw"


        elif value in ["F"]:
            
            player_suits = dict()
            player_suits["Hearts"] = 0
            player_suits["Spades"] = 0
            player_suits["Diamonds"] = 0
            player_suits["Clubs"] = 0

            bot_suits = dict()
            bot_suits["Hearts"] = 0
            bot_suits["Spades"] = 0
            bot_suits["Diamonds"] = 0
            bot_suits["Clubs"] = 0

            p = []
            b = []            
            p_suit = ""
            b_suit = ""
            
            for i in range(len(player_cards)):
                suit = player_cards[i].split(" of ")[1]
                player_suits[suit] += 1
            
            for j in range(len(bot_cards)):
                suit = bot_cards[i].split(" of ")[1]
                bot_suits[suit] += 1

            for key in player_suits.keys():
                if player_suits[key] == 5:
                    p_suit = key
            
            for key in bot_suits.keys():
                if bot_suits[key] == 5:
                    b_suit = key
                
            for card in player_cards:
                if card.split(" of ")[1] == p_suit:
                    p.append(int(self.get_value(card.split(" of ")[0])))
            
            for card in bot_cards:
                if card.split(" of ")[1] == b_suit:
                    b.append(int(self.get_value(card.split(" of ")[0])))
            
            if max(p) > max(b):
                return "player"
            elif max(p) < max(b):
                return "bot"
            else:
                return "draw"
        
        elif value in ["TP"]:
            
            for c in range(len(player_cards)):
                player_cards[c] = player_cards[c].split(" of ")[0]
            
            for c in range(len(bot_cards)):
                bot_cards[c] = bot_cards[c].split(" of ")[0]

            player_pairs = dict()
            bot_pairs = dict()

            
            for i in range(len(player_cards)):
                for j in range(i, len(player_cards)):
                    if player_cards[i] == player_cards[j]:
                        player_pairs[player_cards[i]] = 2
                    else:
                        player_pairs[player_cards[i]] = 1
            
            for i in range(len(bot_cards)):
                for j in range(i, len(bot_cards)):
                    if bot_cards[i] == bot_cards[j]:
                        bot_pairs[bot_cards[i]] = 2
                    else:
                        bot_pairs[bot_cards[i]] = 1

            pp = []
            bp = []

            for key in player_pairs.keys():
                if player_pairs[key] == 2:
                    pp.append(self.get_value(key))
            
            for key in bot_pairs.keys():
                if bot_pairs[key] == 2:
                    bp.append(self.get_value(key))
            
            # Looking at the two separate pairs
            if max(pp) > max(bp):
                return "player"

            elif max(pp) < max(bp):
                return "bot"

            else:
                return "draw"

        elif value in ["P"]:
            
            for c in range(len(player_cards)):
                player_cards[c] = player_cards[c].split(" of ")[0]
            
            for c in range(len(bot_cards)):
                bot_cards[c] = bot_cards[c].split(" of ")[0]

            player_pair = ""
            bot_pair = ""

            for i in range(len(player_cards)):
                for j in range(i, len(player_cards)):
                    if player_cards[i] == player_cards[j]:
                        player_pair = player_cards[i]
            
            for i in range(len(bot_cards)):
                for j in range(i, len(bot_cards)):
                    if bot_cards[i] == bot_cards[j]:
                        bot_pair = bot_cards[i]
            
            if self.get_value(player_pair) > self.get_value(bot_pair):
                return "player"
            
            elif self.get_value(player_pair) < self.get_value(bot_pair):
                return "player"
            
            else:
                return "draw"
            
        
        elif value in ["HC"]:
            if int(self.get_high_card(player_cards)) > int(self.get_high_card(bot_cards)):
                return "player"
            elif int(self.get_high_card(player_cards)) < int(self.get_high_card(bot_cards)):
                return "bot"
            else:
                return "draw"



    def get_value(self, card):
        
        rank = card.split(" of ")[0]
            
        if rank == "Ace":
            return "14"
        
        elif rank == "King":
            return "13"
        
        elif rank == "Queen":
            return "12"
        
        elif rank == "Jack":
            return "11"
        else:
            return int(rank)





    def evaluate_hand_player(self):
        ph = self.player.hand
        table = self.table
        cards = table + ph

        if self.is_royal_flush(cards):
            return "RF"
        
        elif self.is_straight_flush(cards):
            return "SF"
        
        elif self.is_four_of_kind(cards):
            return "FK"
        
        elif self.is_full_house(cards):
            return "FH"
        
        elif self.is_flush(cards):
            return "F"
        
        elif self.is_straight(cards):
            return "S"
        
        elif self.is_three_of_kind(cards):
            return "TK"
        
        elif self.is_two_pair(cards):
            return "TP"
        
        elif self.is_pair(cards):
            return "P"
        
        else:
            return "HC"


    def evaluate_hand_bot(self):
        bh = self.bot.hand
        table = self.table
        cards = table + bh

        if self.is_royal_flush(cards):
            return "RF"
        
        elif self.is_straight_flush(cards):
            return "SF"
        
        elif self.is_four_of_kind(cards):
            return "FK"
        
        elif self.is_full_house(cards):
            return "FH"
        
        elif self.is_flush(cards):
            return "F"
        
        elif self.is_straight(cards):
            return "S"
        
        elif self.is_three_of_kind(cards):
            return "TK"
        
        elif self.is_two_pair(cards):
            return "TP"
        
        elif self.is_pair(cards):
            return "P"
        
        else:
            return "HC"



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
            return "14"
        
        elif "King" in ranks:
            return "13"
        
        elif "Queen" in ranks:
            return "12"
        
        elif "Jack" in ranks:
            return "11"

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