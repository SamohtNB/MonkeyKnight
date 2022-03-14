import pygame
from baseEnnemy import*

VEL_ARROW = 10
VEL_FB = 5

class Scout:
    def __init__(self,x,y):
        self.stats=Ennemy(7,100,4,True)
        self.x = x
        self.y = y
        #self.hb = pygame.rect(x,y,64,64)
        
    def __str__(self) -> str:
        return "the scout deals {} dmg, possesses {} hp, moves {} u/f and is at position ({},{}) and is agressive".format(self.stats.dmg,self.stats.hp,self.stats.mv,self.x,self.y)
    
    def movement(self):
        if self.stats.direction == 'r':
            self.x += self.stats.mv
        else:
            self.x-= self.stats.mv
            
    def get_pos(self):
        print("({},{})".format(self.x,self.y))
        
    def updateScout(self):
        self.movement()

class Elf:
    def __init__(self,x,y):
        self.stats = Ennemy(5,100,4,1)
        self.x = x
        self.y = y
        #self.hb = pygame.Rect((64,64),(x,y))
        self.arrows = []
        
    def __str__(self) -> str:
        return "the elf deals {} dmg, possesses {} hp, moves {} u/f and is at position ({},{}) and is agressive".format(self.stats.dmg,self.stats.hp,self.stats.mv,self.x,self.y)
    
    def movement(self):
        if self.stats.direction == 'r':
            self.x += self.stats.mv
        else:
            self.x-= self.stats.mv
    
    def gets_arrows_array(self):
        return self.arrows
    
    def modif_hp(self,x):
        self.stats.hurt(x)
        
    def handle_arrow(self):
        for arrow in self.arrows:
            if self.stats.direction == 'r':
                arrow.x += VEL_ARROW
            else:
                arrow.x-= VEL_ARROW
        if len(self.arrows)<3:
            self.bullarrowxsets.append(pygame.rect((16,16),(self.x,self.y)))
            
    def get_pos(self):
        print("({},{})".format(self.x,self.y))

        
    def updateElf(self):
        self.movement()
        self.handle_arrow()
        
class Shaman:
    def __init__(self,x,y):
        self.stats = Ennemy(10,100,4,1)
        self.x = x
        self.y = y
        #self.hb = pygame.Rect((64,64),(x,y))
        self.fireBall = []
        
    def __str__(self) -> str:
        return "the shaman deals {} dmg, possesses {} hp, moves {} u/f and is at position ({},{}) and is agressive".format(self.stats.dmg,self.stats.hp,self.stats.mv,self.x,self.y)
    
    def movement(self):
        if self.stats.direction == 'r':
            self.x += self.stats.mv
        else:
            self.x-= self.stats.mv
    
    def get_fireBall_array(self):
        return self.fireBall
    
    def modif_hp(self,x):
        self.stats.hurt(x)
        
    def handle_fire_ball(self):
        for Fb in self.fireBall:
            if self.stats.direction == 'r':
                Fb.x += VEL_FB
            else:
                Fb.x-= VEL_FB
        if len(self.arrows)<3:
            self.bullarrowxsets.append(pygame.rect((32,32),(self.x,self.y)))
            
    def get_pos(self):
        print("({},{})".format(self.x,self.y))
        
    def updateShaman(self):
        self.movement()
        self.handle_fire_ball()