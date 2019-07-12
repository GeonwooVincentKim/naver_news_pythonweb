from SubMenu.broadcaster import *


def KBS():
    print("This is KBS")
    print("Please choose the menu you want")
    menu_kbs = input("입력 : ")
    menu_list = []
    while 1:
        if menu_kbs == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            kbs_first = kbs_news()
            menu_list.append(kbs_first)

        elif menu_kbs == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            kbs_second = printFourthList()
            menu_list.append(kbs_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def kbs_news():
    print("KBS 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
