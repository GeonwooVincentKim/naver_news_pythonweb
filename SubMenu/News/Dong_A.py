from SubMenu.News import *


def Dong_A():
    print("This is Dong_A")
    print("Please choose the menu you want")
    menu_dong_a = input("입력 : ")
    menu_list = []
    while 1:
        if menu_dong_a == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            dong_a_first = dong_a_news()
            menu_list.append(dong_a_first)

        elif menu_dong_a == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            dong_a_second = printFirstList()
            menu_list.append(dong_a_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def dong_a_news():
    print("동아 일보에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
