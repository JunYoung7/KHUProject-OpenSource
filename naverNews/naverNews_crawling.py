from selenium import webdriver
from selenium.common import exceptions
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from konlpy.tag import Twitter
from collections import Counter
import time


def getData(url):
    ## chrome option걸기 (headless하게 웹 크롤링 수행하기 위해<웹페이지 안보이게 하기>)
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument("disable-gpu")
    #_url = "https://entertain.naver.com/ranking/comment/list?oid=144&aid=0000642175" # 크롤링할 URL
    _url = url # 크롤링할 URL
    webDriver = "C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe"  # 내 웹드라이버 위치
    driver = webdriver.Chrome(webDriver,chrome_options=options)
    #driver = webdriver.Chrome(webDriver)
    driver.get(_url)
    pageCnt = 0
    driver.implicitly_wait(3) # 페이지가 다 로드 될때까지 기다리게함
    try:
        while True: # 댓글 페이지 끝날때까지 돌림
            #driver의 find_element_by_css_selector함수로 '네이버 뉴스'의 댓글 '더보기' 버튼을 찾아서 계속 클릭해준다(끝까지)
            driver.find_element_by_css_selector(".u_cbox_btn_more").click() 
            pageCnt = pageCnt+1
        
    except exceptions.ElementNotVisibleException as e: # 페이지가 끝남
        pass
        
    except Exception as e: # 다른 예외 발생시 확인
        print(e)
    
    pageSource = driver.page_source # 페이지 소스를 따와서
    result = BeautifulSoup(pageSource, "lxml") # 빠르게 뽑아오기 위해 lxml 사용

    # nickname, text, time을 raw하게 뽑아온다
    comments_raw = result.find_all("span", {"class" : "u_cbox_contents"})
    nicknames_raw = result.find_all("span", {"class" : "u_cbox_nick"})
    times_raw = result.find_all("span", {"class" : "u_cbox_date"})

    # nickname, text, time 값 만을 뽑아내어 리스트로 정리한다
    comments = [comment.text for comment in comments_raw]
    nicknames = [nickname.text for nickname in nicknames_raw]
    times = [time.text for time in times_raw]
    
    naverNewsList = []
    
    for i in range(len(comments)):
        info_dic = {'userID' : nicknames[i], 'comment' : comments[i], 'time' : times[i]}
        naverNewsList.append(info_dic)
        
    return naverNewsList
    #driver.quit()
    
from time import sleep

def print_cList(c_List) :
    for item in c_List :
        print(item)

def search_by_author(c_List,user_ID) :
        result_List = []
        for item in c_List :
           #print(item['userID'])
            if ( user_ID in item['userID']) :
                result_List.append(item)
        return result_List

def search_by_keyword(c_List,keyword) :
        result_List = []
        for item in c_List :
            #print(item['comment'])
            if ( keyword in item['comment']) :
                result_List.append(item)
        return result_List

def refine_time(c_List): # 시간에서 몇일 전, 몇 분 전, 방금 전 등의 형태를 YYYY.MM.DD로 바꿔준다
    now = datetime.now()
    
    for item in c_List:
        if (item['time'].find('전') != -1): # ~~전이 있으면
            if (item['time'].find('일 전') != -1): # ~일 전이라면
                _day = -(int)(item['time'][0]) # 몇 일전인지에 대한 정수형 변수
                tempTime = now + timedelta(days=_day)
                item['time'] = str(tempTime)
                item['time'] = item['time'][0:10]
                continue
            elif (item['time'].find('시간 전') != -1):
                _index = item['time'].index('시')
                _time = -(int)(item['time'][0:_index]) # 몇 시간 전인지에 대한 정수형 변수
                tempTime = now + timedelta(hours = _time)
                item['time'] = str(tempTime)
                item['time'] = item['time'][0:10]
                continue
            elif (item['time'].find('분 전') != -1):
                _index = item['time'].index('분')
                _minute = -(int)(item['time'][0:_index]) # 몇 분 전인지에 대한 정수형 변수
                tempTime = now + timedelta(minutes = _minute)
                item['time'] = str(tempTime)
                item['time'] = item['time'][0:10]
                continue
            elif (item['time'].find('방금 전') != -1):
                tempTime = now
                item['time'] = str(tempTime)
                item['time'] = item['time'][0:10]
                continue
            else:
                item['time'] = item['time'][0:10]
                continue
        
        
                
            

def search_by_time(c_List,startTime, endTime) : 
    result_List = []
    
    startYear = int(startTime[0:4])
    
    if (int(startTime[5]) == 0): # 한자리의 월일 때
        startMonth = int(startTime[6])
    else:
        startMonth = int(startTime[5:7])
        
    if (int(startTime[8]) == 0): # 한자리의 일일 때
        startDay = int(startTime[9])
    else:
        startDay = int(startTime[8:10])
    
    
    
    endYear = int(endTime[0:4])
    
    if (int(endTime[5]) == 0): # 한자리의 월일 때
        endMonth = int(endTime[6])
    else:
        endMonth = int(endTime[5:7])
        
    if (int(endTime[8]) == 0): # 한자리의 일일 때
        endDay = int(endTime[9])
    else:
        endDay = int(endTime[8:10])
    
    for item in c_List:
        itemYear = int(item['time'][0:4])
        
        if (int(item['time'][5]) == 0): # 한자리의 월일 때
            itemMonth = int(item['time'][6])
        else:
            itemMonth = int(item['time'][5:7])
        
        if (int(item['time'][8]) == 0): # 한자리의 일일 때
            itemDay = int(item['time'][9])
        else:
            itemDay = int(item['time'][8:10])
        
        if (itemYear >= startYear and itemYear <= endYear):
            if (itemMonth >= startMonth and itemMonth <= endMonth):
                if(itemDay >= startDay and itemDay <= endDay):
                    result_List.append(item)
    
    return result_List

def printMostShowed(c_List,limit):
    temp = ""
    result = ""
    for item in c_List:
        temp = str(item['comment']) + " "
        result = result + temp
    
    sp = Twitter()
    
    nouns = sp.nouns(result)
    
    _cnt = Counter(nouns)
    
    tempList = []
    repCnt = 0
    
    for i,j in _cnt.most_common(limit):
        print(str(repCnt+1)+'. '+str(i)+" : "+str(j))
        repCnt += 1
        
def printResult(c_List):
    for i in range(0,len(c_List)):
        print(c_List[i])

def main ():
    ## 시작화면
    
    _star = '*'
    print(_star.center(30,'*'))
    print('\n')
    headString = '< Naver News Crawling >'
    print(headString.center(30,'*'))
    print('\n')
    print(_star.center(30,'*'))
    
    
    # 검색하고자 하는 url을 입력받는다
    _url = input('검색하고자 하는 url을 입력해주세요: ')
    print('comment_list를 가져오는 중.....')
    cList = getData(_url)
    refine_time(cList)
    #printMostShowed(cList,10)
    print('\n')
    print('comment_list를 다 가져왔습니다!')
    
    while(True):
        print('***********************************')
        print('1.닉네임 기반 검색')
        print('2.키워드 기반 검색')
        print('3.작성시간 기반 검색')
        print('4.자주 나타난 단어 출력')
        menu = input('메뉴를 입력해주세요: ')
        
        if(menu == str(1)):
            print('***********************************')
            inputID = input('검색할 닉네임 앞 4자리를 입력해주세요(전 단계로 가시려면 -1을 입력해주세요): ')
            if(inputID == str(-1)):
                continue
            _result = search_by_author(cList,inputID)
            printResult(_result)
            print(_result)
        elif(menu == str(2)):
            print('***********************************')
            inputKW = input('검색할 키워드를 입력해주세요(전 단계로 가시려면 -1을 입력해주세요): ')
            if(inputKW == str(-1)):
                continue
            _result = search_by_keyword(cList,inputKW)
            printResult(_result)
        elif(menu == str(3)):
            print('***********************************')
            print('전 단계로 돌아가시려면 -1을 입력해주세요')
            startTime = input('검색할 시간대의 시작일을 입력해주세요(YYYY-MM-DD): ')
            endTime = input('검색할 시간대의 마지막 일을 입력해주세요(YYYY-MM-DD): ')
            
            if(startTime == str(-1) or endTime == str(-1)):
                continue
                
            _result = search_by_time(cList,startTime,endTime)
            printResult(_result)
        elif(menu == str(4)):
            print('***********************************')
            inputLimit = input('상위 몇 개 까지 보고 싶은지 입력하세요(1~20): ')
            while(True):
                if (int(inputLimit) <= 0 or int(inputLimit) > 20):
                    inputLimit = input('상위 몇 개 까지 보고 싶은지 입력하세요(1~20): ')
                else:
                    break
                
            printMostShowed(cList,int(inputLimit))
        else:
            print('잘못된 입력입니다')
            continue
            

    
main()
