from SubMenu.News import *


def Newsis():
    print("This is Newsis")
    print("Please choose the menu you want")
    menu_newsis = input("입력 : ")
    menu_list = []
    while 1:
        if menu_newsis == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            newsis_first = newsis_tapa()
            menu_list.append(newsis_first)

        elif menu_newsis == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            newsis_second = printFirstList()
            menu_list.append(newsis_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def newsis_tapa():
    print("뉴시스 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
