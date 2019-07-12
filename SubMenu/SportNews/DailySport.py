from SubMenu.SportNews import *


def DailySport():
    print("This is DailySport")
    print("Please choose the menu you want")
    menu_daily = input("입력 : ")
    menu_list = []
    while 1:
        if menu_daily == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            daily_first = daily_news()
            menu_list.append(daily_first)

        elif menu_daily == '2':
            print("Back to the Future")
            from SubMenu.News import printThirdList
            daily_second = printThirdList()
            menu_list.append(daily_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def daily_news():
    print("데일리 Sport 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
