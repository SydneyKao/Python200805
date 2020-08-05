# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:16:36 2020

@author: user
"""

d={}
while True:
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.中翻英')
    print('4.英翻中')
    print('5.測驗學習成果')
    print('6.離開系統')
    a=input('請輸入選項')
    a=int(a)
    while a==1:
        b=input("輸入英文(按o離開)")
        b=str(b)
        if b=='o' or c=='o':

            break
        c=input("輸入中文(按o離開)")
        c=str(c)
        d[b]=c
        if b=='o' or c=='o':
           
            break
    if a==2:
        print(d)
    while a==3:
            
        c=input("輸入中文(按o離開)")
        c=str(c)
        for k,v in d.items():
            if v == c :
                print(k)
        
        if b=='o' or c=='o':
            break  
    while a==4:
            
        c=input("輸入英文(按o離開)")
        c=str(c)
        for k,v in d.items():
            if k == c :
                print(v)
         
        
        if b=='o' or c=='o':
            break          
    if a==6:
        break
        
                    
            
        
    