from SubMenu.Economy import *


def Maeil():
    print("This is Maeil Economy")
    print("Please choose the menu you want")
    menu_maeil = input("입력 : ")
    menu_list = []
    while 1:
        if menu_maeil == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            maeil_first = maeil_news()
            menu_list.append(maeil_first)

        elif menu_maeil == '2':
            print("Back to the Future")
            from SubMenu.News import printSecondList
            maeil_second = printSecondList()
            menu_list.append(maeil_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def maeil_news():
    print("매일 경제에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
