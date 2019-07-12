from SubMenu.broadcaster import *


def OSEN():
    print("This is OSEN")
    print("Please choose the menu you want")
    menu_osen = input("입력 : ")
    menu_list = []
    while 1:
        if menu_osen == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            osen_first = osen_news()
            menu_list.append(osen_first)

        elif menu_osen == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            osen_second = printFourthList()
            menu_list.append(osen_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def osen_news():
    print("OSEN 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
