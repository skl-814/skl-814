#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Filename : wifi_key_find1.0.3.4.py
users1=["skl","SKL","shp","SHP","wyf","WYF"]
#users list
keydictionary1={
    "skl":"skl415416","SKL":"skl415416",
    "shp":"shp415416","SHP":"shp415416",
    "wyf":"wyf415416","WYF":"wyf415416"
    }
#users name-and-key' dictionary.
wifi_key1={
    "Xiaomi_skl":"kskevlinskl",
    "ChinaNet-LpFb":"2fpqvjdk"
    }
#wi_fi name-and-key' dictionary
long__1=len(wifi_key1)
#def help():
def chelp():
    print("1.Look for key for wi-fi(input 'look for'),")
    print("2.Look throw key list for wi-fi(input 'look throw'),")
    print("3.Add new wifi,\n 4.delete wi-fi key(input 'del'),")
    print("5.sign out(input 'sign out)\n")


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
        print("Inpt some commands to begin.(Input 'chelp' to see help)")

        #Input command
        command1=input('')
        if command1=="cheip":
            chelp()
        elif command1=="look for":
            wifiname=input("Name of wi-fi:\n")
            print("wifi's key is:",wifi_key1.get(wifiname,"No this wi-fi"),"\n","\n")
        elif command1=="look throw":
            for name_2,key_2 in wifi_key1.items():
                dd_1=0
                dd_1=dd_1+1
                print(f"{dd_1}.name:{name_2}")
                print(f"key:{key_2}")
        elif command1=="del":
            name_willdel=input("input the name of need-delete wi-fi's name")
            del wifi_key1[name_willdel]
            print("command was finished.You delete the wi-fi named",name_willdel)
        elif command=="add":
            nnaame=input("input the name of wi-fi:\n")
            kkeeyy=input("input the key of wi-fi:\n")
            wifi_key1[nnaame]=kkeeyy
            print("The wi-fi list now is:\n")

            #print the now-wi-fi-dictionary
            for name_2,key_2 in wifi_key1.items():
                dd_1=0
                dd_1=dd_1+1
                print(f"{dd_1}.name:{name_2}")
                print(f"key:{key_2}")
        elif command1=="sign out":
            excit=True
            break
        else:
            print("No this command!")
        if excit==True:
            break
#mader:skl