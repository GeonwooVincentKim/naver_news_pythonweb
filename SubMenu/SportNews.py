from SportDong_A import SportDong_A
from SportSeoul import SportSeoul
from SportChosun import SportChosun
from SpotalKorea import SpotalKorea
from DailySport import DailySport
import time


def printThirdList():
    print("원하시는 스포츠 뉴스 사를 선택하세요")
    print("1. 스포츠동아")
    print("2. 스포츠서울")
    print("3. 스포츠조선")
    print("4. 스포탈코리아")
    print("5. 일간스포츠")
    print("6. 메인메뉴로")
    print("7. 종료")
    menu_sport_select = input()
    menu_list = []

    while 1:
        if menu_sport_select == '1':
            print("No.1 Sport")
            first_sport = SportDong_A()
            menu_list.append(first_sport)
            break

        elif menu_sport_select == '2':
            print("No.2 Sport")
            second_sport = SportSeoul()
            menu_list.append(second_sport)

        elif menu_sport_select == '3':
            print("No.3 Sport")
            third_sport = SportChosun()
            menu_list.append(third_sport)

        elif menu_sport_select == '4':
            print("No.4 Sport")
            fourth_sport = SpotalKorea()
            menu_list.append(fourth_sport)

        elif menu_sport_select == '5':
            print("No.5 Sport")
            fifth_sport = DailySport()
            menu_list.append(fifth_sport)

        elif menu_sport_select == '6':
            print("Going back to Main File")
            from Main import select_menu
            sixth_sport = select_menu()
            menu_list.append(sixth_sport)

        elif menu_sport_select == '7':
            print("Shutting down the program")
            exit(0)
            break
        else:
            print("다른 번호들은 존재하지 않습니다. 다시 눌러주세요")
