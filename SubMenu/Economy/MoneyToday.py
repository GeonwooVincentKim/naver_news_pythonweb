from SubMenu.Economy import *


def MoneyToday():
    print("This is MoneyToday")
    print("Please choose the menu you want")
    menu_money = input("입력 : ")
    menu_list = []
    while 1:
        if menu_money == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            money_first = money_news()
            menu_list.append(money_first)

        elif menu_money == '2':
            print("Back to the Future")
            from SubMenu.News import printSecondList
            money_second = printSecondList()
            menu_list.append(money_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def money_news():
    print("머니투데이에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
