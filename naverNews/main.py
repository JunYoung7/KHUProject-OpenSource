{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "******************************\n",
      "\n",
      "\n",
      "***< Naver News Crawling >****\n",
      "\n",
      "\n",
      "******************************\n",
      "검색하고자 하는 url을 입력해주세요: https://entertain.naver.com/ranking/comment/list?oid=144&aid=0000642175\n",
      "comment_list를 가져오는 중.....\n",
      "Message: element not interactable\n",
      "  (Session info: chrome=78.0.3904.97)\n",
      "\n",
      "[{'userID': 'ydja****', 'comment': '옹벤져스 너무웃겨', 'time': '6일 전'}, {'userID': 'kims****', 'comment': '사랑해요 옹벤져스! 준기엄마 다리 찢을 때 웃겨죽는 줄 진짜 츤데레언니들', 'time': '6일 전'}, {'userID': 'hoho****', 'comment': '옹벤져스가 다른 마을 살인마 잡는 이야기로 시즌 2. 갑시다', 'time': '6일 전'}]\n",
      "comment_list를 다 가져왔습니다!\n"
     ]
    }
   ],
   "source": [
    "import naverNews_crawling \n",
    "from time import sleep\n",
    "\n",
    "def print_cList(c_List) :\n",
    "    for item in c_List :\n",
    "        print(item)\n",
    "\n",
    "def search_by_author(c_List,user_ID) :\n",
    "        result_List = []\n",
    "        for item in c_List :\n",
    "            print(item['userID'])\n",
    "            if ( user_ID in item['userID']) :\n",
    "                result_List.append(item)\n",
    "        return result_List\n",
    "\n",
    "def search_by_keyword(c_List,keyword) :\n",
    "        result_List = []\n",
    "        for item in c_List :\n",
    "            print(item['comment'])\n",
    "            if ( keyword in item['comment']) :\n",
    "                result_List.append(item)\n",
    "        return result_List\n",
    "    \n",
    "'''\n",
    "def search_by_time(c_List,_time) :\n",
    "        result_List = []\n",
    "        for item in c_List :\n",
    "            print(item['time'])\n",
    "            if ( keyword in item['comment']) :\n",
    "                result_List.append(item)\n",
    "        return result_List    \n",
    "        \n",
    "'''    \n",
    "\n",
    "def main ():\n",
    "    ## 시작화면\n",
    "    \n",
    "    _star = '*'\n",
    "    print(_star.center(30,'*'))\n",
    "    print('\\n')\n",
    "    headString = '< Naver News Crawling >'\n",
    "    print(headString.center(30,'*'))\n",
    "    print('\\n')\n",
    "    print(_star.center(30,'*'))\n",
    "    \n",
    "    \n",
    "    # 검색하고자 하는 url을 입력받는다\n",
    "    _url = input('검색하고자 하는 url을 입력해주세요: ')\n",
    "    print('comment_list를 가져오는 중.....')\n",
    "    cList = naverNews_crawling.getData(_url)\n",
    "    print('comment_list를 다 가져왔습니다!')\n",
    "\n",
    "main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
