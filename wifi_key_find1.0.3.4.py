#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Filename : wifi_key_find1.0.3.4.py


#换掉“用户名”、"密码"、"wi-fi名"、"wi-fi密码"！！！
#用于存wi-fi密码的Python程序
users1=["用户名1","用户名2","用户名3","用户名4","用户名5","用户名6"]
#users list
keydictionary1={"用户名1":"密码","用户名2":"密码","用户名3":"密码","用户名4":"密码","用户名5":"密码","用户名6":"密码"}
#users name-and-key' dictionary.
wifi_key1={"wi-fi名1":"wi-fi密码1","wi-fi名2":"wi-fi密码2"}
#wi_fi name-and-key' dictionary
while True:

    aa1=input("Please sign in first.\nInput your user name:")#"sign begin
    if aa1 in users1:
        userin=True
    else:
        userin=False
    if userin==True:
        keyyes=False
        while keyyes==False:
            key1=input("Input the key:")#input user-key
            if key1==keydictionary1[aa1]:
                keyyes=True
                break
            else:
                print("key wrong!")
    else:
        print("No this user!")#sign in end
    while keyyes==True:
            print("What do you want to do? \n(1.Look for key for wi-fi(input 'look for'),\n2.Look throw key list for wi-fi(input 'look throw'),\3.ndelete wi-fi key(input 'del'),\n4.sign out(input 'sign out)\n")
            command1=input('')
            if command1=="look for":
                wifiname=input("Name of wi-fi:\n")
                print("wifi's key is:",wifi_key1[wifiname],"\n","\n")
            elif command1=="look throw":
                print(wifi_key1,"\n","\n")
            elif command1=="del":
                name_willdel=input("input the name of need-delete wi-fi's name")
                del wifi_key1[name_willdel]
                print("command was finished.You delete the wi-fi named",name_willdel)
            elif command1=="sign out":
                excit=True
                break
            else:
                print("No this command!")