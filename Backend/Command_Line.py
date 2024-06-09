from game import Game



def show_hands(game, winner):
    if winner == "player":
        print("Player wins the hand")
    else:
        print("Bot wins the hand")
    
    print()
    print(str(game.table))
    print("Player: " + str(game.player.hand))
    print("Bot: " + str(game.bot.hand))
    print()

    
def print_table_money(game):
    print("Player: $" + str(game.player.money))
    print("Bot: $" + str(game.bot.money))
    print()
    print("Player's Bet: $" + str(game.players_bet))
    print("Bot's bet: $" + str(game.bots_bet))
    print("Pot: $" + str(game.pot))
    print()


def main():

    print("Welcome to Casino Royale...")
    print("Heads up game player vs. bot")
    print()

    game = Game()
    bot = game.bot()
    player = game.player()

    bb = game.big_blind
    sb = game.small_blind

    # Is player big blind?
    player_bb = True

    while bot.money > 0 and player.money > 0:

        if player_bb:
            bot.bet_small_blind(sb)
            player.bet_big_blind(bb)

            print()
        
        
        
        
        
        else:
            return
    

