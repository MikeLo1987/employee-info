# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:40:59 2024

@author: thewh
"""

import pymysql

conn = pymysql.connect(host='localhost', port=3307, user='mike', password='20240522', db='mike_db', charset='utf8')
cur = conn.cursor()

def index():
    print('花蓮縣避難地點')
    print('-'*20)
    print('1.隸屬於花蓮分局之地點數量')
    print('2.隸屬於花蓮分局之可容納人數')
    print('3.各分局數量統計')
    print('4.各分局數量統計及可容納人數')
    print('5.壽豐鄉避難地點數量')
    print('6.壽豐鄉避難地點詳細資料')
    print('7.壽豐鄉平和村避難地點詳細資料')
    print('8.可容納人數最多之前五名地點詳細資料')
    print('9.位於吉安鄉、壽豐鄉、花蓮市')
    print('10.建築物名稱最後一個字為"學"')
    print('11.結束操作')
    
def menu():
    while True:
        index()
        print()
        n = int(input('請輸入號碼來執行功能：'))
        if n == 1:
            sql = "SELECT COUNT(*) AS '花蓮分局總計' FROM `hualien_evacuation_facility` WHERE unit = '花蓮分局';"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 2:
            sql = "SELECT SUM(capacity) AS '花蓮分局可容納人數' FROM `hualien_evacuation_facility` WHERE unit = '花蓮分局';"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 3:
            sql = "SELECT unit, COUNT(unit) AS '各分局統計' FROM `hualien_evacuation_facility` GROUP BY unit ORDER BY number ASC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 4:
            sql = "SELECT unit, COUNT(unit) AS '各分局統計', SUM(capacity) AS '可容納人數' FROM `hualien_evacuation_facility` GROUP BY unit ORDER BY number ASC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 5:
            sql = "SELECT COUNT(*) AS 'Shoufeng' FROM `hualien_evacuation_facility` WHERE township = '壽豐鄉';"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 6:
            sql = "SELECT building, village, address, capacity, unit, more_than_2_exits, dynamo, airy, lighting FROM `hualien_evacuation_facility` WHERE township = '壽豐鄉';"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 7:
            sql = "SELECT address, capacity, unit, more_than_2_exits, dynamo, airy, lighting FROM `hualien_evacuation_facility` WHERE township = '壽豐鄉' AND village = '平和村';"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 8:
            sql = "SELECT * FROM `hualien_evacuation_facility` ORDER BY capacity DESC LIMIT 5;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 9:
            sql = "SELECT * FROM `hualien_evacuation_facility` WHERE township IN ('吉安鄉', '壽豐鄉', '花蓮市') ORDER BY township DESC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 10:
            sql = "SELECT * FROM `hualien_evacuation_facility` WHERE building LIKE '%學' ORDER BY township DESC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 11:
            break