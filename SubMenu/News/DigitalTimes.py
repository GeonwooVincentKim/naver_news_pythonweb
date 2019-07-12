from SubMenu.News import *


def DigialTimes():
    print("This is DigialTimes")
    print("Please choose the menu you want")
    menu_digital_times = input("입력 : ")
    menu_list = []
    while 1:
        if menu_digital_times == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            digital_times_first = digital_times_news()
            menu_list.append(digital_times_first)

        elif menu_digital_times == '2':
            print("Back to the Future")
            from SubMenu.News import printFirstList
            digital_times_second = printFirstList()
            menu_list.append(digital_times_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def digital_times_news():
    print("디지털 타임즈에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")