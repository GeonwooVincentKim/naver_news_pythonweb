from SubMenu.News import *


def Choseon():
    print("This is Choseon")
    print("Please choose the menu you want")
    menu_choseon = input("입력 : ")
    menu_list = []
    while 1:
        if menu_choseon == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            choseon_first = choseon_news()
            menu_list.append(choseon_first)

        elif menu_choseon == '2':
            print("Back to the Future")

            from SubMenu.News import printFirstList
            choseon_second = printFirstList()
            menu_list.append(choseon_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def choseon_news():
    print("조선 일보에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
