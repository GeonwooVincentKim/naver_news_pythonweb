from SubMenu.News import *


def MyDaily():
    print("This is MyDaily")
    print("Please choose the menu you want")
    menu_my_daily = input("입력 : ")
    menu_list = []
    while 1:
        if menu_my_daily == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            my_daily_first = my_daily_news()
            menu_list.append(my_daily_first)

        elif menu_my_daily == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            my_daily_second = printFirstList()
            menu_list.append(my_daily_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def my_daily_news():
    print("마이 데일리 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")