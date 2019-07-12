from SubMenu.SportNews import *


def SportSeoul():
    print("This is SportSeoul")
    print("Please choose the menu you want")
    menu_seoul = input("입력 : ")
    menu_list = []
    while 1:
        if menu_seoul == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            seoul_first = seoul_news()
            menu_list.append(seoul_first)

        elif menu_seoul == '2':
            print("Back to the Future")
            from SubMenu.News import printThirdList
            seoul_second = printThirdList()
            menu_list.append(seoul_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def seoul_news():
    print("서울 Sport 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
