from SubMenu.broadcaster import *


def YTN():
    print("This is YTN")
    print("Please choose the menu you want")
    menu_ytn = input("입력 : ")
    menu_list = []
    while 1:
        if menu_ytn == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            ytn_first = ytn_news()
            menu_list.append(ytn_first)

        elif menu_ytn == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            ytn_second = printFourthList()
            menu_list.append(ytn_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def ytn_news():
    print("YTN 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
