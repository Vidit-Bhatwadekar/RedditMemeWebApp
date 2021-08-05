import praw
import pandas as pd
import numpy as np

data = []
reddit = praw.Reddit(client_id='tNLoCjYkiHZD5w', client_secret='wJv_fIOZbTvQGxuVkw2JYhz4wgnoig', user_agent='reddit WebScraping')

hot_posts = reddit.subreddit('okbuddyretard').hot(limit=500)
for post in hot_posts:
    data.append(post.title)

OKBR_Titles =  pd.DataFrame(data)

OKBR_Titles.to_csv('OKBR.csv')
