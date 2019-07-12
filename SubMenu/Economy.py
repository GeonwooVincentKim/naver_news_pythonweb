from Maeil import Maeil
from MoneyToday import MoneyToday
from SeoulEconomy import SeoulEconomy
from Asia import Asia
from EDaily import EDaily
from ChosunBiz import ChosunBiz
from ZidinetKorea import ZidnetKorea
from FinancialNews import FinancialNews
from KoreaEconomy import KoreaEconomy
from Herald import Herald

import time


def printSecondList():
    print("원하시는 스포츠 뉴스 사를 선택하세요")
    print("1. 매일경제")
    print("2. 머니투데이")
    print("3. 서울경제")
    print("4. 아시아경제")
    print("5. 이데일리")
    print("6. 조선비즈")
    print("7. 지디넷코리아")
    print("8. 파이낸셜뉴스")
    print("9. 한국경제")
    print("10. 헤럴드 경제")
    print("11. 메인메뉴로")
    print("12. 종료")
    menu_economy_select = input()
    menu_list = []

    while 1:
        if menu_economy_select == '1':
            print("No.1 Economy")
            first_economy = Maeil()
            menu_list.append(first_economy)

        elif menu_economy_select == '2':
            print("No.2 Economy")
            second_economy = MoneyToday()
            menu_list.append(second_economy)

        elif menu_economy_select == '3':
            print("No.3 Economy")
            third_economy = SeoulEconomy()
            menu_list.append(third_economy)

        elif menu_economy_select == '4':
            print("No.4 Economy")
            fourth_economy = Asia()
            menu_list.append(fourth_economy)

        elif menu_economy_select == '5':
            print("No.5 Economy")
            fifth_economy = EDaily()
            menu_list.append(fifth_economy)

        elif menu_economy_select == '6':
            print("No.6 Economy")
            sixth_economy = ChosunBiz()
            menu_list.append(sixth_economy)

        elif menu_economy_select == '7':
            print("No.7 Economy")
            seventh_economy = ZidnetKorea()
            menu_list.append(seventh_economy)

        elif menu_economy_select == '8':
            print("No.8 Economy")
            eight_economy = FinancialNews()
            menu_list.append(eight_economy)

        elif menu_economy_select == '9':
            print("No.9 Economy")
            nine_economy = KoreaEconomy()
            menu_list.append(nine_economy)

        elif menu_economy_select == '10':
            print("No.10 Economy")
            ten_economy = Herald()
            menu_list.append(ten_economy)

        elif menu_economy_select == '11':
            print("Going back to Main File")
            from Main import select_menu
            eleventh_economy = select_menu()
            menu_list.append(eleventh_economy)

        elif menu_economy_select == '12':
            print("Shutting down the program")
            exit(0)
            break
        else:
            print("다른 번호들은 존재하지 않습니다. 다시 눌러주세요")
