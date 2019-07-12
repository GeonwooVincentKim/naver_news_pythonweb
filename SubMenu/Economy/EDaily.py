from SubMenu.Economy import *


def EDaily():
    print("This is EDaily")
    print("Please choose the menu you want")
    menu_edaily = input("입력 : ")
    menu_list = []
    while 1:
        if menu_edaily == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            edaily_first = edaily_news()
            menu_list.append(edaily_first)

        elif menu_edaily == '2':
            print("Back to the Future")
            from SubMenu.Economy import printSecondList
            edaily_second = printSecondList()
            menu_list.append(edaily_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def edaily_news():
    print("이데일리 경제 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
