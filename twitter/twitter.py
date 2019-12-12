import GetOldTweets3 as got
from bs4 import BeautifulSoup

import datetime
import time
from random import uniform
from tqdm import tqdm_notebook

def get_tweets(criteria):
    tweet = got.manager.TweetManager.getTweets(criteria)
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
        # 휴식 
        time.sleep(uniform(1,2))
    print("====================================")
    if(len(tweet_list) == 0):
        print("조건에 맞는 tweet이 없습니다.")
    else:
        print(tweet_list)
    print("====================================")
days_range = []

start = datetime.datetime.strptime("2019-11-25", "%Y-%m-%d")
end = datetime.datetime.strptime("2019-11-26", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    days_range.append(date.strftime("%Y-%m-%d"))
print("=== 기본으로 설정된 트윗 수집 기간은 {} 에서 {} 까지 입니다 ===".format(days_range[0], days_range[-1]))
print("=== 총 {}일 간의 데이터 수집 ===".format(len(days_range)))

# 수집 기간 맞추기
start_date = days_range[0]
end_date = (datetime.datetime.strptime(days_range[-1], "%Y-%m-%d") 
            + datetime.timedelta(days=1)).strftime("%Y-%m-%d") # setUntil이 끝을 포함하지 않으므로, day + 1

my_key = input("검색할 키워드를 입력해주세요: ")

while(True):
    temp1 = "현재 검색어는 " + my_key + "입니다. "
    print(temp1)
    print("기간은 기본적으로 최근 1일입니다.")
    print("빠른 검색을 지원하기 위해 최대 50건까지만 표시됩니다.")
    print("1. 닉네임을 통한 검색")
    print("2. 키워드를 통한 검색")
    print("3. 시간을 통한 검색")
    print("4. 종료")
    userNum = int(input("무엇을 하시겠습니까?: "))
    
    if userNum == 1:
        nick = input("검색할 닉네임을 입력해주세요: ")
        print("1. 최근 10개만 보기")
        print("2. 해당 닉네임의 트윗 50건 보기")
        print("3. 현재 검색어를 적용시켜 보기")
        tweetNum = int(input("무엇을 하시겠습니까?: "))
        if(tweetNum == 1):
            tweetCriteria = got.manager.TweetCriteria().setUsername(nick)\
                                           .setSince(start_date)\
                                           .setUntil(end_date)\
                                           .setMaxTweets(10)
            get_tweets(tweetCriteria)
        elif(tweetNum == 2):
            tweetCriteria = got.manager.TweetCriteria().setUsername(nick)\
                                           .setSince(start_date)\
                                           .setUntil(end_date)\
                                           .setMaxTweets(50)
            get_tweets(tweetCriteria)
        elif(tweetNum == 3):
            tweetCriteria = got.manager.TweetCriteria().setUsername(nick)\
                                           .setQuerySearch(my_key)\
                                           .setSince(start_date)\
                                           .setUntil(end_date)\
                                           .setMaxTweets(50)
            get_tweets(tweetCriteria)
        else:
            print("잘못된 보기를 선택하셨습니다.")
    elif userNum == 2:
        my_key = input("검색할 키워드를 입력해주세요: ")
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(my_key)\
                                           .setSince(start_date)\
                                           .setUntil(end_date)\
                                           .setMaxTweets(50)
        get_tweets(tweetCriteria)
    elif userNum == 3:
        user_start = int(input("시작일을 입력해주세요(yyyymmdd형태): "))
        if(user_start < 20170000 or user_start > 20191200):
            print("최근 3년 이내만 검색가능합니다.")
            continue
        user_end = int(input("종료일을 입력해주세요(yyyymmdd형태): "))
        if(user_end > 20191200):
            print("미래로 갈 수는 없습니다.")
            continue
        elif(user_end < user_start):
            print("시작일보다 작을 수 없습니다.")
            continue
        if(user_end - 8 > user_start):
            print("최대 1주일까지 검색이 가능합니다.")
            continue
        else:
            start_year = user_start // 10000
            start_month = user_start // 100 - start_year * 100
            start_day = user_start - start_year * 10000 - start_month * 100
            end_year = user_end // 10000
            end_month = user_end // 100 - end_year * 100
            end_day = user_end - end_year * 10000 - end_month * 100
            d1 = str(start_year) + "-" + str(start_month) + "-" + str(start_day)
            # d2는 보여주기용, d3는 실제 코드에 넣기용(코드에 넣을때는 +1을 해줘야 한다.)
            d2 = str(end_year) + "-" + str(end_month) + "-" + str(end_day)
            d3 = str(end_year) + "-" + str(end_month) + "-" + str(end_day + 1)
            print("1. 현재 검색어를 적용시켜 검색")
            print("2. 다른 검색어를 적용시켜 검색")
            myNum = int(input("무엇을 선택하시겠습니까?: "))
            if(myNum == 1):
                print("1. 닉네임을 적용시켜 검색")
                print("2. 닉네임 상관없이 전부 검색")
                myNum1 = int(input("무엇을 선택하시겠습니까?: "))
                if(myNum1 == 1):
                    nick2 = input("검색할 닉네임을 입력해주세요: ")
                    tweetCriteria = got.manager.TweetCriteria().setUsername(nick)\
                                           .setQuerySearch(my_key)\
                                           .setSince(d1)\
                                           .setUntil(d3)\
                                           .setMaxTweets(50)
                elif(myNum1 == 2):
                    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(my_key)\
                                           .setSince(d1)\
                                           .setUntil(d3)\
                                           .setMaxTweets(50)
                else:
                    print("잘못된 입력입니다.")
                    continue
            elif(myNum == 2):
                my_key = input("검색할 키워드를 입력해주세요: ")
                print("1. 닉네임을 적용시켜 검색")
                print("2. 닉네임 상관없이 전부 검색")
                myNum2 = int(input("무엇을 선택하시겠습니까?: "))
                if(myNum2 == 1):
                    nick2 = input("검색할 닉네임을 입력해주세요: ")
                    tweetCriteria = got.manager.TweetCriteria().setUsername(nick)\
                                           .setQuerySearch(my_key)\
                                           .setSince(d1)\
                                           .setUntil(d3)\
                                           .setMaxTweets(50)
                elif(myNum2 == 2):
                    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(my_key)\
                                           .setSince(d1)\
                                           .setUntil(d3)\
                                           .setMaxTweets(50)
                else:
                    print("잘못된 입력입니다.")
                    continue
            else:
                print("잘못된 입력입니다.")
                continue
            print("=== 현재 설정된 트윗 수집 기간은 {} 에서 {} 까지 입니다 ===".format(d1, d2))
            print("=== 총 {}일 간의 데이터 수집 ===".format(user_end - user_start))
            get_tweets(tweetCriteria)
    elif userNum == 4:
        break
    else:
        print("잘못된 입력입니다.")
        continue
