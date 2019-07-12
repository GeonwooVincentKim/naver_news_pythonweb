from SubMenu.News import *


def NewDaily():
    print("This is MyDaily")
    print("Please choose the menu you want")
    menu_new_daily = input("입력 : ")
    menu_list = []
    while 1:
        if menu_new_daily == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            new_daily_first = new_daily_news()
            menu_list.append(new_daily_first)

        elif menu_new_daily == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            new_daily_second = printFirstList()
            menu_list.append(new_daily_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def new_daily_news():
    print("뉴데일리 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
