from SubMenu.broadcaster import *


def KBSWorld():
    print("This is KBSWorld")
    print("Please choose the menu you want")
    menu_kbsworld = input("입력 : ")
    menu_list = []
    while 1:
        if menu_kbsworld == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            kbsworld_first = kbsworld_news()
            menu_list.append(kbsworld_first)

        elif menu_kbsworld == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            kbsworld_second = printFourthList()
            menu_list.append(kbsworld_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def kbsworld_news():
    print("KBS World TV 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
