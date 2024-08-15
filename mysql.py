# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:16:36 2024

@author: thewh
"""

import pymysql

conn = pymysql.connect(host='localhost', port=3307, user='mike', password='20240522', db='mike_db', charset='utf8')
cur = conn.cursor()

def insert(name, acc, pwd, phone, email, address):
    sql = "INSERT INTO `stuff_info`(`sf_name`, `sf_phone`, `sf_email`, `sf_address`, `sf_account`, `sf_pwd`) VALUES ('" + name + "', '" + phone + "', '" + email + "','" + address + "',  '" + acc + "','" + pwd + "')"
    cur.execute(sql)
    conn.commit() # 更新資料庫

def select(acc):
    sql = "SELECT sf_account, sf_pwd, sf_level, sf_name, sf_phone, sf_email, sf_address FROM `stuff_info` WHERE sf_del=0 AND sf_account='" + acc + "';"
    cur.execute(sql)
    info = cur.fetchone() # 抓取一筆資料
    return info
        
def update(option, acc, data):
    if option == 1:
        sql = "UPDATE stuff_info SET sf_phone='" + data + "' WHERE sf_del=0 AND sf_account='" + acc + "'"
        #print(sql)
        cur.execute(sql)
        conn.commit()
        
    elif option == 2:
        sql = "UPDATE stuff_info SET sf_address='" + data + "' WHERE sf_del=0 AND sf_account='" + acc + "'"
        #print(sql)
        cur.execute(sql)
        conn.commit()
        
    elif option == 3:
        sql = "UPDATE stuff_info SET sf_email='" + data + "' WHERE sf_del=0 AND sf_account='" + acc + "'"
        #print(sql)
        cur.execute(sql)
        conn.commit()
        
    elif option == 4:
        sql = "UPDATE stuff_info SET sf_pwd='" + data + "' WHERE sf_del=0 AND sf_account='" + acc + "'"
        #print(sql)
        cur.execute(sql)
        conn.commit()
        
def delete(acc):
    sql = "UPDATE stuff_info SET sf_del=1 WHERE sf_del=0 AND sf_account='" + acc + "'"
    #print(sql)
    cur.execute(sql)
    conn.commit()