from game import Game

def print_player_hand(game):
    print()
    print("Table: " + str(game.table))
    print("Player's Hand: " + str(game.player.hand))
    print("Bot's Hand: []")
    print()


def show_hands(game, winner):
    if winner == "player":
        print("Player wins the hand")
    elif winner == "bot":
        print("Bot wins the hand")
    else:
        print("It's a draw")
    
    print()
    print(str(game.table))
    print("Player's Hand: " + str(game.player.hand))
    print("Bot's Hand: " + str(game.bot.hand))
    print()

    
def print_table_money(game):
    print("Player: $" + str(game.player.money))
    print("Bot: $" + str(game.bot.money))
    print()
    print("Player's Bet: $" + str(game.players_bet))
    print("Bot's Bet: $" + str(game.bots_bet))
    print("Pot: $" + str(game.pot))
    print()


def main():

    print("Welcome to Casino Royale...")
    print("Heads up game player vs. bot")
    print()

    game = Game()
    bot = game.bot
    player = game.player

    bb = game.big_blind
    sb = game.small_blind

    # Is player big blind?
    player_bb = True

    while bot.money > 0 and player.money > 0:

        # This is for keeping track of the current hand
        game_over = False

        game.deal_cards()

        if player_bb:
            bot.bet_small_blind(sb)
            player.bet_big_blind(bb)
            game.players_bet = bb
            game.bots_bet = sb

            print_table_money(game)

            # Bot's turn
            print("Bot's Move: ")
            # TODO
            # TODO
            # TODO

            # Player's turn
            print_player_hand(game)
            move = input("Do you Check/Raise or Fold? (CH/R-$/F): ")

            if move == "C":
                player.check()

            elif move == "F":
                player.fold()
                game.clear_hands()
                game_over = True

            elif move[0] == "R":
                #TODO Raise call logic
                return
            
            if not game_over:
                
                # Flop
                print("Flop")
                game.deal_flop()
                print_player_hand(game)

                # Bot's turn
                print("Bot's Move: ")
                # TODO
                # TODO
                # TODO

                # Player's turn
                move = input("Do you Check/Raise or Fold? (CH/R-$/F): ")

            


            if not game_over:

                # Turn
                print("Turn")
                game.deal_turn_river()
                print_player_hand(game)

                # Bot's turn
                print("Bot's Move: ")
                # TODO
                # TODO
                # TODO

                # Player's turn
                move = input("Do you Check/Raise or Fold? (CH/R-$/F): ")
                
            
            if not game_over:
                
                # River
                print("River")
                game.deal_turn_river()
                print_player_hand(game)

                # Bot's turn
                print("Bot's Move: ")
                # TODO
                # TODO
                # TODO

                # Player's turn
                move = input("Do you Check/Raise or Fold? (CH/R-$/F): ")
                
            
            if not game_over:
                winner = game.choose_winner()
                show_hands(game, winner)
                print_table_money(game)



        else:
            return
    



if __name__ == "__main__":
    main()