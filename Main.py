from SubMenu.ManageAllFile import *
from SubMenu.News import *
import time


class MainNews:
    def __init__(self, select):
        if select is None:
            select = {}
        self.select = select
    # def __init__(self, news, economy, sports, board_casting):
    #     if news is None:
    #         news = {}
    #     if economy is None:
    #         economy = {}
    #     if sports is None:
    #         sports = {}
    #     if board_casting is None:
    #         board_casting = {}
    #     self.news = news
    #     self.economy = economy
    #     self.sports = sports
    #     self.board_casting = board_casting


def select_menu():
    print("원하시는 메뉴를 선택하세요")
    print("1. 뉴스")
    print("2. 경제")
    print("3. 스포츠뉴스")
    print("4. 방송사")
    print("5. 종료")
    menu_input = input("메뉴 선택 : ")
    menu_list = []
    while 1:
        if menu_input == '1':
            print("dfd")
            first = printFirstList()
            menu_list.append(first)
            break

        elif menu_input == '2':
            print("break")
            second = printSecondList()
            menu_list.append(second)
            break

        elif menu_input == '3':
            print("sadlkfj")
            third = printThirdList()
            menu_list.append(third)
        elif menu_input == '4':
            print("sadfdsaads")
            fourth = printFourthList()
            menu_list.append(fourth)

        elif menu_input == '5':
            print("Shutting down the program")
            exit(0)
        else:
            print("다른 번호들은 존재하지 않습니다. 다시 눌러주세요")


# def set_select():
#     print("원하시는 메뉴를 선택하세요")
#     print("1. 뉴스")
#     print("2. 경제")
#     print("3. 스포츠뉴스")
#     print("4. 방송사")
#     print("5. 종료")
#     select = News.select
#     select = input()
#     return int(select)


# def print_menu():
#     print("원하시는 메뉴를 선택하세요")
#     print("1. 뉴스")
#     print("2. 경제")
#     print("3. 스포츠뉴스")
#     print("4. 방송사")
#     print("5. 종료")
#     menu_select = input()
#     return int(menu_select)


# def run():
#     menu_list = []
#     while 1:
#         menu_select = set_select()
#         if menu_select == 1:
#             print("dfd")
#             first = printFirstList()
#             menu_list.append(first)
#
#         elif menu_select == 2:
#             print("break")
#             second = printSecondList()
#             menu_list.append(second)
#         elif menu_select == 3:
#             print("sadlkfj")
#             third = printThirdList()
#             menu_list.append(third)
#         elif menu_select == 4:
#             print("sadfdsaads")
#             fourth = printFourthList()
#             menu_list.append(fourth)
#         elif menu_select == 5:
#             print("Shutting down the program")
#             exit(0)
#         else:
#             print("다른 번호들은 존재하지 않습니다. 다시 눌러주세요")


if __name__ == "__main__":
    main = MainNews.select_menu()
