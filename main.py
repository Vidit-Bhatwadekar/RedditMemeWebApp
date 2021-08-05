import praw
import pandas as pd
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import streamlit as st



OKBR_df = pd.read_csv('OKBR.csv')
OKBR_arr = OKBR_df.iloc[:, 1].to_numpy()
OKBR_ls = OKBR_arr.tolist()

st.sidebar.title("NLP Bot")
st.title("okbuddyretard Bot")

bot = ChatBot('Yahoo')

ind = 1
if st.sidebar.button('Initialize chatbot'):
    trainer = ListTrainer(bot)
    trainer.train(OKBR_ls)
    st.title("Your bot is ready to talk to you")
    ind = ind + 1

def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text

user_input = get_text()

if True:
    st.text_area("Bot:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)

# while True:
#     request = st.text_input('You: ')
#     response = bot.get_response(request)
#     st.write('Bot: ' + str(response))
