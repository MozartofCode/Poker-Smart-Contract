# @Author: Bertan Berker
# @File: GeminiBot.py
# This file has the functions to fine-tune Gemini and make API calls calling for action

import google.generativeai as genai

API_KEY = ""
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro')

from CLI import Game_State
        
# FOR SITUATION WHERE BOTS GOING SECOND
#
#
def query_game_state(game_state):

    query = "Pretend that You are an average texas holdem player and you are playing against me. Here is the game situation: "

    query += "It's " + str(game_state.game_situation) + ". "
    query += "Card's on the table are: " + str(game_state.table_cards) + ". "
    query += "Your cards are: " + str(game_state.your_cards) + ". "  
    query += "Your total money: $" + str(game_state.bot_money) + ". "
    query += "Player's total money: $" + str(game_state.player_money) + ". "
    query += "Player's recent move was: " + str(game_state.player_recent_move) + ". "
    query += "Pot is: $" + str(game_state.player_recent_move) + ". "

    response_style = "I want you to tell me what you do next in this format: 'FOLD/CALL/RAISE'. For example if you are calling only respond with 'CALL'.\
        The only exception is when you are raising I want you to respond in the format: 'RAISE-$50' to raise $50 for example. DO NOT RESPOND IN ANY OTHER FORM!"
    
    query += response_style

    response = model.generate_content(query)    
    return response.text


def get_bot_move(game_state):
    text = query_game_state(game_state)
    print(text)









