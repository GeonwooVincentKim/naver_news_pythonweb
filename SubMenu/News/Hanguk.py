from SubMenu.News import *


def Hanguk():
    print("This is Hanguk")
    print("Please choose the menu you want")
    menu_hanguk = input("입력 : ")
    menu_list = []
    while 1:
        if menu_hanguk == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            hanguk_first = hanguk_news()
            menu_list.append(hanguk_first)

        elif menu_hanguk == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            hanguk_second = printFirstList()
            menu_list.append(hanguk_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def hanguk_news():
    print("한국 일보에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
