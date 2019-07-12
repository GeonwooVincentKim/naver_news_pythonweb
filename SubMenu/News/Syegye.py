from SubMenu.News import *


def Syegye():
    print("This is Syegye")
    print("Please choose the menu you want")
    menu_syegye = input("입력 : ")
    menu_list = []
    while 1:
        if menu_syegye == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            syegye_first = syegye_news()
            menu_list.append(syegye_first)

        elif menu_syegye == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            syegye_second = printFirstList()
            menu_list.append(syegye_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def syegye_news():
    print("세계 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")