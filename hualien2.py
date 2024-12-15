# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:08:07 2024

@author: thewh
"""

import pymysql

conn = pymysql.connect(host='localhost', port=3307, user='mike', password='20240522', db='mike_db', charset='utf8')
cur = conn.cursor()

def index():
    print('花蓮縣提供流感疫苗之院所')
    print('-'*20)
    print('1.在壽豐之院所')
    print('2.鄉立衛生所')
    print('3.列出所有院所(依行政區排序)')
    print('4.有提供自費疫苗之院所')
    print('5.位於壽豐鄉、吉安鄉之院所')
    print('6.位於壽豐鄉、吉安鄉之診所')
    print('7.各行政區院所數量')
    print('8.有提供自費疫苗且行政區為"鎮"之院所')
    print('9.非花蓮市之醫院')
    print('10.花蓮市第3~7間院所(依登錄順序)')
    print('11.結束操作')
    
def menu():
    while True:
        index()
        print()
        n = int(input('請輸入號碼來執行功能：'))
        if n == 1:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` WHERE district LIKE '壽豐_';"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 2:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` WHERE hospital LIKE '%衛生所' AND district LIKE '%鄉';"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 3:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` ORDER BY zip_code ASC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 4:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` WHERE remark LIKE '%自費%' ORDER BY zip_code ASC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 5:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` WHERE district IN ('壽豐鄉', '吉安鄉') ORDER BY district DESC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 6:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` WHERE district IN ('壽豐鄉', '吉安鄉') AND hospital LIKE '%診所' ORDER BY district DESC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 7:
            sql = "SELECT district, COUNT(district) AS '各行政區統計' FROM `hualien_county_influenza_vaccine` GROUP BY district ORDER BY `各行政區統計` DESC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 8:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` WHERE remark LIKE '%自費%' AND district LIKE '%鎮' ORDER BY zip_code ASC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 9:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` WHERE district NOT IN ('花蓮市') && hospital LIKE '%院' ORDER BY `zip_code` ASC;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 10:
            sql = "SELECT * FROM `hualien_county_influenza_vaccine` WHERE district='花蓮市' ORDER BY primary_key LIMIT 5 OFFSET 2;"
            cur.execute(sql)
            info = cur.fetchall()
            print(info)
            
        elif n == 11:
            break