import downloader
from time import sleep

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
    author_results = search_by_author(a,'광고제거기')
    text_resutls = search_by_keyword(a,'지현')
    print_result(author_results)
    print_result(text_resutls)
    return a

CommentList = call_main()
