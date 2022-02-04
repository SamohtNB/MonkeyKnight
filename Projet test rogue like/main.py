import pygame
from random import *
import keyboard
def ouverture(dossier):
        r=open(dossier,"r")
        r=r.read()
        b=""
        l=[]
        a=[]
        sorte=None
        for i in r:
            if i=='$':
                sorte=b
                b=""
            elif i =='@':
                a.append(b)
                l.append(a)
                a=[]
                b=""
            elif i==",":
                a.append(b)
                b=""
                
            else:
                b+=i
        return (l,sorte)

    
class salle():
    def __init__(self,data,b):
        self.datasalle=data
        self.dataimg=self.datasalle
        self.background=b
        dataimage,none=ouverture("Data\dataimage.txt")
        self.dataimg=[]
        for i in range(len(data)):
            l=[]
            for j in range(len(data[i])):
                l.append(pygame.image.load(dataimage[0][int(self.datasalle[i][j][:2])]))
            self.dataimg.append(l)
class Etage():
    
    def __init__(self,data):
        self.data=data
        self.map,self.none=ouverture(self.data)
        
        self.niveau=self.map[randint(0,len(self.map)-1)]
    
        self.map.append(self.niveau)
        self.niveau=self.niveau[0]
        a=ouverture(self.niveau)
        background=a[1]
        a=a[0]
        
        self.niveaudata=salle(a,background)
    

class player():
    def __init__(self):
        self.x=64
        self.y=256
        self.xs=[1,2]
        self.ys=[1,2]
        self.speedx=0
        self.speedy=0
        self.img=pygame.image.load("JeanEud.png")
        self.jump=0
    def gravite(self):
        pass
class test():
    def __init__(self):
        self.x0=750
        self.y0=350
        self.x=750
        self.y=350
        self.speedx=0
        self.speedy=8
        self.img=pygame.image.load("JeanEud.png")
Player=player()
Test=test()
screen =pygame.display.set_mode((1280,704))
etagetest=Etage("Etage1.txt")
continu=1
deplacement=1

while continu:
    for i in range(len(etagetest.niveaudata.datasalle)):
        for j in range(len(etagetest.niveaudata.datasalle[i])):
            screen.blit(etagetest.niveaudata.dataimg[i][j],((j)*64,(i)*64))
    screen.blit(Player.img,(Player.x,Player.y))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continu=0
    
    
    if keyboard.is_pressed("z") and Player.speedy==0 and Player.jump==0:
                Player.speedy=-24
                Player.jump=1
    if keyboard.is_pressed("s"):
                    
    
                    if etagetest.niveaudata.datasalle[Player.ys[1]+1][Player.xs[0]][2:4]!="01" and etagetest.niveaudata.datasalle[Player.ys[1]+1][Player.xs[1]][2:4]!="01":
                        Player.speedy+=1
    elif keyboard.is_pressed("d"):
                
                    if Player.speedx<20:
                        Player.speedx+=2
                    
    elif keyboard.is_pressed("q"):   
                    
                    if Player.speedx>-20:
                      
                            Player.speedx-=2
                        
                        
    if Player.speedx!=0:
        
        
        if Player.speedx<0:
            if etagetest.niveaudata.datasalle[Player.ys[0]][Player.xs[0]-1][2:4]!="01" and etagetest.niveaudata.datasalle[Player.ys[1]][Player.xs[0]-1][2:4]!="01":
                Player.x+=Player.speedx
                Player.speedx+=1.5
            else:
                if (Player.x+Player.speedx)-Player.xs[0]*64>0:
                    Player.x+=Player.speedx
                    Player.speedx+=1.5
                else:
                    Player.speedx=0
        else:
                
    
            if etagetest.niveaudata.datasalle[Player.ys[0]][Player.xs[1]+1][2:4]!="01" and etagetest.niveaudata.datasalle[Player.ys[1]][Player.xs[1]+1][2:4]!="01":
                Player.x+=Player.speedx
                Player.speedx-=1
            else:
                if (Player.xs[0]+1)*64-(Player.x+Player.speedx)>0:
                    Player.x+=Player.speedx
                    Player.speedx-=1
                else:
                    Player.speedx=0
    if etagetest.niveaudata.datasalle[Player.ys[1]+1][Player.xs[1]][2:4]!="01" and etagetest.niveaudata.datasalle[Player.ys[1]+1][Player.xs[0]][2:4]!="01":
        if etagetest.niveaudata.datasalle[Player.ys[0]-1][Player.xs[1]][2:4]=="01" and etagetest.niveaudata.datasalle[Player.ys[0]-1][Player.xs[0]][2:4]=="01":
            if (Player.ys[0])*64<(Player.y+Player.speedy):
                Player.y+=Player.speedy
                Player.speedy+=2    
                 
            else:
                Player.speedy=3
                Player.y+=Player.speedy
                
        else:
            Player.y+=Player.speedy
            Player.speedy+=2
    else:
        
        if Player.ys[1]*64>(Player.y+Player.speedy):
                    Player.y+=Player.speedy
                    Player.speedy+=1
        else:
                    Player.speedy=0
                    Player.jump=0
    
        
    
    Player.xs=[int(Player.x/64),int((Player.x+64)/64)]
    Player.ys=[int(Player.y/64),int((Player.y+64)/64)]
    
    screen.blit(Test.img,(Test.x,Test.y))
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)