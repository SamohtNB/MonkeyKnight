# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:40:09 2022

@author: remir

a=open("Room10.txt",'r')
b=a.readlines()
c='3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7@5,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,4'
c=c.split('@')
for i in range(len(c)):
    c[i]=c[i].split(",")
for i in range(len(c)):
    for j in range(len(c[i])):
        if c[i][j]=='1':
            c[i][j]='0'+c[i][j]+'00'
        else:
            c[i][j]='0'+c[i][j]+'01'
sol=''
for i in c:
    for j in i:
        sol=sol+j+","
    sol+='@'
print(sol)

"""

import keyboard
a=0
while True:
    if keyboard.is_pressed("q"):
        print("You pressed q")
        a+=1
    if a>30:
        break