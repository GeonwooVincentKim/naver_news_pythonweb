from SubMenu.SportNews import *


def SpotalKorea():
    print("This is SpotalKorea")
    print("Please choose the menu you want")
    menu_spotal = input("입력 : ")
    menu_list = []
    while 1:
        if menu_spotal == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            spotal_first = spotal_news()
            menu_list.append(spotal_first)

        elif menu_spotal == '2':
            print("Back to the Future")
            from SubMenu.News import printThirdList
            spotal_second = printThirdList()
            menu_list.append(spotal_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def spotal_news():
    print("스포탈 Sport 에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
