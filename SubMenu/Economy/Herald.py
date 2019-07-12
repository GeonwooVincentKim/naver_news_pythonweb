from SubMenu.Economy import *


def Herald():
    print("This is Herald")
    print("Please choose the menu you want")
    menu_herald = input("입력 : ")
    menu_list = []
    while 1:
        if menu_herald == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            herald_first = herald_news()
            menu_list.append(herald_first)

        elif menu_herald == '2':
            print("Back to the Future")
            from SubMenu.Economy import printSecondList
            herald_second = printSecondList()
            menu_list.append(herald_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def herald_news():
    print("헤럴드 경제 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
