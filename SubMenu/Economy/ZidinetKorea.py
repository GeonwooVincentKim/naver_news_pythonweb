from SubMenu.Economy import *


def ZidnetKorea():
    print("This is ZidnetKorea")
    print("Please choose the menu you want")
    menu_zidnet = input("입력 : ")
    menu_list = []
    while 1:
        if menu_zidnet == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            zidnet_first = zidnet_news()
            menu_list.append(zidnet_first)

        elif menu_zidnet == '2':
            print("Back to the Future")

            from SubMenu.News import printSecondList
            zidnet_second = printSecondList()
            menu_list.append(zidnet_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")


def zidnet_news():
    print("zidnet 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")