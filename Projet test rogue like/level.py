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
        self.choice2=[]
        for i in range(len(data)):
            l=[]
            for j in range(len(data[i])):
                if self.datasalle[i][j][2:4]=="02":
                    self.inpose=[i,j]
                if self.datasalle[i][j][2:4]=="04":
                    k=randint(1,6)
                    while k in self.choice2:
                        k=randint(1,6)
                    data2=ouverture("Data\datapersonnage.txt")
                    self.choice2.append(k)
                    self.choice.append([pygame.transform.scale(pygame.image.load(data2[0][k][0]+"\A1.png"), (64,64)),[j*64,i*64],k])
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
        self.niveau=choice(self.map[0])
        self.niv=self.niveau
        
        a=ouverture(self.niveau)
        background=a[1]
        a=a[0]
        
        self.niveaudata=salle(a,background)
    

class player():
    def __init__(self,pose,typ):
        data=ouverture("Data\datapersonnage.txt")
        self.liane=0
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
        self.hpmax=self.hp
        if self.type==6:
            self.armor=30
        self.attack=int(self.data[self.type][3])
        self.direction="+"
        self.timeattack=None
        self.basehealth=self.hp
        self.imo=0
        self.anim=0
        self.invul=0
        self.conditionult=0
        self.ultac=0
    def ult(self):
        if self.typ==0:
            if self.condionult!=60*30:
                self.conionult+=1
            else:
                self.ultac=1
        elif self.typ==1:
            if self.conditionult>80:
                self.ultac=1
        elif self.typ==2:
            if self.conditionult>7:
                self.ultac=1
            #one shot=pv
        elif self.typ==3:
            if self.conditionult>10:
                self.ultac=1
            #if enemy freeze degat*2
        elif self.typ==4:
            if self.conditionult>0:
                self.ultac=1
        elif self.typ==5:
            if self.conditionult>50:
                self.ultac=1
        elif self.typ==6:
            if self.armor>50:
                self.ultac=1
    def gravite(self):
            pass


def main(level,niv,screen,Ally):
    heart=pygame.transform.scale(pygame.image.load("data/hearth.png"),(30,30))
    shield=pygame.transform.scale(pygame.image.load("data/shield.png"),(30,30))
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    etagetest=Etage(level,niv)
    
    continu=1
    if Ally==[]:
        Ally.append(player(etagetest.niveaudata.inpose,0))
    Ally[0].x=etagetest.niveaudata.inpose[1]*64
    Ally[0].y=etagetest.niveaudata.inpose[0]*64
    while continu==1:
        screen.blit(etagetest.niveaudata.background,(0,0))
        for i in range(len(etagetest.niveaudata.datasalle)):
            for j in range(len(etagetest.niveaudata.datasalle[i])):
                screen.blit(etagetest.niveaudata.dataimg[i][j],((j)*64,(i)*64))
        if Ally[0].direction=="+":
            if Ally[0].jump==0:
                if Ally[0].anim==0:
                    screen.blit(Ally[0].imgimo,(Ally[0].x,Ally[0].y))
                    
                elif Ally[0].anim<11:
                    screen.blit(Ally[0].img1,(Ally[0].x,Ally[0].y))
                    
                    
                else:
                    screen.blit(Ally[0].img2,(Ally[0].x,Ally[0].y))
                
            else:
                screen.blit(Ally[0].img3,(Ally[0].x,Ally[0].y))
        else:
            if Ally[0].jump==0:
                if Ally[0].anim==0:
                    screen.blit(Ally[0].imgimoret,(Ally[0].x,Ally[0].y))
                    
                elif Ally[0].anim<11:
                    screen.blit(Ally[0].img1ret,(Ally[0].x,Ally[0].y))
                    
                else:
                    screen.blit(Ally[0].img2ret,(Ally[0].x,Ally[0].y))
            else:
                screen.blit(Ally[0].img3ret,(Ally[0].x,Ally[0].y))
        if Ally[0].speedx==0:
                Ally[0].anim=0
        else:
                if Ally[0].anim==21:
                    Ally[0].anim=1
                else:
                    Ally[0].anim+=1
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return(0,etagetest.niv)
                if event.type == pygame.KEYDOWN:
     
                  if event.key == pygame.K_c:
                          dmg,effect,time=(attack.choice(Ally[0],Ally[0].type,Ally[0].xs,Ally[0].ys,Ally[0].direction))
                          etagetest.niveaudata.dmg.append(att(time,dmg,effect))
                  elif event.key == pygame.K_f:
                          dmg,effect,time=(attack.choice2(Ally[0],Ally[0].type,Ally[0].xs,Ally[0].ys,Ally[0].direction))
                          etagetest.niveaudata.dmg.append(att(time,dmg,effect))
                          Ally[0].imo=1
        if(etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[0]][:2]=="04" or etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[1]][:2]=="04"):

            Ally[0].liane=1
            if keyboard.is_pressed("z"):
                Ally[0].speedy=-5
            else:
                Ally[0].speedy=5
        else:
            Ally[0].liane=0
        if Ally[0].imo==0:                 
                if keyboard.is_pressed("z") and Ally[0].speedy==0 and Ally[0].jump==0:
                    Ally[0].speedy=-25
                    Ally[0].jump=1
                if keyboard.is_pressed("a"):
                    print(Ally[0].x,Ally[0].y)
                if keyboard.is_pressed("s"):
                        
        
                        if etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[0]][2:4]!="01" and etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[1]][2:4]!="01":
                            Ally[0].speedy+=1
        
                if keyboard.is_pressed("d"):
                            Ally[0].direction="+"
                            if Ally[0].speedx<Ally[0].speedxmax:
                                Ally[0].speedx+=2
                            
                if keyboard.is_pressed("q"):   
                            Ally[0].direction="-"
                            if Ally[0].speedx>Ally[0].speedxmax*-1:
                              
                                    Ally[0].speedx-=2
        else:
            Ally[0].speedx=0
            Ally[0].speedy=0
        if etagetest.niveaudata.enemy==[]:
            for i in range(len(etagetest.niveaudata.datasalle)):
                for j in range(len(etagetest.niveaudata.datasalle[i])):
                    if etagetest.niveaudata.datasalle[i][j][2:4]=="03":
                        etagetest.niveaudata.dataimg[i][j]=pygame.image.load("data/block/P3.png")
                        
        if keyboard.is_pressed("s"):
           
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Ally[0].ys[0]][Ally[0].xs[0]][2:4]=="03":
                return(1,etagetest.niv)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[0]][2:4]=="03":
                return(1,etagetest.niv)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Ally[0].ys[0]][Ally[0].xs[1]][2:4]=="03":
                return(1,etagetest.niv)
            if etagetest.niveaudata.enemy==[] and etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[1]][2:4]=="03":
                return(1,etagetest.niv)
        
                
        """
        if keyboard.is_pressed("a"):
            etagetest.niveaudata.dmg=(attack.choice(Ally[0].type,Ally[0].xs,Ally[0].ys,Ally[0].direction))
          """                      
        
                            
        if Ally[0].speedx!=0:
            
            if Ally[0].x%64<4 and Ally[0].speedx%64<4:
                if Ally[0].speedx<0:
                    if  etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[0]-1][2:4]!="01":
                        Ally[0].x+=Ally[0].speedx
                        Ally[0].speedx+=1.5
                    else:
                        if (Ally[0].x+Ally[0].speedx)-Ally[0].xs[0]*64>0:
                            Ally[0].x+=Ally[0].speedx
                            Ally[0].speedx+=1.5
                        else:
                            Ally[0].speedx=0
                            Ally[0].x=Ally[0].xs[0]*64
                else:
                        
            
                    if etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[1]+1][2:4]!="01":
                        Ally[0].x+=Ally[0].speedx
                        Ally[0].speedx-=1
                    else:
                        if (Ally[0].xs[0]+1)*64-(Ally[0].x+Ally[0].speedx)>0:
                            Ally[0].x+=Ally[0].speedx
                            Ally[0].speedx-=1
                        else:
                            Ally[0].speedx=0
                            Ally[0].x=Ally[0].xs[1]*64-1
            else:
                if Ally[0].speedx<0:
                    if etagetest.niveaudata.datasalle[Ally[0].ys[0]][Ally[0].xs[0]-1][2:4]!="01" and etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[0]-1][2:4]!="01":
                        Ally[0].x+=Ally[0].speedx
                        Ally[0].speedx+=1.5
                    else:
                        if (Ally[0].x+Ally[0].speedx)-Ally[0].xs[0]*64>0:
                            Ally[0].x+=Ally[0].speedx
                            Ally[0].speedx+=1.5
                        else:
                            Ally[0].speedx=0
                            Ally[0].x=Ally[0].xs[0]*64
                else:
                        
            
                    if etagetest.niveaudata.datasalle[Ally[0].ys[0]][Ally[0].xs[1]+1][2:4]!="01" and etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[1]+1][2:4]!="01":
                        Ally[0].x+=Ally[0].speedx
                        Ally[0].speedx-=1
                    else:
                        if (Ally[0].xs[0]+1)*64-(Ally[0].x+Ally[0].speedx)>0:
                            Ally[0].x+=Ally[0].speedx
                            Ally[0].speedx-=1
                        else:
                            Ally[0].speedx=0
                            Ally[0].x=Ally[0].xs[1]*64-1
        if Ally[0].liane==0:
            if Ally[0].x%64==0:
                if (etagetest.niveaudata.datasalle[Ally[0].ys[0]-1][Ally[0].xs[1]][2:4]=="01" or etagetest.niveaudata.datasalle[Ally[0].ys[0]-1][Ally[0].xs[0]][2:4]=="01") :
                        if (Ally[0].ys[0])*64<(Ally[0].y+Ally[0].speedy):
                            Ally[0].y+=Ally[0].speedy
                            Ally[0].speedy+=2   
                             
                        else:
                            
                            Ally[0].speedy=3
                            Ally[0].y+=Ally[0].speedy
                if etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[1]][2:4]!="01" and etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[0]][2:4]!="01" :
        
                        Ally[0].y+=Ally[0].speedy
                        Ally[0].speedy+=2
                else:
                    
                    if Ally[0].ys[1]*64>(Ally[0].y+Ally[0].speedy):
                                Ally[0].y+=Ally[0].speedy
                                Ally[0].speedy+=1
                    else:
                                Ally[0].speedy=0
                                Ally[0].jump=0
                                Ally[0].y=Ally[0].ys[1]*64-1
            elif Ally[0].x%64>54 and Ally[0].direction=="+" :

                if etagetest.niveaudata.datasalle[Ally[0].ys[0]-1][Ally[0].xs[1]][2:4]=="01":
                        if (Ally[0].ys[0])*64<(Ally[0].y+Ally[0].speedy):
                            Ally[0].y+=Ally[0].speedy
                            Ally[0].speedy+=2   
                             
                        else:
                            
                            Ally[0].speedy=3
                            Ally[0].y+=Ally[0].speedy
                
                if etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[1]][2:4]!="01":
                   
                        Ally[0].y+=Ally[0].speedy
                        Ally[0].speedy+=2
                else:   
                    if Ally[0].ys[1]*64>(Ally[0].y+Ally[0].speedy):
                            Ally[0].y+=Ally[0].speedy
                            Ally[0].speedy+=1
                    else:
                            Ally[0].speedy=0
                            Ally[0].jump=0
                            Ally[0].y=Ally[0].ys[1]*64-1
            elif Ally[0].x%64<10 and Ally[0].direction=="-":

                if etagetest.niveaudata.datasalle[Ally[0].ys[0]-1][Ally[0].xs[0]][2:4]=="01":
                        if (Ally[0].ys[0])*64<(Ally[0].y+Ally[0].speedy):
                            Ally[0].y+=Ally[0].speedy
                            Ally[0].speedy+=2   
                             
                        else:
                            
                            Ally[0].speedy=3
                            Ally[0].y+=Ally[0].speedy
                if etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[0]][2:4]!="01":
                        Ally[0].y+=Ally[0].speedy
                        Ally[0].speedy+=2
                else:   
                    
                    if Ally[0].ys[1]*64>(Ally[0].y+Ally[0].speedy):
                            Ally[0].y+=Ally[0].speedy
                            Ally[0].speedy+=1
                    else:
                            Ally[0].speedy=0
                            Ally[0].jump=0
                            Ally[0].y=Ally[0].ys[1]*64-1
            
            else: 
                if etagetest.niveaudata.datasalle[Ally[0].ys[0]-1][Ally[0].xs[1]][2:4]=="01" or etagetest.niveaudata.datasalle[Ally[0].ys[0]-1][Ally[0].xs[0]][2:4]=="01":
                        if (Ally[0].ys[0])*64<(Ally[0].y+Ally[0].speedy):
                            Ally[0].y+=Ally[0].speedy
                            Ally[0].speedy+=2   
                             
                        else:
                            
                            Ally[0].speedy=3
                            Ally[0].y+=Ally[0].speedy
                if etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[1]][2:4]!="01" and etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[0]][2:4]!="01":
        
                        Ally[0].y+=Ally[0].speedy
                        Ally[0].speedy+=2
                else:
                    
                    if Ally[0].ys[1]*64>(Ally[0].y+Ally[0].speedy):
                                Ally[0].y+=Ally[0].speedy
                                Ally[0].speedy+=1
                    else:
                                Ally[0].speedy=0
                                Ally[0].jump=0
                                Ally[0].y=Ally[0].ys[1]*64-1
        else:
            if etagetest.niveaudata.datasalle[Ally[0].ys[0]-1][Ally[0].xs[1]][2:4]=="01" or etagetest.niveaudata.datasalle[Ally[0].ys[0]-1][Ally[0].xs[0]][2:4]=="01":
                        if (Ally[0].ys[0])*64<(Ally[0].y+Ally[0].speedy):
                            pass
                        else:
                            Ally[0].speedy=0
            Ally[0].y+=Ally[0].speedy
        if etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[1]][:2]=="02" or etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[0]][:2]=="02":
            for i in range(len(etagetest.niveaudata.datasalle)):
                for j in range(len(etagetest.niveaudata.datasalle[i])):
                    if etagetest.niveaudata.datasalle[i][j][2:4]=="02":
                        Ally[0].x=j*64
                        Ally[0].y=i*64
                        Ally[0].hp-=Ally[0].hpmax/2
                        
        if etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[1]][:2]=="14" or etagetest.niveaudata.datasalle[Ally[0].ys[1]][Ally[0].xs[0]][:2]=="14":
            for i in etagetest.niveaudata.choice:
               
                if int(i[1][1]/64)==Ally[0].ys[0] and (int(i[1][0]/64)==Ally[0].xs[0] or int(i[1][0]/64)==Ally[0].xs[0]):
                    print
                    screen.blit(pygame.transform.scale(pygame.image.load("Data\choice\A"+str(i[2])+".png"),(9*64,5*64)),(5*64,2*64))
                    if keyboard.is_pressed("z"):
                        Ally[0]=player(etagetest.niveaudata.inpose,i[2])
                        for i in range(3):
                            etagetest.niveaudata.choice.pop()
        if etagetest.niveaudata.datasalle[Ally[0].ys[1]+1][Ally[0].xs[1]][:2]=="03" or etagetest.niveaudata.datasalle[Ally[0].ys[0]+1][Ally[0].xs[0]][:2]=="03":
            if Ally[0].invul==0:
                Ally[0].invul=60
                Ally[0].hp-=15
        if Ally[0].invul!=0:
            Ally[0].invul-=1
        for i in etagetest.niveaudata.enemy:
            i.actu
        damage(etagetest.niveaudata.dmg,screen,Ally[0])
        Ally[0].xs=[int(Ally[0].x/64),int((Ally[0].x+64)/64)]
        Ally[0].ys=[int(Ally[0].y/64),int((Ally[0].y+64)/64)]
        for i in etagetest.niveaudata.choice:
            screen.blit(i[0],i[1])
        screen.blit(heart,(32,32))
        textsurface = myfont.render(str(Ally[0].hp), False, (0, 0, 0))
        screen.blit(textsurface,(70,25))
        if Ally[0].type==6:
            screen.blit(shield,(32,64))
            textsurface = myfont.render(str(Ally[0].armor), False, (0, 0, 0))
            screen.blit(textsurface,(70,25+32))
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)
        if Ally[0].hp<1:
            return(0,0)
