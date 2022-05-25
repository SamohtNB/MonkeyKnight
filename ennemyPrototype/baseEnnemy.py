from cmath import cos
from email.header import Header
from email.mime import image
import pygame
from attack import*
import os

NUMBER_ENEMY = 18

'''
state = is the ennemy alive or dead
if state = true , the ennemy is alive
if state = false, the ennemy is dead
direction = the direction the ennemy is facing
l = the ennemy is facing left, r = the ennemy is facing right
type table:
1 = scout, 2 = elf, 3 = shaman
4 = big cockroach, 5 = bee, 6 = praying mantis
7 = turtoise, 8 = zombie, 9 = sorcerer
10 = bir rat, 11 = flying squirrel, 12 = procupine
13 = gard, 14 = soldier, 15 = musketeer
16 = gunman, 17 = noble, 18 = knight
'''

class Enemy:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.dmg = None
        self.hp = None
        self.mv = None
        self.type = type
        self.agression =  None
        self.state = True
        self.direction = 'r'
        self.by = y
        self.sprite = None
        
    def movement(self):
        if self.direction == 'r':
            self.x += self.mv
        else:
            self.x-= self.mv
        if self.type ==  5:
            self. y = cos(self.count) + self.by
        
    
    def attack(self):
        pass
    
    def update(self):
        self.movement()
        #self.attack()
        
    def __str__(self):
        return "this unites deals {} damage, possesses {} health points and moves {} unites \nthe unit is at the position ({},{})".format(self.dmg,self.hp,self.mv,self.x,self.y)

def recupStatsEnemy(enemy,type):
    with open("Enemy_stats.txt",'r',encoding="utf-8") as f:
        temp_lines = f.readlines()
    line = temp_lines[type-1].strip("\n")
    stats = line.split(" ")
    enemy.dmg = int(stats[1])
    enemy.hp = int(stats[2])
    enemy.mv = int(stats[3])
    enemy.agression = bool(stats[4])
    enemy.sprite = stats[0]
    
           
if __name__=="__main__":
    running = True
    counter = 0
    claude=Enemy(0,0,1)
    recupStatsEnemy(claude,claude.type)
    print(claude.dmg)