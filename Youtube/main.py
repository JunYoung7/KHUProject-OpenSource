import downloader
from time import sleep
from konlpy.tag import Twitter
from collections import Counter
import pytagcloud
import operator
def get_tags (Comment_List) :

    okja = []
    for temp in Comment_List :
        okja.append(temp['text'])
    twitter = Twitter()
    sentence_tag  =[]
    for sentence in okja:
        morph = twitter.pos(sentence)
        sentence_tag.append(morph)
        print(morph)
        print('-'*30)
    print(sentence_tag)
    print(len(sentence_tag))
    print('\n'*3)

    noun_adj_list = []
    for sentence1 in sentence_tag:
        for word,tag in sentence1:
             if len(word) >=2 and tag  == 'Noun':
                noun_adj_list.append(word)
    counts = Counter(noun_adj_list)
    print(' 가장 많이 등장한 10개의 키워드. \n')
    print(counts.most_common(10))
    tags2 = counts.most_common(10)
    taglist = pytagcloud.make_tags(tags2,maxsize=80)
    pytagcloud.create_tag_image(taglist,'wordcloud.jpg',size =(900,600),fontname ='Nanum Gothic', rectangular = False)

def print_result(Comment_List) :
    for var in Comment_List :
        print(var)
    print('******* 검색 완료 *******')
    print('\n\n\n')

def search_by_author(Comment_List,author_name) :
    result_List = []

    for var in Comment_List :
        if (var['author'] == author_name) :
            result_List.append(var)

    return result_List
def search_by_keyword(Comment_List,keyword) :
        result_List = []
        for var in Comment_List :
            print(var['text'])
            if ( keyword in var['text']) :
                result_List.append(var)

        return result_List
def search_by_time(Comment_List,Time_input) :
    result_List = []
    for var in Comment_List :
        if(var['time'] == Time_input) :
            result_List.append(var)
    return result_List

def make_time_chart (Comment_List) :
    result_List = []
    save_List = []
    day_dict = {}
    month_dict = {}
    year_dict = {}
    hour_dict = {}
    minute_dict = {}
    week_dict = {}
    for var in Comment_List :
        result_List.append(var['time'])
    for i in range(len(result_List)) :
        print(result_List[i] + ' ')
    print('\n\n\n\n')
    temp_List = list(set(result_List))
    for i in range(len(temp_List)) :
        print(temp_List[i] + ' ')
    print('\n\n\n\n')
    for i in range (len(temp_List)) :
        result_dict = {}
        a = result_List.count(temp_List[i])
        result_dict[temp_List[i]] = a
        save_List.append(result_dict)

    for i in range (len(save_List)):
        num = ''
        data = 0
        for j in save_List[i] :
            num = j
        for k in save_List[i].values() :
            data = k
        if num.find('개월') >= 0 :
            month_dict[num] = k
        elif num.find('일') >= 0 :
            day_dict[num] = k
        elif num.find('년') >= 0 :
            year_dict[num] = k
        elif num.find('시간') >= 0 :
            hour_dict[num] = k
        elif num.find('주') >= 0 :
            week_dict[num] = k
        elif num.find('분') >= 0 :
            minute_dict[num] = k
    year_data = sorted(year_dict.items(), key=operator.itemgetter(0))
    month_data = sorted(month_dict.items(), key=operator.itemgetter(0))
    week_data = sorted(week_dict.items(), key=operator.itemgetter(0))
    day_data = sorted(day_dict.items(), key=operator.itemgetter(0))
    hour_data = sorted(hour_dict.items(), key=operator.itemgetter(0))
    minute_data = sorted(minute_dict.items(), key=operator.itemgetter(0))
    print(month_data)
    print(week_data)
    print(day_data)

def call_main ():
    print(' Comment Thread 생성중 \n')

    sleep(1)
    print(' **************************************************************')
    print(' **************************************************************')
    print(' **************************************************************')
    print(' **************** 생성 완료 정보를 입력하세요. ****************  ')
    print(' **************************************************************')
    print(' **************************************************************')
    print(' **************************************************************')
    a = downloader.main()

    return a

if __name__ == "__main__":
    CommentList = call_main()
    make_time_chart(CommentList)
    ##author_results = search_by_author(CommentList,'광고제거기')
    ##text_resutls = search_by_keyword(CommentList,'지현')
    ##get_tags(CommentList)
    ##print_result(author_results)
    ##print_result(text_resutls)
