# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:09:20 2024

@author: thewh
"""

import pymysql

conn = pymysql.connect(host='localhost', port=3307, user='mike', password='20240522', db='mike_db', charset='utf8')
cur = conn.cursor()

def index():
    print("台北捷運票價查詢")
    print('-'*20)
    print('1.全票票價')
    print('2.全票票價(指定起點站)')
    print('3.全票票價(指定終點站)')
    print('4.指定起點站且全票票價低於30元')
    print('5.捷運站點數量')
    print('6.指定起點站且全票票價低於30元時，可抵達之終點站數量')
    print('7.全票最高金額')
    print('8.指定起點站之行駛距離最短的10個捷運站')
    print('9.行駛距離最短的10個捷運站')
    print('10.指定起點站及終點站')
    print('11.結束操作')
    
def menu():
    while True:
        index()
        print()
        n = int(input('請輸入號碼來執行功能：'))
        if n == 1:
            sql = "SELECT start_station, end_station, full_fare FROM `taipei_metro_fare`;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 2:
            sql = "SELECT start_station, end_station, full_fare FROM `taipei_metro_fare` WHERE start_station = '南港展覽館' GROUP BY end_station;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 3:
            sql = "SELECT start_station, end_station, full_fare FROM `taipei_metro_fare` WHERE end_station = '南港展覽館' GROUP BY start_station;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 4:
            sql = "SELECT start_station, end_station, distance, full_fare FROM `taipei_metro_fare` WHERE start_station = '南港展覽館' AND full_fare <= 30 GROUP BY end_station ORDER BY distance ASC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 5:
            sql = "SELECT COUNT(DISTINCT end_station) AS 'number of stations' FROM `taipei_metro_fare`;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 6:
            sql = "SELECT COUNT(DISTINCT end_station) AS 'number of stations' FROM `taipei_metro_fare` WHERE start_station = '南港展覽館' AND full_fare <=30;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 7:
            sql = "SELECT MAX(full_fare) AS 'highest_fare' FROM `taipei_metro_fare`;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 8:
            sql = "SELECT start_station, end_station, distance, full_fare, children_fare, others_fare FROM `taipei_metro_fare` WHERE start_station = '南港展覽館' GROUP BY end_station ORDER BY distance DESC LIMIT 10;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 9:
            sql = "SELECT start_station, end_station, distance, full_fare FROM `taipei_metro_fare` GROUP BY distance ORDER BY distance DESC LIMIT 10;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 10:
            sql = "SELECT * FROM `taipei_metro_fare` WHERE start_station = '南港展覽館' AND end_station = '台北車站' GROUP BY distance;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 11:
            break