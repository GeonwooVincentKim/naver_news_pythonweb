from SubMenu.News import *


def JoongAng():
    print("This is JoongAng")
    print("Please choose the menu you want")
    menu_JoongAng = input("입력 : ")
    menu_list = []
    while 1:
        if menu_JoongAng == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            JoongAng_first = joongang_news()
            menu_list.append(JoongAng_first)

        elif menu_JoongAng == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            JoongAng_second = printFirstList()
            menu_list.append(JoongAng_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def joongang_news():
    print("중앙일보 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
