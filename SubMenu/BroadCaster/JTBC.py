from SubMenu.broadcaster import *


def JTBC():
    print("This is JTBC")
    print("Please choose the menu you want")
    menu_jtbc = input("입력 : ")
    menu_list = []
    while 1:
        if menu_jtbc == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            jtbc_first = jtbc_news()
            menu_list.append(jtbc_first)

        elif menu_jtbc == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            jtbc_second = printFourthList()
            menu_list.append(jtbc_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def jtbc_news():
    print("JTBC 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
