from SubMenu.News import *


def Dailyian():
    print("This is Dailyian")
    print("Please choose the menu you want")
    menu_dailyian = input("입력 : ")
    menu_list = []
    while 1:
        if menu_dailyian == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            dailyian_first = dailyian_news()
            menu_list.append(dailyian_first)

        elif menu_dailyian == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            dailyian_second = printFirstList()
            menu_list.append(dailyian_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def dailyian_news():
    print("데일리안 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
