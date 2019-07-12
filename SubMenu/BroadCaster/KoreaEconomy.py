from SubMenu.broadcaster import *


def korea_economy():
    print("This is KoreaEconomy")
    print("Please choose the menu you want")
    menu_korea = input("입력 : ")
    menu_list = []
    while 1:
        if menu_korea == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            korea_first = korea_news()
            menu_list.append(korea_first)

        elif menu_korea == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            korea_second = printFourthList()
            menu_list.append(korea_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def korea_news():
    print("한국 경제 TV 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")

