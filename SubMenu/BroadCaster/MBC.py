from SubMenu.broadcaster import *


def MBC():
    print("This is MBC")
    print("Please choose the menu you want")
    menu_mbc = input("입력 : ")
    menu_list = []
    while 1:
        if menu_mbc == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            mbc_first = mbc_news()
            menu_list.append(mbc_first)

        elif menu_mbc == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            mbc_second = printFourthList()
            menu_list.append(mbc_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def mbc_news():
    print("MBC 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")

