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
    

class att:
    def __init__(self,time,value,effect):
        self.time=time
        self.value=value
        self.effect=effect
        self.intime=0
def damage(dmg,screen,Player):
        if dmg!=[]:
            
            for i in dmg:
                
                for j in i.value[0]:
    
                        temp=pygame.image.load(j[1])
                        screen.blit(temp,(j[0][0]*64,j[0][1]*64))
                
                i.intime+=1
                if i.intime>=i.time:
                    
                    i.value.pop(0)
                    i.intime=0
            for i in range(len(dmg)-1,-1,-1):

                if dmg[i].value==[]:
                    dmg.pop(i)
            if dmg==[]:
                Player.imo=0
            
class salle():
    def __init__(self,data,b):
        self.datasalle=data
        self.dataimg=self.datasalle
        self.background=pygame.image.load(b)
        dataimage,none=ouverture("Data\dataimage.txt")
        self.dataimg=[]
        self.enemy=[]
        self.choice=[]
        for i in range(len(data)):
            l=[]
            for j in range(len(data[i])):
    
                if self.datasalle[i][j][2:4]=="02":
                    self.inpose=[i,j]
                if self.datasalle[i][j][2:4]=="04":
                    k=randint(1,4)
                    while k in self.choice:
                        k=randint(1,4)
                    data2=ouverture("Data\datapersonnage.txt")
                    
                    self.choice.append([pygame.transform.scale(pygame.image.load(data2[0][k][0]+"\A1.png"), (64,64)),[j*64,i*64]])
                if self.datasalle[i][j][:2]=="02":
                    a=str(randint(1,5))
                    l.append(pygame.image.load(dataimage[0][int(self.datasalle[i][j][:2])]+a+".png"))
                elif self.datasalle[i][j][:2]=="01":
                     a=str(randint(1,3))
        
                     l.append(pygame.image.load(dataimage[0][int(self.datasalle[i][j][:2])]+a+".png"))
            
                else:
                    
                    l.append(pygame.image.load(dataimage[0][int(self.datasalle[i][j][:2])]))
            self.dataimg.append(l)
        self.dmg=[]
        self.effect=None
        
class Etage():
    
    def __init__(self,data,niv):
        self.data=data
        self.map,self.none=ouverture(self.data)
        for i in niv:
            self.map.remove(i)
        self.niveau=self.map[randint(0,len(self.map)-1)]
        self.niv=self.niveau
        
        self.niveau=self.niveau[0]
        a=ouverture(self.niveau)
        background=a[1]
        a=a[0]
        
        self.niveaudata=salle(a,background)
    

class player():
    def __init__(self,pose,typ):
        data=ouverture("Data\datapersonnage.txt")
        self.data=data[0]
        self.x=pose[1]*64
        self.y=pose[0]*64
        self.type=typ
        self.xs=[pose[1],pose[1]+1]
        self.ys=[pose[0],pose[0]+1]
        self.speedx=int(self.data[self.type][2])
        self.speedxmax=self.speedx*4.5
        self.speedy=0
        self.image=data[0][self.type]
        self.imgimo=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"\A1.png"),(64,64))
        self.imgimoret=pygame.transform.flip(self.imgimo,True,False)
        self.img1=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"\A2.png"),(64,64))
        self.img1ret=pygame.transform.flip(self.img1,True,False)
        self.img2=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"\A3.png"),(64,64))
        self.img2ret=pygame.transform.flip(self.img2,True,False)
        self.img3=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"\A4.png"),(64,64))
        self.img3ret=pygame.transform.flip(self.img3,True,False)
        self.jump=0
        self.hp=int(self.data[self.type][1])
        if self.type==6:
            self.armor=30
        self.attack=int(self.data[self.type][3])
        self.direction="+"
        self.timeattack=None
        self.basehealth=self.hp
        self.imo=0
        self.anim=0
    def gravite(self):
        pass


def main(level,niv,screen):
    heart=pygame.transform.scale(pygame.image.load("data/hearth.png"),(30,30))
    shield=pygame.transform.scale(pygame.image.load("data/shield.png"),(30,30))
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    etagetest=Etage(level,niv)
    
    continu=1
    Player=player(etagetest.niveaudata.inpose,3)
    while continu==1:
        screen.blit(etagetest.niveaudata.background,(0,0))
        for i in range(len(etagetest.niveaudata.datasalle)):
            for j in range(len(etagetest.niveaudata.datasalle[i])):
                screen.blit(etagetest.niveaudata.dataimg[i][j],((j)*64,(i)*64))
        if Player.direction=="+":
            if Player.jump==0:
                if Player.anim==0:
                    screen.blit(Player.imgimo,(Player.x,Player.y))
                    
                elif Player.anim<11:
                    screen.blit(Player.img1,(Player.x,Player.y))
                    
                    
                else:
                    screen.blit(Player.img2,(Player.x,Player.y))
                
            else:
                screen.blit(Player.img3,(Player.x,Player.y))
        else:
            if Player.jump==0:
                if Player.anim==0:
                    screen.blit(Player.imgimoret,(Player.x,Player.y))
                    
                elif Player.anim<11:
                    screen.blit(Player.img1ret,(Player.x,Player.y))
                    
                else:
                    screen.blit(Player.img2ret,(Player.x,Player.y))
            else:
                screen.blit(Player.img3ret,(Player.x,Player.y))
        if Player.speedx==0:
                Player.anim=0
        else:
                if Player.anim==21:
                    Player.anim=1
                else:
                    Player.anim+=1
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return(0,etagetest.niv)
                if event.type == pygame.KEYDOWN:
     
                  if event.key == pygame.K_c:
                          dmg,effect,time=(attack.choice(Player,Player.type,Player.xs,Player.ys,Player.direction))
                          etagetest.niveaudata.dmg.append(att(time,dmg,effect))
                  elif event.key == pygame.K_f:
                          dmg,effect,time=(attack.choice2(Player,Player.type,Player.xs,Player.ys,Player.direction))
                          etagetest.niveaudata.dmg.append(att(time,dmg,effect))
                          Player.imo=1
        if Player.imo==0:                 
                if keyboard.is_pressed("z") and Player.speedy==0 and Player.jump==0:
                    Player.speedy=-25
                    Player.jump=1
                if keyboard.is_pressed("s"):
                        
        
                        if etagetest.niveaudata.datasalle[Player.ys[1]+1][Player.xs[0]][2:4]!="01" and etagetest.niveaudata.datasalle[Player.ys[1]+1][Player.xs[1]][2:4]!="01":
                            Player.speedy+=1
        
                if keyboard.is_pressed("d"):
                            Player.direction="+"
                            if Player.speedx<Player.speedxmax:
                                Player.speedx+=2
                            
                if keyboard.is_pressed("q"):   
                            Player.direction="-"
                            if Player.speedx>Player.speedxmax*-1:
                              
                                    Player.speedx-=2
        else:
            Player.speedx=0
            Player.speedy=0
        if keyboard.is_pressed("s"):
           
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Player.ys[0]][Player.xs[0]][2:4]=="03":
                return(1,etagetest.niv)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Player.ys[1]][Player.xs[0]][2:4]=="03":
                return(1,etagetest.niv)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Player.ys[0]][Player.xs[1]][2:4]=="03":
                return(1,etagetest.niv)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Player.ys[1]][Player.xs[1]][2:4]=="03":
                return(1,etagetest.niv)
        
                
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
            if etagetest.niveaudata.datasalle[Player.ys[0]-1][Player.xs[1]][2:4]=="01" or etagetest.niveaudata.datasalle[Player.ys[0]-1][Player.xs[0]][2:4]=="01":
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
        
        for i in etagetest.niveaudata.enemy:
            i.actu
        damage(etagetest.niveaudata.dmg,screen,Player)
        Player.xs=[int(Player.x/64),int((Player.x+64)/64)]
        Player.ys=[int(Player.y/64),int((Player.y+64)/64)]
        for i in etagetest.niveaudata.choice:
            screen.blit(i[0],i[1])
        screen.blit(heart,(32,32))
        textsurface = myfont.render(str(Player.hp), False, (0, 0, 0))
        screen.blit(textsurface,(70,25))
        if Player.type==6:
            screen.blit(shield,(32,64))
            textsurface = myfont.render(str(Player.armor), False, (0, 0, 0))
            screen.blit(textsurface,(70,25+32))
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)
