from urllib.request import urlopen
from RenminWang import *
from RenminWang import RenminWang
from GyeongHyang import GyeongHyang
from Gukmin import Gukmin
from Nocut import Nocut
from NewsTapa import NewsTapa
from NewDaily import NewDaily
from Newsis import Newsis
from Dailyian import Dailyian
from Dong_A import Dong_A
from DigitalTimes import DigialTimes
from MyDaily import MyDaily
from Munhua import Munhua
from Blotter import Blotter
from Seoul import Seoul
from Syegye import Syegye
from Sisain import Sisain
from EyeNews24 import EyeNews24
from OhMyNews import OhMyNews
from Jeonja import Jeonja
from Choseon import Choseon
from JoongAng import JoongAng
from Jiji import Jiji
from Hangyeorye import Hangyeorye
from Hanguk import Hanguk
import time


import requests
from bs4 import BeautifulSoup
from datetime import datetime
from operator import eq
import re
import json
import urllib

# 차트인 여부
# rank_chart = []
# song_chart = []

# def FirstList(articleUrl):
# html = urlopen("https://newsstand.naver.com"+articleUrl)
# bsObj = BeautifulSoup(html, "html.parser")
# return bsObj.find("", {}).findAll()
from SubMenu.ManageAllFile import *


def printFirstList():
    print("원하시는 뉴스 사를 선택해주세요")
    print("1. 인민망")
    print("2. 경향신문")
    print("3. 국민일보")
    print("4. 노컷뉴스")
    print("5. 뉴데일리")
    print("6. 뉴스타파")
    print("7. 뉴시스")
    print("8. 데일리안")
    print("9. 동아일보")
    print("10. 디지털타임즈")
    print("11. 마이데일리")
    print("12. 문화일보")
    print("13. 블로터")
    print("14. 서울신문")
    print("15. 세계일보")
    print("16. 시사인")
    print("17. 아이뉴스 24")
    print("18. 오마이뉴스")
    print("19. 전자신문")
    print("20. 조선일보")
    print("21. 중앙일보")
    print("22. 지지통신")
    print("23. 한겨레")
    print("24. 한국일보")
    print("25. 메인 메뉴로")
    print("26. 종료")
    menu_news_select = input()
    menu_list = []
    while 1:
        if menu_news_select == '1':
            print("No.1 News")
            first_news = RenminWang()
            menu_list.append(first_news)
            break

        elif menu_news_select == '2':
            print("No.2 News")
            second_news = GyeongHyang()
            menu_list.append(second_news)
            # break

        elif menu_news_select == '3':
            print("No.3 News")
            third_news = Gukmin()
            menu_list.append(third_news)
            # break

        elif menu_news_select == '4':
            print("No.4 News")
            fourth_news = Nocut()
            menu_list.append(fourth_news)

        elif menu_news_select == '5':
            print("No.5 News")
            fifth_news = NewDaily()
            menu_list.append(fifth_news)

        elif menu_news_select == '6':
            print("No.6 News")
            sixth_news = NewsTapa()
            menu_list.append(sixth_news)

        elif menu_news_select == '7':
            print("No.7 News")
            seventh_news = Newsis()
            menu_list.append(seventh_news)

        elif menu_news_select == '8':
            print("No.8 News")
            eight_news = Dailyian()
            menu_list.append(eight_news)

        elif menu_news_select == '9':
            print("No.9 News")
            nine_news = Dong_A()
            menu_list.append(nine_news)

        elif menu_news_select == '10':
            print("No.10 News")
            ten_news = DigialTimes()
            menu_list.append(ten_news)

        elif menu_news_select == '11':
            print("No.11 News")
            eleventh_news = MyDaily()
            menu_list.append(eleventh_news)

        elif menu_news_select == '12':
            print("No.12 News")
            twelve_news = Munhua()
            menu_list.append(twelve_news)

        elif menu_news_select == '13':
            print("No.13 News")
            thirteen_news = Blotter()
            menu_list.append(thirteen_news)

        elif menu_news_select == '14':
            print("No.14 News")
            fourteen_news = Seoul()
            menu_list.append(fourteen_news)

        elif menu_news_select == '15':
            print("No.15 News")
            fifteen_news = Syegye()
            menu_list.append(fifteen_news)

        elif menu_news_select == '16':
            print("No.16 News")
            sixteen_news = Sisain()
            menu_list.append(sixteen_news)

        elif menu_news_select == '17':
            print("No.17 News")
            seventeen_news = EyeNews24()
            menu_list.append(seventeen_news)

        elif menu_news_select == '18':
            print("No.18 News")
            eighteen_news = OhMyNews()
            menu_list.append(eighteen_news)

        elif menu_news_select == '19':
            print("No.19 News")
            nineteen_news = Jeonja()
            menu_list.append(nineteen_news)

        elif menu_news_select == '20':
            print("No.20 News")
            twenty_news = Choseon()
            menu_list.append(twenty_news)

        elif menu_news_select == '21':
            print("No.21 News")
            twenty_one_news = JoongAng()
            menu_list.append(twenty_one_news)

        elif menu_news_select == '22':
            print("No.22 News")
            twenty_two_news = Jiji()
            menu_list.append(twenty_two_news)

        elif menu_news_select == '23':
            print("No.23 News")
            twenty_three_news = Hangyeorye()
            menu_list.append(twenty_three_news)

        elif menu_news_select == '24':
            print("No.24 News")
            twenty_four_news = Hanguk()
            menu_list.append(twenty_four_news)

        elif menu_news_select == '25':
            print("Going back to Main File")
            # from Main import MainNews
            # back = MainNews(MainNews.select_menu)
            # menu_list.append(back)
            from Main import select_menu
            twenty_five_news = select_menu()
            menu_list.append(twenty_five_news)

        elif menu_news_select == '26':
            print("Shutting down the program")
            exit(0)
            break
        else:
            print("다른 번호들은 존재하지 않습니다. 다시 눌러주세요")

