import pygame
from baseEnnemy import*
from random import randint

class Big_Cockroach:
    def __init__(self,x,y):
        self.stats = Ennemy(10,100,4,False)
        self.x = x
        self.y = y
        #self.hb = pygame.rect(x,y,64,64)
        
    def __str__(self) -> str:
        return "the big cockroach deals {} dmg, possesses {} hp, moves {} u/f and is at position ({},{}) and is a passive ennemy that doesn't activly seek to hurt the player".format(self.stats.dmg,self.stats.hp,self.stats.mv,self.x,self.y)
    
    def movement(self):
        if self.stats.direction == 'r':
            self.x += self.stats.mv
        else:
            self.x-= self.stats.mv
    
    def get_pos(self):
        print("({},{})".format(self.x,self.y))

        
    def updateBC(self):
        self.movement()
        
class Bee:
    def __init__(self,x,y):
        self.stats=Ennemy(10,50,2,False)
        self.x = x
        self.y = y
        #self.hb = pygame.rect(x,y,64,64)
        
    def __str__(self) -> str:
        return "the bee deals {} dmg, possesses {} hp, moves {} u/f and is at position ({},{}) and is a passive ennemy that doesn't activly seek to hurt the player".format(self.stats.dmg,self.stats.hp,self.stats.mv,self.x,self.y)
    
    def get_pos(self):
        print("({},{})".format(self.x,self.y))

    
    def movement(self):
        if self.stats.direction == 'r':
            self.x += self.stats.mv
        else:
            self.x-= self.stats.mv
        pass #not finished, need a way to change the fly patern of the bee to a wave, don't know how to
        
    def updateBee(self):
        self.movement()
        
class Praying_Mantis:
    def __init__(self,x,y):
        self.stats=Ennemy(10,150,4,True)
        self.x = x
        self.y = y
        #self.hb = pygame.rect((x,y),(64,64))
        
    def __str__(self) -> str:
        return "the praying mantis deals {} dmg, possesses {} hp, moves {} u/f and is at position ({},{}) and is agressive".format(self.stats.dmg,self.stats.hp,self.stats.mv,self.x,self.y)
    
    def movement(self):
        if self.stats.direction == 'r':
            self.x += self.stats.mv
        else:
            self.x-= self.stats.mv
        
    def block(self):
        avoid = randint(1,100)
        if avoid<=34:
            return True
        return False
    
    def get_pos(self):
        print("({},{})".format(self.x,self.y))

        
    def updatePM(self):
        self.movement()