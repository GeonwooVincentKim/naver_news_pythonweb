from SubMenu.broadcaster import *


def MBN():
    print("This is MBN")
    print("Please choose the menu you want")
    menu_mbn = input("입력 : ")
    menu_list = []
    while 1:
        if menu_mbn == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            mbn_first = mbn_news()
            menu_list.append(mbn_first)

        elif menu_mbn == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            mbn_second = printFourthList()
            menu_list.append(mbn_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def mbn_news():
    print("MBN 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
