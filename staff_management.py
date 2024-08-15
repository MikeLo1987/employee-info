# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:13:41 2024

@author: thewh
"""

import pymysql, hashlib

conn = pymysql.connect(host='localhost', port=3307, user='mike', password='20240522', db='mike_db', charset='utf8')
cur = conn.cursor()

def myindex():
    print("管理者登入系統")
    print('-'*20)
    print('1.登入')
    print('2.註冊帳號')
    print('3.離開')

def myindex2():
    print('-'*20)
    print('1.查詢所有員工的資料')
    print('11.查詢指定員工的資料')
    print('2.修改員工資料')
    print('3.刪除員工帳號')
    print('4.離開')

def myindex3():
    print('-'*20)
    print('1.修改姓名')
    print('2.修改密碼')
    print('3.修改電子郵件')
    print('4.離開')

def login():
    #def_account = 'mike'
    #def_password = '12345678'
    
    while True:
        account = input("請輸入帳號: ")
        
        if account == "":
            print("未輸入帳號，程式將返回主選單\n")
            break
        
        sql = "SELECT sf_account, sf_pwd FROM stuff_info WHERE sf_account = '" + account + "' AND sf_del=0"
        cur.execute(sql)
        #print(sql)
        info = cur.fetchone()
        #print(info)
        
        if info == None:
            print("帳號" + account + "不存在，程式將返回主選單\n")
            break
        elif account == info[0]:
            password = input("請輸入密碼: ")
            md5_pwd = md5(password)
            
            if md5_pwd == "":
                print("未輸入密碼，程式將返回主選單\n")
                break
            elif md5_pwd == info[1]:
                print("登入成功")
                mymenu2()
                break
            else:
                print("密碼錯誤，程式將返回主選單\n")
                break
                
def sign_up():
    while True:
        name = input('姓名：')
        if name == "":
            print('姓名不能為空白。')
            continue
        
        acc = input('帳號：')
        if acc == "":
            print('帳號不能為空白。')
            continue
        
        sql = "SELECT sf_account FROM stuff_info WHERE sf_del=0 AND sf_account='" + acc + "'"
        cur.execute(sql)
        data = cur.fetchone()
        if not data == None:
            print("{}帳號已存在，請重新輸入註冊資料。".format(acc))
            continue
        
        pwd = input('密碼：')
        if pwd == "":
            print('密碼不能為空白。')
            continue
        md5_pwd = md5(pwd)
        
        email = input('公司email：')
        level = input('職等：')
        sql_insert = "INSERT INTO `stuff_info`(`sf_name`, `sf_email`, `sf_account`, `sf_pwd`, `sf_level`) VALUES ('" + name + "', '" + email + "', '" + acc + "','" + md5_pwd + "','" + level + "')"
        #print(sql_insert)
        cur.execute(sql_insert)
        conn.commit() # 更新資料庫
        print("{}已註冊成功".format(acc))
        break

def get_staff_info(select):
    sql = "SELECT sf_name, sf_account, sf_pwd, sf_level FROM `stuff_info` WHERE sf_del=0;"
    cur.execute(sql)
    
    info = cur.fetchall() # 抓取所有資料
    return info
    
def update_staff_info():
    while True:
        #print('修改員工資料')
        #輸入想要修改的員工資料
        acc = input('請輸入欲修改之帳號：')
        #確認帳號是否存在
        sql = "SELECT sf_account, sf_name FROM stuff_info WHERE sf_del=0 AND sf_account='" + acc + "'"
        #print(sql)
        cur.execute(sql)
        data = cur.fetchone()
        #print(data)
        
        if data == None:
            print('無此帳號，請重新輸入')
            continue
        
        else:
            option = mymenu3()
            #print(option)
        
            if option == 'name':
                name = input('請輸入新名字: ')
                sql_update = "UPDATE stuff_info SET sf_name='" + name + "' WHERE sf_del=0 AND sf_account='" + acc + "'"
                #print(sql_update)
                cur.execute(sql_update)
                conn.commit()
                print('姓名修改成功')
                break
            elif option == 'pwd':
                pwd = input('請輸入新密碼: ')
                md5_pwd = md5(pwd)
                
                sql_update = "UPDATE stuff_info SET sf_pwd='" + md5_pwd + "' WHERE sf_del=0 AND sf_account='" + acc + "'"
                #print(sql_update)
                cur.execute(sql_update)
                conn.commit()
                print('密碼修改成功')
                break
            elif option == 'email':
                email = input('請輸入新電子信箱: ')
                sql_update = "UPDATE stuff_info SET sf_email='" + email + "' WHERE sf_del=0 AND sf_account='" + acc + "'"
                #print(sql_update)
                cur.execute(sql_update)
                conn.commit()
                print('電子信箱修改成功')
                break            
            

def del_staff_info():
    while True:
        #print('刪除員工資料')
        acc = input('請輸入欲刪除之帳號：')
        #確認帳號是否存在
        sql = "SELECT sf_account, sf_name FROM stuff_info WHERE sf_del=0 AND sf_account='" + acc + "'"
        #print(sql)
        cur.execute(sql)
        data = cur.fetchone()
        #print(data)
        
        if data == None:
            print('無此帳號，請重新輸入')
            continue
        
        confirm = input('確定要刪除此帳號嗎?(Y/n)')
        if (confirm == 'Y' or confirm == 'y'):
            sql_del = "UPDATE stuff_info SET sf_del=1 WHERE sf_del=0 AND sf_account='" + acc + "'"
            #print(sql_del)
            cur.execute(sql_del)
            conn.commit()
            print('帳號已刪除')
            break
        else:
            print('未執行刪除指令')
            break
    


def mymenu():
    while True:
        myindex()
        print()
        num = int(input('請輸入您要執行的動作：'))
        if num == 1:
            #print('登入功能')
            login()
        elif num == 2:
            #print('註冊功能')
            sign_up()
        elif num == 3:
            break
        
def mymenu2():
    while True:
        myindex2()
        print()
        num = int(input('請輸入您要執行的動作：'))
        if num == 1:
            all_staff = get_staff_info('all')
            print(all_staff)
        elif num == 11:
            staff = get_staff_info('one')
            print(staff)
        elif num == 2:
            update_staff_info()
        elif num == 3:
            del_staff_info()
        elif num == 4:
            break

def mymenu3():
    while True:
        myindex3()
        print()
        n = int(input("請輸入要修改的資料："))
        if n == 1:
            #print("修改姓名")
            return 'name'
        elif n == 2:
            #print("修改密碼")
            return 'pwd'
        elif n == 3:
            #print("修改電子郵件")
            return 'email'
        elif n == 4:
            break

def md5(pwd):
    md5_hash = hashlib.md5()
    md5_hash.update(pwd.encode('utf-8'))
    md5_value = md5_hash.hexdigest()
    
    return md5_value

mymenu()

cur.close()
conn.close()
