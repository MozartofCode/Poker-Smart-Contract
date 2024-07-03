# @Author: Bertan Berker
# @File: GeminiBot.py
# This file has the functions to fine-tune Gemini and make API calls calling for action

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

API_KEY = ""
genai.configure(api_key=API_KEY)


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


class Game_State:
    def __init__(self, table_cards, your_cards, player_recent_move, player_total_bet):
        self.table_cards = table_cards
        self.your_cards = your_cards
        self.player_recent_move = player_recent_move      
        self.player_total_bet = player_total_bet

        

def query_game_state():
    return


model = genai.GenerativeModel('gemini-1.0-pro')

response = model.generate_content("What is the meaning of life?")

print(response.text)





