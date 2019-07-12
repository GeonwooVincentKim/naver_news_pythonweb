from SubMenu.News import *


def Munhua():
    print("This is Munhua")
    print("Please choose the menu you want")
    menu_munhwa = input("입력 : ")
    menu_list = []
    while 1:
        if menu_munhwa == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            munhwa_first = munhwa_news()
            menu_list.append(munhwa_first)

        elif menu_munhwa == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            munhwa_second = printFirstList()
            menu_list.append(munhwa_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def munhwa_news():
    print("문화 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
