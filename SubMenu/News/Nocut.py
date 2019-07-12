from SubMenu.News import *


def Nocut():
    print("This is Nocut")
    print("Please choose the menu you want")
    menu_no_cut = input("입력 : ")
    menu_list = []
    while 1:
        if menu_no_cut == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            nocut_first = nocut_news()
            menu_list.append(nocut_first)

        elif menu_no_cut == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            nocut_second = printFirstList()
            menu_list.append(nocut_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def nocut_news():
    print("노컷 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")