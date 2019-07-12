from JTBC import JTBC
from KBS import KBS
from KBS_World import KBSWorld
from MBC import MBC
from MBN import MBN
from OSEN import OSEN
from SBS import SBS
from YTN import YTN
from Yonhab import YonHab
from KoreaEconomy import KoreaEconomy
import time


def printFourthList():
    print("원하시는 방송사를 선택하세요")
    print("1. JTBC")
    print("2. KBS")
    print("3. KBS World")
    print("4. MBC")
    print("5. MBN")
    print("6. OSEN")
    print("7. SBS")
    print("8. YTN")
    print("9. 연합뉴스 TV")
    print("10. 한국경제 TV")
    print("11. 메인메뉴로")
    print("12. 종료")
    menu_broadcast_select = input()
    menu_list = []

    while 1:
        if menu_broadcast_select == '1':
            print("No.1")
            first_broadcast = JTBC()
            menu_list.append(first_broadcast)

        elif menu_broadcast_select == '2':
            print("No.2")
            second_broadcast = KBS()
            menu_list.append(second_broadcast)

        elif menu_broadcast_select == '3':
            print("No.3")
            third_broadcast = KBSWorld()
            menu_list.append(third_broadcast)

        elif menu_broadcast_select == '4':
            print("No.4")
            fourth_broadcast = MBC()
            menu_list.append(fourth_broadcast)

        elif menu_broadcast_select == '5':
            print("No.5")
            fifth_broadcast = MBN()
            menu_list.append(fifth_broadcast)

        elif menu_broadcast_select == '6':
            print("No.6")
            sixth_broadcast = OSEN()
            menu_list.append(sixth_broadcast)

        elif menu_broadcast_select == '7':
            print("No.7")
            seventh_broadcast = SBS()
            menu_list.append(seventh_broadcast)

        elif menu_broadcast_select == '8':
            print("No.8")
            eight_broadcast = YTN()
            menu_list.append(eight_broadcast)

        elif menu_broadcast_select == '9':
            print("No.9")
            nine_broadcast = YonHab()
            menu_list.append(nine_broadcast)

        elif menu_broadcast_select == '10':
            print("No.10")
            ten_broadcast = KoreaEconomy()
            menu_list.append(ten_broadcast)

        elif menu_broadcast_select == '11':
            print("Going back to Main File")
            from Main import select_menu
            eleventh_broadcast = select_menu()
            menu_list.append(eleventh_broadcast)

        elif menu_broadcast_select == '12':
            print("Shutting down the program")
            exit(0)
            break
        else:
            print("다른 번호들은 존재하지 않습니다. 다시 눌러주세요")
