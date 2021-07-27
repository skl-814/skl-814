#!/usr/bin/env python
#-*- coding: utf-8 -*- 
# Filename : 勾股数2.0.py
#这个程序用于判断一组数是否是勾股数

#勾股数列表
list1=[3,4,5]
list2=[5,12,13]
list3=[7,24,25]
list4=[8,15,17]
list5=[9,40,41]
list6=[11,60,61]
list7=[12,35,37]
list8=[13,84,85]
list9=[15,112,113]
list10=[20,21,29]
list11=[20,99,101]
list12=[48,55,73]
list13=[60,91,109]

print("这个程序用于判断一组数是否是勾股数")
while True:
    d=int(input("input a:"))
    e=int(input("input b:"))
    f=int(input("input c:"))
    if d>e and e>f:
        c=d;b=e;a=f
    elif d>f and f>e:
        c=d;b=f;a=e
    elif e>d and d>f:
        c=e;b=d;a=f
    elif e>f and f>d:
        c=e;b=f;a=d
    elif f>d and d>e:
        c=f;b=d;a=e
    elif f>e and e>d:
        c=f;b=e;a=d
    else:
        print("出错！")
        break

    print(a,b,c,sep="____")

    if a/3==b/4==c/5:
        num=True
    elif a/3==b/4==c/5:
        num=True
    elif a/5==b/12==c/13:
        num=True
    elif a/7==b/24==c/25:
        num=True
    elif a/8==b/15==c/17:
        num=True
    elif a/9==b/40==c/41:
        num=True
    elif a/11==b/60==c/61:
        num=True
    elif a/12==b/35==c/37:
        num=True
    elif a/13==b/84==c/85:
        num=True
    elif a/15==b/112==c/113:
        num=True
    elif a/20==b/21==c/29:
        num=True
    elif a/20==b/99==c/101:
        num=True
    elif a/48==b/55==c/73:
        num=True
    elif a/60==b/91==c/109:
        num=True
    else:
        num=False
    
    if num==True:
        print("Yes!")
    elif num==False:
        print("No!")
    else:
        print("Wrong!")
#Mader:SKL