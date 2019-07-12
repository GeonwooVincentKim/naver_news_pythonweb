from SubMenu.News import *


def Jiji():
    print("This is Jiji News")
    print("Please choose the menu you want")
    menu_jiji = input("입력 : ")
    menu_list = []
    while 1:
        if menu_jiji == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            Jiji_first = jiji_news()
            menu_list.append(Jiji_first)

        elif menu_jiji == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            jiji_second = printFirstList()
            menu_list.append(jiji_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def jiji_news():
    print("지지통신에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
