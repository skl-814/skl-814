while True:
    year=int(input("输入年份:"))
    a=year%400
    b=year%4
    if a==0:
        print("这是闰年")
    elif a!=0 and b==0:
        print("这是闰年")
    else:
        print("这不是闰年")