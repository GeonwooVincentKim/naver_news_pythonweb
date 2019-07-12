from SubMenu.News import *


def Blotter():
    print("This is Blotter")
    print("Please choose the menu you want")
    menu_blotter = input("입력 : ")
    menu_list = []
    while 1:
        if menu_blotter == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            blotter_first = blotter_news()
            menu_list.append(blotter_first)

        elif menu_blotter == '2':
            print("Back to the Future")

            from SubMenu.News import printFirstList
            blotter_second = printFirstList()
            menu_list.append(blotter_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def blotter_news():
    print("블로터 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
