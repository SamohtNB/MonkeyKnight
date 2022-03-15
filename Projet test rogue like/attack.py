# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:10:05 2022

@author: remir
"""

"""
0=Basique
1=Capusaint
2=Chamanzée
3=Tue marin
4=albus Dumbabouin
5=Ouistitigre
6=Guenondorf
7=Guerille
8=Euthanasique
9=Beau Bono Bonobo
"""
def choice(typ,xs,ys,direction):
    if typ==0:
        return coupbasique(xs,ys,direction,"JeanEud.png",None)
    elif typ==1:
        return coupbasique(xs,ys,direction,"JeanEud.png",None)
    elif typ==2:
        return coupbasique(xs,ys,direction,"JeanEud.png","Lightnighting")
    elif typ==3:
        return coupbasique(xs,ys,direction,"JeanEud.png","First hit")
    elif typ==4:
        return spell(xs,ys,direction,"attaque.png",5,None)
    elif typ==5:
        return spell(xs,ys,direction,"attaque.png",7,None)
def spell(xs,ys,direction,image,rang,effect):
    if direction=="+":
        l=[]
        for i in range(rang):
            l.append([[xs[1]+i,ys[1]],image])
        return(l,effect)
    if direction=="-":
        l=[]
        for i in range(rang):
            l.append([[xs[0]-i,ys[1]],image])
        return(l,effect)        
def coupbasique(xs,ys,direction,image,effect):
    if direction=="+":
        return([[[xs[1],ys[1]],image],[[xs[1]+1,ys[1]],image]],effect)
    if direction=="-":
        return([[[xs[0],ys[1]],image],[[xs[0]-1,ys[1]],image]],effect)