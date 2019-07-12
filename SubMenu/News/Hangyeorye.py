from SubMenu.News import *


def Hangyeorye():
    print("This is Hangyeorye")
    print("Please choose the menu you want")
    menu_hangyeorye = input("입력 : ")
    menu_list = []
    while 1:
        if menu_hangyeorye == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            hangyeorye_first = hangyeorye_news()
            menu_list.append(hangyeorye_first)

        elif menu_hangyeorye == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            hangyeorye_second = printFirstList()
            menu_list.append(hangyeorye_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def hangyeorye_news():
    print("한겨레 일보에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
