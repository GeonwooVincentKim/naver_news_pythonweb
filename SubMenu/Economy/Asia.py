from SubMenu.Economy import *


def Asia():
    print("This is Aisan Economy")
    print("Please choose the menu you want")
    menu_asia = input("입력 : ")
    menu_list = []
    while 1:
        if menu_asia == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            aisa_first = asia_news()
            menu_list.append(aisa_first)

        elif menu_asia == '2':
            print("Back to the Future")
            from SubMenu.Economy import printSecondList
            asia_second = printSecondList()
            menu_list.append(asia_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def asia_news():
    print("아시아 경제 일보에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
