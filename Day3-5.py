while True:
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    a=input('請輸入選項(數字)')
    a=int(a)   
    if a==1:
        b=input('輸入被加數')
        c=input('輸入加數')
        b=int(b)
        c=int(c)
        d=b+c
        print(d)
    if a==2:
        b=input('輸入被減數')
        c=input('輸入減數')
        b=int(b)
        c=int(c)
        d=b-c
        print(d)
    if a==3:   
        b=input('輸入被乘數')
        c=input('輸入乘數')
        b=int(b)
        c=int(c)
        d=b*c
        print(d)
    if a==1:
        b=input('輸入被除數')
        c=input('輸入除數')
        b=int(b)
        c=int(c)
        d=b/c
        print(d)
    if a==5:
        break
     