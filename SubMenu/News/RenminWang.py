from SubMenu.News import *


def RenminWang():
    print("This is RenminWang")
    print("Please choose the menu you want")
    menu_Renmin = input("입력 : ")
    menu_list = []
    while 1:
        if menu_Renmin == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            renmin_first = renmin_wang()
            menu_list.append(renmin_first)

        elif menu_Renmin == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            renmin_second = printFirstList()
            menu_list.append(renmin_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def renmin_wang():
    print("인민망에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")

