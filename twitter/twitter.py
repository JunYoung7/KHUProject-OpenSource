#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import GetOldTweets3 as got
from bs4 import BeautifulSoup

import datetime

days_range = []

start = datetime.datetime.strptime("2019-11-14", "%Y-%m-%d")
end = datetime.datetime.strptime("2019-11-15", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    days_range.append(date.strftime("%Y-%m-%d"))
print("=== 설정된 트윗 수집 기간은 {} 에서 {} 까지 입니다 ===".format(days_range[0], days_range[-1]))
print("=== 총 {}일 간의 데이터 수집 ===".format(len(days_range)))

import time

# 수집 기간 맞추기
start_date = days_range[0]
end_date = (datetime.datetime.strptime(days_range[-1], "%Y-%m-%d") 
            + datetime.timedelta(days=1)).strftime("%Y-%m-%d") # setUntil이 끝을 포함하지 않으므로, day + 1

# 트윗 수집 기준 정의
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('한글')                                           .setSince(start_date)                                           .setUntil(end_date)                                           .setMaxTweets(-1)

# 수집 with GetOldTweet3
print("Collecting data start.. from {} to {}".format(days_range[0], days_range[-1]))
start_time = time.time()

tweet = got.manager.TweetManager.getTweets(tweetCriteria)

print("Collecting data end.. {0:0.2f} Minutes".format((time.time() - start_time)/60))
print("=== Total num of tweets is {} ===".format(len(tweet)))
from random import uniform
from tqdm import tqdm_notebook

# initialize
tweet_list = []

for index in tqdm_notebook(tweet):
    
    # 메타데이터 목록 
    username = index.username
    link = index.permalink 
    content = index.text
    tweet_date = index.date.strftime("%Y-%m-%d")
    retweets = index.retweets
    favorites = index.favorites
     
    # 결과 합치기
    info_list = {'username' : username, 'text': content, 'time': tweet_date, 'link': link}
    tweet_list.append(info_list)
    print(tweet_list)
    # 휴식 
    time.sleep(uniform(1,2))


# In[ ]:




