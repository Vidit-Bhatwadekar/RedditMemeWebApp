import pandas as pd
import json
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
import streamlit as st
from bottle import route, template, run
import praw



OKBR_df = pd.read_csv('OKBR.csv')
OKBR_arr = OKBR_df.iloc[:, 1].to_numpy()
OKBR_ls = OKBR_arr.tolist()

OKBR_df = OKBR_df.rename(columns={'Unnamed: 0':'Number', '0': 'Quote'})

st.title("r/okbr MEme funtime")

st.markdown("""
### okbudy time for todays mem


""")






# bot = ChatBot('Yahoo')

# ind = 1
# if st.sidebar.button('Initialize chatbot'):
#     # trainer = ListTrainer(bot)
#     # trainer.train(OKBR_ls)
#     st.title("Your bot is ready to talk to you")
#     ind = ind + 1

# def get_text():
#     input_text = st.text_input("You: ","So, what's in your mind")
#     return input_text
#
# user_input = get_text()

if True:
    st.markdown(OKBR_df.sample()['Quote'].iloc[0])
