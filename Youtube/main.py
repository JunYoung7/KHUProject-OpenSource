import downloader
from time import sleep

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

CommentList = call_main()
