from selenium import webdriver
from selenium.common import exceptions
from bs4 import BeautifulSoup
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
        
    print(naverNewsList[:3])
    
    return naverNewsList
    #driver.quit()