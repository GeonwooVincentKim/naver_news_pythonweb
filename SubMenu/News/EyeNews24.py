from SubMenu.News import *


def EyeNews24():
    print("This is EyeNews24")
    print("Please choose the menu you want")
    menu_eyenews24 = input("입력 : ")
    menu_list = []
    while 1:
        if menu_eyenews24 == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            eyenews24_first = eyenews24_news()
            menu_list.append(eyenews24_first)

        elif menu_eyenews24 == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            eyenews24_second = printFirstList()
            menu_list.append(eyenews24_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def eyenews24_news():
    print("아이뉴스24에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
