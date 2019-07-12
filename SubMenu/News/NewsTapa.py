from SubMenu.News import *


def NewsTapa():
    print("This is NewsTapa")
    print("Please choose the menu you want")
    menu_news_tapa = input("입력 : ")
    menu_list = []
    while 1:
        if menu_news_tapa == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            news_tapa_first = news_tapa()
            menu_list.append(news_tapa_first)

        elif menu_news_tapa == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            news_tapa_second = printFirstList()
            menu_list.append(news_tapa_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def news_tapa():
    print("뉴스 타파에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")