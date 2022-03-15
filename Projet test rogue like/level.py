import pygame
from random import *
import keyboard
import attack
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

def damage(dmg,screen,Player):
        if dmg!=[]:
                temp=pygame.image.load(dmg[0][1])
                screen.blit(temp,(dmg[0][0][0]*64,dmg[0][0][1]*64))
                
                if pygame.time.get_ticks()-Player.timeattack>0:
                    dmg.pop(0)
                    Player.timeattack=pygame.time.get_ticks()
class salle():
    def __init__(self,data,b):
        self.datasalle=data
        self.dataimg=self.datasalle
        self.background=b
        dataimage,none=ouverture("Data\dataimage.txt")
        self.dataimg=[]
        self.enemy=[]
        for i in range(len(data)):
            l=[]
            for j in range(len(data[i])):
                if self.datasalle[i][j][2:4]=="02":
                    self.inpose=[i,j]
                if self.datasalle[i][j][4:6]!="00":
                    self.enemy.append(0)
                l.append(pygame.image.load(dataimage[0][int(self.datasalle[i][j][:2])]))
            self.dataimg.append(l)
        self.dmg=[]
        self.effect=None
        
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
    def __init__(self,pose):
        data=ouverture("Data\datapersonnage.txt")
        data=data[0]
        self.x=pose[1]*64
        self.y=pose[0]*64
        self.type=5
        self.xs=[pose[1],pose[1]+1]
        self.ys=[pose[0],pose[0]+1]
        self.speedx=int(data[self.type][2])
        self.speedy=0
        self.img=pygame.image.load(data[self.type][0])
        self.img=pygame.transform.scale(self.img, (64,64))
        self.jump=0
        self.health=int(data[self.type][1])
        self.attack=int(data[self.type][3])
        self.direction="+"
        self.timeattack=None
        
    def gravite(self):
        pass


def main(level):
    screen =pygame.display.set_mode((1280,704))
    etagetest=Etage(level)
    continu=1
    Player=player(etagetest.niveaudata.inpose)
    while continu:
        for i in range(len(etagetest.niveaudata.datasalle)):
            for j in range(len(etagetest.niveaudata.datasalle[i])):
                screen.blit(etagetest.niveaudata.dataimg[i][j],((j)*64,(i)*64))
        screen.blit(Player.img,(Player.x,Player.y))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
     
                  if event.key == pygame.K_a:
                      if etagetest.niveaudata.dmg==[]:
                          etagetest.niveaudata.dmg,etagetest.niveaudata.effect=(attack.choice(Player.type,Player.xs,Player.ys,Player.direction))
                          Player.timeattack=pygame.time.get_ticks()
        
        if keyboard.is_pressed("z") and Player.speedy==0 and Player.jump==0:
                    Player.speedy=-27
                    Player.jump=1
        if keyboard.is_pressed("s"):
                        
        
                        if etagetest.niveaudata.datasalle[Player.ys[1]+1][Player.xs[0]][2:4]!="01" and etagetest.niveaudata.datasalle[Player.ys[1]+1][Player.xs[1]][2:4]!="01":
                            Player.speedy+=1
        if keyboard.is_pressed("d"):
                        Player.direction="+"
                        if Player.speedx<20:
                            Player.speedx+=2
                        
        if keyboard.is_pressed("q"):   
                        Player.direction="-"
                        if Player.speedx>-20:
                          
                                Player.speedx-=2
        if keyboard.is_pressed("s"):
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Player.ys[0]][Player.xs[0]][2:4]!="03":
                print(1)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Player.ys[1]][Player.xs[0]][2:4]!="03":
                print(2)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Player.ys[0]][Player.xs[1]][2:4]!="03":
                print(3)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Player.ys[1]][Player.xs[1]][2:4]!="03":
                print(4)
        
                
        """
        if keyboard.is_pressed("a"):
            etagetest.niveaudata.dmg=(attack.choice(Player.type,Player.xs,Player.ys,Player.direction))
          """                      
                            
                            
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
                        Player.x=Player.xs[0]*64
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
                        Player.x=Player.xs[1]*64-1
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
                        Player.y=Player.ys[1]*64-1
        
            
        damage(etagetest.niveaudata.dmg,screen,Player)
        Player.xs=[int(Player.x/64),int((Player.x+64)/64)]
        Player.ys=[int(Player.y/64),int((Player.y+64)/64)]
        
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)