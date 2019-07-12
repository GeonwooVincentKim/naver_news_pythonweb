from SubMenu.News import *


def OhMyNews():
    print("This is OhMyNews")
    print("Please choose the menu you want")
    menu_ohmynews = input("입력 : ")
    menu_list = []
    while 1:
        if menu_ohmynews == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            oh_my_news_first = oh_my_news()
            menu_list.append(oh_my_news_first)

        elif menu_ohmynews == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            oh_my_news_second = printFirstList()
            menu_list.append(oh_my_news_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def oh_my_news():
    print("오마이 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
