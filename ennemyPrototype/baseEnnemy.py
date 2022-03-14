import imp
import pygame
from unicodedata import name
from Forest_1 import*
from forest_2 import*

'''
state = is the ennemy alive or dead
if state = true , the ennemy is alive
if state = false, the ennemy is dead
direction = the direction the ennemy is facing
l = the ennemy is facing left, r = the ennemy is facing right
'''

class Ennemy:
    def __init__(self,dmg,hp,mv,aggression):
        self.dmg = dmg
        self.hp = hp
        self.mv = mv
        self.agression =  aggression
        self.state = True
        self.direction = 'r'
        
    def get_atk(self):
        return self.dmg
    
    def get_hp(self):
        return self.hp
    
    def get_mv(self):
        return self.mv
        
    def __str__(self):
        return "this unites deals {} damage, possesses {} health points and moves {} unites".format(self.dmg,self.hp,self.mv)
    
    def hurt(self,dmg):
        self.hp -= dmg
    

class BobLeGLorieux:
    def __init__(self):
        self.stats = Ennemy(10000000000,10**20,1,True)
        
    def __str__(self):
        return "voici l'être le plus glorieux qui a jamais éxiste, Bob Le Glorieux\nIl est invincible({} hp), te tues en un coup({} dmg),mais est très lent ({} u/s)\nLe concept de genre ou sexe ne s'applique pa sa lui dû à sa grandeur".format(self.stats.hp,self.stats.dmg,self.stats.mv)
            
    
if __name__ == '__main__':
    JC = Scout(10,10)
    marc = Elf(20,20)
    josef = Shaman(60,60)
    JB = Big_Cockroach(30,30)
    maya = Bee(40,40)
    JK = Praying_Mantis(50,50)
    print(JC)
    print(marc)
    print(josef)
    print(maya)
    print(JK)
    for i in range(4):
        JC.updateScout()
        marc.updateElf()
        josef.updateShaman()
        JB.updateBC()
        maya.updateBee()
        JK.updatePM()
        JC.get_pos()
        marc.get_pos()
        josef.get_pos()
        JB.get_pos()
        maya.get_pos()
        JK.get_pos()