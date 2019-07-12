from SubMenu.News import *


def GyeongHyang():
    print("This is GyeongHyang")
    print("Please choose the menu you want")
    menu_gyeonghyang = input("입력 : ")
    menu_list = []
    while 1:
        if menu_gyeonghyang == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            gyeonghyang_first = gyeonghyang_news()
            menu_list.append(gyeonghyang_first)

        elif menu_gyeonghyang == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            gyeonghyang_second = printFirstList()
            menu_list.append(gyeonghyang_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def gyeonghyang_news():
    print("경향 일보에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
