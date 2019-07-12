from SubMenu.broadcaster import *


def SportChosun():
    print("This is SportChosun")
    print("Please choose the menu you want")
    menu_chosun = input("입력 : ")
    menu_list = []
    while 1:
        if menu_chosun == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            chosun_first = chosun_news()
            menu_list.append(chosun_first)

        elif menu_chosun == '2':
            print("Back to the Future")
            from SubMenu.News import printThirdList
            chosun_second = printThirdList()
            menu_list.append(chosun_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def chosun_news():
    print("조선 Sport 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
