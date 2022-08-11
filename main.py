import pandas as pd
import json
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
import streamlit as st

st.set_page_config(
    page_title="Okbuddy get ready for some MEMSS",
    page_icon= "😜",
    layout="wide"
)



st.markdown('''<style> 
ul {
    padding-left: 1.5rem;
  }

h1 {
    text-align:center;
}

h5 {
    text-align:center;
}

img {
    margin-left: 17.2rem;
}

#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}
header {
    visibility: hidden;
}')
</style>
''', unsafe_allow_html=True)



OKBR_df = pd.read_csv('OKBR.csv')
OKBR_url = pd.read_csv('OKBR_url.csv')
OKBR_arr = OKBR_df.iloc[:, 1].to_numpy()
OKBR_ls = OKBR_arr.tolist()

OKBR_url = OKBR_url.rename(columns={'Unnamed: 0':'Number', '0': 'URL'})
OKBR_df = OKBR_df.rename(columns={'Unnamed: 0':'Number', '0': 'Quote'})

st.title("r/okbr MEme funtime")

st.markdown("""
### okbudy time for todays mem

Refresh page for new meme and Quotation. 

The author of this page does not endorse any of the sentiments expressed in the quotes or memes - they are randomly selected

""")


if True:
    a = """
    <img src={} width="500">

    """.format('"' + OKBR_url.sample()['URL'].iloc[0] + '"')

    st.markdown("Quotation:" + OKBR_df.sample()['Quote'].iloc[0])
    st.markdown(a, unsafe_allow_html=True)

with st.container():
    for i in range(3):
        st.write("##")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            The author of this page does not endorse any of the sentiments expressed in the above quotations and memes
            """
        )
    with col2:
        st.markdown("<p style='text-align: right;'>Made in 2022 with Python, Pandas, Streamlit. Deployed using Heroku</p>", unsafe_allow_html=True)
    st.write("---")