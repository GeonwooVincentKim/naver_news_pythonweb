from SubMenu.News import *


def Sisain():
    print("This is Sisain")
    print("Please choose the menu you want")
    menu_sisain = input("입력 : ")
    menu_list = []
    while 1:
        if menu_sisain == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            sisain_first = sisain_news()
            menu_list.append(sisain_first)

        elif menu_sisain == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            sisain_second = printFirstList()
            menu_list.append(sisain_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def sisain_news():
    print("시사인 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
