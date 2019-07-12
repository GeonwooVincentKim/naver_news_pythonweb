from SubMenu.News import *


def Jeonja():
    print("This is Jeonja")
    print("Please choose the menu you want")
    menu_jeonja = input("입력 : ")
    menu_list = []
    while 1:
        if menu_jeonja == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            Jeonja_first = jeonja_news()
            menu_list.append(Jeonja_first)

        elif menu_jeonja == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            Jeonja_second = printFirstList()
            menu_list.append(Jeonja_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def jeonja_news():
    print("전자 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
