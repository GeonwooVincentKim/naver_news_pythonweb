from SubMenu.Economy import *


def FinancialNews():
    print("This is FinancialNews")
    print("Please choose the menu you want")
    menu_financial = input("입력 : ")
    menu_list = []
    while 1:
        if menu_financial == '1':
            print("잠시만 기다려주세요..")
            time.sleep(0.5)
            financial_first = financial_news()
            menu_list.append(financial_first)

        elif menu_financial == '2':
            print("Back to the Future")
            from SubMenu.Economy import printSecondList
            financial_second = printSecondList()
            menu_list.append(financial_second)
            break

        else:
            print("번호를 잘못 누르셨어요ㅠㅠ(메밀티콘)")
            break


def financial_news():
    print("파이낸셜 경제 뉴스에 오신 것을 환영합니다.")
    print("원하시는 버튼을 선택하세요")
