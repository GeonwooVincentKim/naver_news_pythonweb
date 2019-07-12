from SubMenu.News import *


def Gukmin():
    print("This is Gukmin")
    print("Please choose the menu you want")
    menu_gukmin = input("입력 : ")
    menu_list = []
    while 1:
        if menu_gukmin == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            gukmin_first = gukmin_news()
            menu_list.append(gukmin_first)

        elif menu_gukmin == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            gukmin_second = printFirstList()
            menu_list.append(gukmin_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def gukmin_news():
    print("국민 일보에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
