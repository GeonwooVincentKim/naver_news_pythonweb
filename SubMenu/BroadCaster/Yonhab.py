from SubMenu.broadcaster import *


def YonHab():
    print("This is Yonhab")
    print("Please choose the menu you want")
    menu_yonhab= input("입력 : ")
    menu_list = []
    while 1:
        if menu_yonhab == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            yonhab_first = yonhab_news()
            menu_list.append(yonhab_first)

        elif menu_yonhab == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            yonhab_second = printFourthList()
            menu_list.append(yonhab_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def yonhab_news():
    print("연합뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
