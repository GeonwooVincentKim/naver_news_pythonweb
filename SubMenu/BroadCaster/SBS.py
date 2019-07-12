from SubMenu.broadcaster import *


def SBS():
    print("This is SBS")
    print("Please choose the menu you want")
    menu_sbs = input("입력 : ")
    menu_list = []
    while 1:
        if menu_sbs == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            sbs_first = sbs_news()
            menu_list.append(sbs_first)

        elif menu_sbs == '2':
            print("Back to the Future")
            from SubMenu.broadcaster import printFourthList
            sbs_second = printFourthList()
            menu_list.append(sbs_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def sbs_news():
    print("SBS 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
