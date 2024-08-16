# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:13:41 2024

@author: thewh
"""

import hashlib, mysql, taipei_metro, hualien1, hualien2

def myindex():
    print("會員登入系統")
    print('-'*20)
    print('1.登入')
    print('2.註冊帳號')
    print('3.離開')

def myindex2():
    print('-'*20)
    print('1.台北捷運票價查詢')
    print('2.花蓮縣避難地點')
    print('3.花蓮縣提供流感疫苗之院所')
    print('4.會員資料')
    print('5.離開')

def myindex3():
    print('-'*20)
    print('1.查詢會員資料')
    print('2.修改聯絡電話')
    print('3.修改地址')
    print('4.修改電子郵件')
    print('5.修改密碼')
    print('6.刪除帳號')
    print('7.離開')

def mymenu():
    while True:
        myindex()
        print()
        n = int(input('請輸入號碼來執行功能：'))
        if n == 1:
            #print('登入功能')
            login()
        elif n == 2:
            #print('註冊功能')
            sign_up()
        elif n == 3:
            break
        
def mymenu2():
    while True:
        myindex2()
        print()
        n = int(input('請輸入號碼來執行功能：'))
        if n == 1:
            taipei_metro.menu()
        elif n == 2:
            hualien1.menu()
        elif n == 3:
            hualien2.menu()
        elif n == 4:
            mymenu3()
        elif n == 5:
            break

def mymenu3():
    while True:
        myindex3()
        print()
        n = int(input("請輸入號碼來執行功能："))
        if n == 1:
            #查詢會員資料
            print(mysql.select(account))
        elif n == 2:
            #修改聯絡電話
            update_member_info(1)
        elif n == 3:
            #修改地址
            update_member_info(2)
        elif n == 4:
            #修改電子郵件
            update_member_info(3)
        elif n == 5:
            #修改密碼
            update_member_info(4)
        elif n == 6:
            delete()            
        elif n == 7:
            break

def login():
    #def_account = 'mike'
    #def_password = '12345678'
    global account
    
    while True:
        account = input("請輸入帳號: ")
        
        if account == "":
            print("未輸入帳號，程式將返回主選單\n")
            break
        
        data = mysql.select(account)
        #print(info)
        
        if data == None:
            print("帳號" + account + "不存在，程式將返回主選單\n")
            break
        elif account == data[0]:
            password = input("請輸入密碼: ")
            md5_pwd = md5(password)
            
            if md5_pwd == "":
                print("未輸入密碼，程式將返回主選單\n")
                break
            elif md5_pwd == data[1]:
                print("登入成功")
                mymenu2()
                break
            else:
                print("密碼錯誤，程式將返回主選單\n")
                break
            
def sign_up():
    while True:
        while True:
            name = input('姓名：')
            if name == "":
                print('姓名為必填資料。')
            else:
                break
        
        while True:
            acc = input('帳號：')
            if acc == "":
                print('請輸入帳號。')
                continue
        
            data = mysql.select(acc)
            if data is not None:
                print("{}帳號已存在，請使用其他帳號。".format(acc))
            else:
                break
            
        while True:
            pwd = input('密碼：')
            if pwd == "":
                print('請輸入密碼。')
            else:
                md5_pwd = md5(pwd)
                break
        
        while True:
            phone = input('聯絡電話：')
            if phone == "":
                print('聯絡電話為必填資料。')
            else:
                break
        
        email = input('email：')
        address = input('地址：')
        
        mysql.insert(name, acc, md5_pwd, phone, email, address)
        
        print("{}已註冊成功".format(acc))
        break

def update_member_info(option):
    while True:
        #print('修改會員資料')
        if option == 1:
            phone = input('請輸入新的電話號碼: ')
            mysql.update(1, account, phone)
            print('電話修改成功。')
            break
        
        elif option == 2:
            address = input('請輸入新地址: ')
            mysql.update(2, account, address)
            print('地址修改成功。')
            break
        
        elif option == 3:
            email = input('請輸入新電子信箱: ')
            mysql.update(3, account, email)
            print('電子信箱修改成功。')
            break
        
        elif option == 4:
            pwd = input('請輸入新密碼: ')
            #待辦：新密碼不可為空白
            md5_pwd = md5(pwd)
            mysql.update(4, account, md5_pwd)
            print('密碼修改成功，請使用新密碼重新登入。')
            break #待辦：改成回到第一層選單

def delete():
    while True:
        #print('刪除帳號')        
        confirm = input('確定要刪除帳號嗎?(Y/n)')
        if (confirm == 'Y' or confirm == 'y'):
            mysql.delete(account)
            print('帳號已刪除')
            break #待辦：改成回到第一層選單
        else:
            print('未執行刪除指令')
            break

def md5(pwd):
    md5_hash = hashlib.md5()
    md5_hash.update(pwd.encode('utf-8'))
    md5_value = md5_hash.hexdigest()
    
    return md5_value

mymenu()

mysql.cur.close()
mysql.conn.close()
