#!/usr/bin/env python
# Filename : 勾股数1.0.py
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

    if a in list1 and b in list1 and c in list1:
        print("Yes!")
    elif a/2 in list1 and b/2 in list1 and c/2 in list1:
        print("Yes!")
    elif a/3 in list1 and b/3 in list1 and c/3 in list1:
        print("Yes!")
    elif a/4 in list1 and b/4 in list1 and c/4 in list1:
        print("Yes!")
    elif a/5 in list1 and b/5 in list1 and c/5 in list1:
        print("Yes!")
    elif a/6 in list1 and b/6 in list1 and c/6 in list1:
        print("Yes!")
    elif a/7 in list1 and b/7 in list1 and c/7 in list1:
        print("Yes!")
    elif a/8 in list1 and b/8 in list1 and c/8 in list1:
        print("Yes!")
    elif a/9 in list1 and b/9 in list1 and c/9 in list1:
        print("Yes!")
    elif a/10 in list1 and b/10 in list1 and c/10 in list1:
        print("Yes!")
    elif a/11 in list1 and b/11 in list1 and c/11 in list1:
        print("Yes!")
    elif a/12 in list1 and b/12 in list1 and c/12 in list1:
        print("Yes!")
    elif a/13 in list1 and b/13 in list1 and c/13 in list1:
        print("Yes!")
    elif a/14 in list1 and b/14 in list1 and c/14 in list1:
        print("Yes!")
    elif a/15 in list1 and b/15 in list1 and c/15 in list1:
        print("Yes!")
    elif a/16 in list1 and b/16 in list1 and c/16 in list1:
        print("Yes!")
    elif a/17 in list1 and b/17 in list1 and c/17 in list1:
        print("Yes!")
    elif a/18 in list1 and b/18 in list1 and c/18 in list1:
        print("Yes!")
    elif a/19 in list1 and b/19 in list1 and c/19 in list1:
        print("Yes!")
    elif a/20 in list1 and b/20 in list1 and c/20 in list1:
        print("Yes!")



    elif a in list2 and b in list2 and c in list2:
        print("Yes!")
    elif a/2 in list2 and b/2 in list2 and c/2 in list2:
        print("Yes!")
    elif a/3 in list2 and b/3 in list2 and c/3 in list2:
        print("Yes!")
    elif a/4 in list2 and b/4 in list2 and c/4 in list2:
        print("Yes!")
    elif a/5 in list2 and b/5 in list2 and c/5 in list2:
        print("Yes!")
    elif a/6 in list2 and b/6 in list2 and c/6 in list2:
        print("Yes!")
    elif a/7 in list2 and b/7 in list2 and c/7 in list2:
        print("Yes!")
    elif a/8 in list2 and b/8 in list2 and c/8 in list2:
        print("Yes!")
    elif a/9 in list2 and b/9 in list2 and c/9 in list2:
        print("Yes!")
    elif a/10 in list2 and b/10 in list2 and c/10 in list2:
        print("Yes!")
    elif a/11 in list2 and b/11 in list2 and c/11 in list2:
        print("Yes!")
    elif a/12 in list2 and b/12 in list2 and c/12 in list2:
        print("Yes!")
    elif a/13 in list2 and b/13 in list2 and c/13 in list2:
        print("Yes!")
    elif a/14 in list2 and b/14 in list2 and c/14 in list2:
        print("Yes!")
    elif a/15 in list2 and b/15 in list2 and c/15 in list2:
        print("Yes!")
    elif a/16 in list2 and b/16 in list2 and c/16 in list2:
        print("Yes!")
    elif a/17 in list2 and b/17 in list2 and c/17 in list2:
        print("Yes!")
    elif a/18 in list2 and b/18 in list2 and c/18 in list2:
        print("Yes!")
    elif a/19 in list2 and b/19 in list2 and c/19 in list2:
        print("Yes!")
    elif a/20 in list2 and b/20 in list2 and c/20 in list2:
        print("Yes!")



    elif a in list3 and b in list3 and c in list3:
        print("Yes!")
    elif a/2 in list3 and b/2 in list3 and c/2 in list3:
        print("Yes!")
    elif a/3 in list3 and b/3 in list3 and c/3 in list3:
        print("Yes!")
    elif a/4 in list3 and b/4 in list3 and c/4 in list3:
        print("Yes!")
    elif a/5 in list3 and b/5 in list3 and c/5 in list3:
        print("Yes!")
    elif a/6 in list3 and b/6 in list3 and c/6 in list3:
        print("Yes!")
    elif a/7 in list3 and b/7 in list3 and c/7 in list3:
        print("Yes!")
    elif a/8 in list3 and b/8 in list3 and c/8 in list3:
        print("Yes!")
    elif a/9 in list3 and b/9 in list3 and c/9 in list3:
        print("Yes!")
    elif a/10 in list3 and b/10 in list3 and c/10 in list3:
        print("Yes!")
    elif a/11 in list3 and b/11 in list3 and c/11 in list3:
        print("Yes!")
    elif a/12 in list3 and b/12 in list3 and c/12 in list3:
        print("Yes!")
    elif a/13 in list3 and b/13 in list3 and c/13 in list3:
        print("Yes!")
    elif a/14 in list3 and b/14 in list3 and c/14 in list3:
        print("Yes!")
    elif a/15 in list3 and b/15 in list3 and c/15 in list3:
        print("Yes!")
    elif a/16 in list3 and b/16 in list3 and c/16 in list3:
        print("Yes!")
    elif a/17 in list3 and b/17 in list3 and c/17 in list3:
        print("Yes!")
    elif a/18 in list3 and b/18 in list3 and c/18 in list3:
        print("Yes!")
    elif a/19 in list3 and b/19 in list3 and c/19 in list3:
        print("Yes!")
    elif a/20 in list3 and b/20 in list3 and c/20 in list3:
        print("Yes!")



    elif a in list4 and b in list4 and c in list4:
        print("Yes!")
    elif a/2 in list4 and b/2 in list4 and c/2 in list4:
        print("Yes!")
    elif a/3 in list4 and b/3 in list4 and c/3 in list4:
        print("Yes!")
    elif a/4 in list4 and b/4 in list4 and c/4 in list4:
        print("Yes!")
    elif a/5 in list4 and b/5 in list4 and c/5 in list4:
        print("Yes!")
    elif a/6 in list4 and b/6 in list4 and c/6 in list4:
        print("Yes!")
    elif a/7 in list4 and b/7 in list4 and c/7 in list4:
        print("Yes!")
    elif a/8 in list4 and b/8 in list4 and c/8 in list4:
        print("Yes!")
    elif a/9 in list4 and b/9 in list4 and c/9 in list4:
        print("Yes!")
    elif a/10 in list4 and b/10 in list4 and c/10 in list4:
        print("Yes!")
    elif a/11 in list4 and b/11 in list4 and c/11 in list4:
        print("Yes!")
    elif a/12 in list4 and b/12 in list4 and c/12 in list4:
        print("Yes!")
    elif a/13 in list4 and b/13 in list4 and c/13 in list4:
        print("Yes!")
    elif a/14 in list4 and b/14 in list4 and c/14 in list4:
        print("Yes!")
    elif a/15 in list4 and b/15 in list4 and c/15 in list4:
        print("Yes!")
    elif a/16 in list4 and b/16 in list4 and c/16 in list4:
        print("Yes!")
    elif a/17 in list4 and b/17 in list4 and c/17 in list4:
        print("Yes!")
    elif a/18 in list4 and b/18 in list4 and c/18 in list4:
        print("Yes!")
    elif a/19 in list4 and b/19 in list4 and c/19 in list4:
        print("Yes!")
    elif a/20 in list4 and b/20 in list4 and c/20 in list4:
        print("Yes!")



    elif a in list5 and b in list5 and c in list5:
        print("Yes!")
    elif a/2 in list5 and b/2 in list5 and c/2 in list5:
        print("Yes!")
    elif a/3 in list5 and b/3 in list5 and c/3 in list5:
        print("Yes!")
    elif a/4 in list5 and b/4 in list5 and c/4 in list5:
        print("Yes!")
    elif a/5 in list5 and b/5 in list5 and c/5 in list5:
        print("Yes!")
    elif a/6 in list5 and b/6 in list5 and c/6 in list5:
        print("Yes!")
    elif a/7 in list5 and b/7 in list5 and c/7 in list5:
        print("Yes!")
    elif a/8 in list5 and b/8 in list5 and c/8 in list5:
        print("Yes!")
    elif a/9 in list5 and b/9 in list5 and c/9 in list5:
        print("Yes!")
    elif a/10 in list5 and b/10 in list5 and c/10 in list5:
        print("Yes!")
    elif a/11 in list5 and b/11 in list5 and c/11 in list5:
        print("Yes!")
    elif a/12 in list5 and b/12 in list5 and c/12 in list5:
        print("Yes!")
    elif a/13 in list5 and b/13 in list5 and c/13 in list5:
        print("Yes!")
    elif a/14 in list5 and b/14 in list5 and c/14 in list5:
        print("Yes!")
    elif a/15 in list5 and b/15 in list5 and c/15 in list5:
        print("Yes!")
    elif a/16 in list5 and b/16 in list5 and c/16 in list5:
        print("Yes!")
    elif a/17 in list5 and b/17 in list5 and c/17 in list5:
        print("Yes!")
    elif a/18 in list5 and b/18 in list5 and c/18 in list5:
        print("Yes!")
    elif a/19 in list5 and b/19 in list5 and c/19 in list5:
        print("Yes!")
    elif a/20 in list5 and b/20 in list5 and c/20 in list5:
        print("Yes!")



    elif a in list6 and b in list6 and c in list6:
        print("Yes!")
    elif a/2 in list6 and b/2 in list6 and c/2 in list6:
        print("Yes!")
    elif a/3 in list6 and b/3 in list6 and c/3 in list6:
        print("Yes!")
    elif a/4 in list6 and b/4 in list6 and c/4 in list6:
        print("Yes!")
    elif a/5 in list6 and b/5 in list6 and c/5 in list6:
        print("Yes!")
    elif a/6 in list6 and b/6 in list6 and c/6 in list6:
        print("Yes!")
    elif a/7 in list6 and b/7 in list6 and c/7 in list6:
        print("Yes!")
    elif a/8 in list6 and b/8 in list6 and c/8 in list6:
        print("Yes!")
    elif a/9 in list6 and b/9 in list6 and c/9 in list6:
        print("Yes!")
    elif a/10 in list6 and b/10 in list6 and c/10 in list6:
        print("Yes!")
    elif a/11 in list6 and b/11 in list6 and c/11 in list6:
        print("Yes!")
    elif a/12 in list6 and b/12 in list6 and c/12 in list6:
        print("Yes!")
    elif a/13 in list6 and b/13 in list6 and c/13 in list6:
        print("Yes!")
    elif a/14 in list6 and b/14 in list6 and c/14 in list6:
        print("Yes!")
    elif a/15 in list6 and b/15 in list6 and c/15 in list6:
        print("Yes!")
    elif a/16 in list6 and b/16 in list6 and c/16 in list6:
        print("Yes!")
    elif a/17 in list6 and b/17 in list6 and c/17 in list6:
        print("Yes!")
    elif a/18 in list6 and b/18 in list6 and c/18 in list6:
        print("Yes!")
    elif a/19 in list6 and b/19 in list6 and c/19 in list6:
        print("Yes!")
    elif a/20 in list6 and b/20 in list6 and c/20 in list6:
        print("Yes!")



    elif a in list7 and b in list7 and c in list7:
        print("Yes!")
    elif a/2 in list7 and b/2 in list7 and c/2 in list7:
        print("Yes!")
    elif a/3 in list7 and b/3 in list7 and c/3 in list7:
        print("Yes!")
    elif a/4 in list7 and b/4 in list7 and c/4 in list7:
        print("Yes!")
    elif a/5 in list7 and b/5 in list7 and c/5 in list7:
        print("Yes!")
    elif a/6 in list7 and b/6 in list7 and c/6 in list7:
        print("Yes!")
    elif a/7 in list7 and b/7 in list7 and c/7 in list7:
        print("Yes!")
    elif a/8 in list7 and b/8 in list7 and c/8 in list7:
        print("Yes!")
    elif a/9 in list7 and b/9 in list7 and c/9 in list7:
        print("Yes!")
    elif a/10 in list7 and b/10 in list7 and c/10 in list7:
        print("Yes!")
    elif a/11 in list7 and b/11 in list7 and c/11 in list7:
        print("Yes!")
    elif a/12 in list7 and b/12 in list7 and c/12 in list7:
        print("Yes!")
    elif a/13 in list7 and b/13 in list7 and c/13 in list7:
        print("Yes!")
    elif a/14 in list7 and b/14 in list7 and c/14 in list7:
        print("Yes!")
    elif a/15 in list7 and b/15 in list7 and c/15 in list7:
        print("Yes!")
    elif a/16 in list7 and b/16 in list7 and c/16 in list7:
        print("Yes!")
    elif a/17 in list7 and b/17 in list7 and c/17 in list7:
        print("Yes!")
    elif a/18 in list7 and b/18 in list7 and c/18 in list7:
        print("Yes!")
    elif a/19 in list7 and b/19 in list7 and c/19 in list7:
        print("Yes!")
    elif a/20 in list7 and b/20 in list7 and c/20 in list7:
        print("Yes!")



    elif a in list8 and b in list8 and c in list8:
        print("Yes!")
    elif a/2 in list8 and b/2 in list8 and c/2 in list8:
        print("Yes!")
    elif a/3 in list8 and b/3 in list8 and c/3 in list8:
        print("Yes!")
    elif a/4 in list8 and b/4 in list8 and c/4 in list8:
        print("Yes!")
    elif a/5 in list8 and b/5 in list8 and c/5 in list8:
        print("Yes!")
    elif a/6 in list8 and b/6 in list8 and c/6 in list8:
        print("Yes!")
    elif a/7 in list8 and b/7 in list8 and c/7 in list8:
        print("Yes!")
    elif a/8 in list8 and b/8 in list8 and c/8 in list8:
        print("Yes!")
    elif a/9 in list8 and b/9 in list8 and c/9 in list8:
        print("Yes!")
    elif a/10 in list8 and b/10 in list8 and c/10 in list8:
        print("Yes!")
    elif a/11 in list8 and b/11 in list8 and c/11 in list8:
        print("Yes!")
    elif a/12 in list8 and b/12 in list8 and c/12 in list8:
        print("Yes!")
    elif a/13 in list8 and b/13 in list8 and c/13 in list8:
        print("Yes!")
    elif a/14 in list8 and b/14 in list8 and c/14 in list8:
        print("Yes!")
    elif a/15 in list8 and b/15 in list8 and c/15 in list8:
        print("Yes!")
    elif a/16 in list8 and b/16 in list8 and c/16 in list8:
        print("Yes!")
    elif a/17 in list8 and b/17 in list8 and c/17 in list8:
        print("Yes!")
    elif a/18 in list8 and b/18 in list8 and c/18 in list8:
        print("Yes!")
    elif a/19 in list8 and b/19 in list8 and c/19 in list8:
        print("Yes!")
    elif a/20 in list8 and b/20 in list8 and c/20 in list8:
        print("Yes!")



    elif a in list9 and b in list9 and c in list9:
        print("Yes!")
    elif a/2 in list9 and b/2 in list9 and c/2 in list9:
        print("Yes!")
    elif a/3 in list9 and b/3 in list9 and c/3 in list9:
        print("Yes!")
    elif a/4 in list9 and b/4 in list9 and c/4 in list9:
        print("Yes!")
    elif a/5 in list9 and b/5 in list9 and c/5 in list9:
        print("Yes!")
    elif a/6 in list9 and b/6 in list9 and c/6 in list9:
        print("Yes!")
    elif a/7 in list9 and b/7 in list9 and c/7 in list9:
        print("Yes!")
    elif a/8 in list9 and b/8 in list9 and c/8 in list9:
        print("Yes!")
    elif a/9 in list9 and b/9 in list9 and c/9 in list9:
        print("Yes!")
    elif a/10 in list9 and b/10 in list9 and c/10 in list9:
        print("Yes!")
    elif a/11 in list9 and b/11 in list9 and c/11 in list9:
        print("Yes!")
    elif a/12 in list9 and b/12 in list9 and c/12 in list9:
        print("Yes!")
    elif a/13 in list9 and b/13 in list9 and c/13 in list9:
        print("Yes!")
    elif a/14 in list9 and b/14 in list9 and c/14 in list9:
        print("Yes!")
    elif a/15 in list9 and b/15 in list9 and c/15 in list9:
        print("Yes!")
    elif a/16 in list9 and b/16 in list9 and c/16 in list9:
        print("Yes!")
    elif a/17 in list9 and b/17 in list9 and c/17 in list9:
        print("Yes!")
    elif a/18 in list9 and b/18 in list9 and c/18 in list9:
        print("Yes!")
    elif a/19 in list9 and b/19 in list9 and c/19 in list9:
        print("Yes!")
    elif a/20 in list9 and b/20 in list9 and c/20 in list9:
        print("Yes!")



    elif a in list10 and b in list10 and c in list10:
        print("Yes!")
    elif a/2 in list10 and b/2 in list10 and c/2 in list10:
        print("Yes!")
    elif a/3 in list10 and b/3 in list10 and c/3 in list10:
        print("Yes!")
    elif a/4 in list10 and b/4 in list10 and c/4 in list10:
        print("Yes!")
    elif a/5 in list10 and b/5 in list10 and c/5 in list10:
        print("Yes!")
    elif a/6 in list10 and b/6 in list10 and c/6 in list10:
        print("Yes!")
    elif a/7 in list10 and b/7 in list10 and c/7 in list10:
        print("Yes!")
    elif a/8 in list10 and b/8 in list10 and c/8 in list10:
        print("Yes!")
    elif a/9 in list10 and b/9 in list10 and c/9 in list10:
        print("Yes!")
    elif a/10 in list10 and b/10 in list10 and c/10 in list10:
        print("Yes!")
    elif a/11 in list10 and b/11 in list10 and c/11 in list10:
        print("Yes!")
    elif a/12 in list10 and b/12 in list10 and c/12 in list10:
        print("Yes!")
    elif a/13 in list10 and b/13 in list10 and c/13 in list10:
        print("Yes!")
    elif a/14 in list10 and b/14 in list10 and c/14 in list10:
        print("Yes!")
    elif a/15 in list10 and b/15 in list10 and c/15 in list10:
        print("Yes!")
    elif a/16 in list10 and b/16 in list10 and c/16 in list10:
        print("Yes!")
    elif a/17 in list10 and b/17 in list10 and c/17 in list10:
        print("Yes!")
    elif a/18 in list10 and b/18 in list10 and c/18 in list10:
        print("Yes!")
    elif a/19 in list10 and b/19 in list10 and c/19 in list10:
        print("Yes!")
    elif a/20 in list10 and b/20 in list10 and c/20 in list10:
        print("Yes!")


    elif a in list11 and b in list11 and c in list11:
        print("Yes!")
    elif a/2 in list11 and b/2 in list11 and c/2 in list11:
        print("Yes!")
    elif a/3 in list11 and b/3 in list11 and c/3 in list11:
        print("Yes!")
    elif a/4 in list11 and b/4 in list11 and c/4 in list11:
        print("Yes!")
    elif a/5 in list11 and b/5 in list11 and c/5 in list11:
        print("Yes!")
    elif a/6 in list11 and b/6 in list11 and c/6 in list11:
        print("Yes!")
    elif a/7 in list11 and b/7 in list11 and c/7 in list11:
        print("Yes!")
    elif a/8 in list11 and b/8 in list11 and c/8 in list11:
        print("Yes!")
    elif a/9 in list11 and b/9 in list11 and c/9 in list11:
        print("Yes!")
    elif a/10 in list11 and b/10 in list11 and c/10 in list11:
        print("Yes!")
    elif a/11 in list11 and b/11 in list11 and c/11 in list11:
        print("Yes!")
    elif a/12 in list11 and b/12 in list11 and c/12 in list11:
        print("Yes!")
    elif a/13 in list11 and b/13 in list11 and c/13 in list11:
        print("Yes!")
    elif a/14 in list11 and b/14 in list11 and c/14 in list11:
        print("Yes!")
    elif a/15 in list11 and b/15 in list11 and c/15 in list11:
        print("Yes!")
    elif a/16 in list11 and b/16 in list11 and c/16 in list11:
        print("Yes!")
    elif a/17 in list11 and b/17 in list11 and c/17 in list11:
        print("Yes!")
    elif a/18 in list11 and b/18 in list11 and c/18 in list11:
        print("Yes!")
    elif a/19 in list11 and b/19 in list11 and c/19 in list11:
        print("Yes!")
    elif a/20 in list11 and b/20 in list11 and c/20 in list11:
        print("Yes!")



    elif a in list12 and b in list12 and c in list12:
        print("Yes!")
    elif a/2 in list12 and b/2 in list12 and c/2 in list12:
        print("Yes!")
    elif a/3 in list12 and b/3 in list12 and c/3 in list12:
        print("Yes!")
    elif a/4 in list12 and b/4 in list12 and c/4 in list12:
        print("Yes!")
    elif a/5 in list12 and b/5 in list12 and c/5 in list12:
        print("Yes!")
    elif a/6 in list12 and b/6 in list12 and c/6 in list12:
        print("Yes!")
    elif a/7 in list12 and b/7 in list12 and c/7 in list12:
        print("Yes!")
    elif a/8 in list12 and b/8 in list12 and c/8 in list12:
        print("Yes!")
    elif a/9 in list12 and b/9 in list12 and c/9 in list12:
        print("Yes!")
    elif a/10 in list12 and b/10 in list12 and c/10 in list12:
        print("Yes!")
    elif a/11 in list12 and b/11 in list12 and c/11 in list12:
        print("Yes!")
    elif a/12 in list12 and b/12 in list12 and c/12 in list12:
        print("Yes!")
    elif a/13 in list12 and b/13 in list12 and c/13 in list12:
        print("Yes!")
    elif a/14 in list12 and b/14 in list12 and c/14 in list12:
        print("Yes!")
    elif a/15 in list12 and b/15 in list12 and c/15 in list12:
        print("Yes!")
    elif a/16 in list12 and b/16 in list12 and c/16 in list12:
        print("Yes!")
    elif a/17 in list12 and b/17 in list12 and c/17 in list12:
        print("Yes!")
    elif a/18 in list12 and b/18 in list12 and c/18 in list12:
        print("Yes!")
    elif a/19 in list12 and b/19 in list12 and c/19 in list12:
        print("Yes!")
    elif a/20 in list12 and b/20 in list12 and c/20 in list12:
        print("Yes!")



    elif a in list13 and b in list13 and c in list13:
        print("Yes!")
    elif a/2 in list13 and b/2 in list13 and c/2 in list13:
        print("Yes!")
    elif a/3 in list13 and b/3 in list13 and c/3 in list13:
        print("Yes!")
    elif a/4 in list13 and b/4 in list13 and c/4 in list13:
        print("Yes!")
    elif a/5 in list13 and b/5 in list13 and c/5 in list13:
        print("Yes!")
    elif a/6 in list13 and b/6 in list13 and c/6 in list13:
        print("Yes!")
    elif a/7 in list13 and b/7 in list13 and c/7 in list13:
        print("Yes!")
    elif a/8 in list13 and b/8 in list13 and c/8 in list13:
        print("Yes!")
    elif a/9 in list13 and b/9 in list13 and c/9 in list13:
        print("Yes!")
    elif a/10 in list13 and b/10 in list13 and c/10 in list13:
        print("Yes!")
    elif a/11 in list13 and b/11 in list13 and c/11 in list13:
        print("Yes!")
    elif a/12 in list13 and b/12 in list13 and c/12 in list13:
        print("Yes!")
    elif a/13 in list13 and b/13 in list13 and c/13 in list13:
        print("Yes!")
    elif a/14 in list13 and b/14 in list13 and c/14 in list13:
        print("Yes!")
    elif a/15 in list13 and b/15 in list13 and c/15 in list13:
        print("Yes!")
    elif a/16 in list13 and b/16 in list13 and c/16 in list13:
        print("Yes!")
    elif a/17 in list13 and b/17 in list13 and c/17 in list13:
        print("Yes!")
    elif a/18 in list13 and b/18 in list13 and c/18 in list13:
        print("Yes!")
    elif a/19 in list13 and b/19 in list13 and c/19 in list13:
        print("Yes!")
    elif a/20 in list13 and b/20 in list13 and c/20 in list13:
        print("Yes!")
