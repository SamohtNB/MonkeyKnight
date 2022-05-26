from cmath import cos
from email.header import Header
import pygame
from attack import*
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)

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

class Ennemy:
    def __init__(self,x,y,dmg,hp,mv,type,aggression):
        self.x = x
        self.y = y
        self.dmg = dmg
        self.hp = hp
        self.mv = mv
        self.type = type
        self.agression =  aggression
        self.state = True
        self.direction = 'r'
        self.by = y
        self.sprite = pygame.image.load(os.path.join('Assets', 'guenon.png'))
        
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

def draw_window(ennemy):
    
    WIN.blit(ennemy.sprite,(ennemy.x,ennemy.y))
    

if __name__=="__main__":
    running = True
    counter = 0
    claude=Ennemy(0,0,10,10,1,3,True)
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        claude.update()
        draw_window(claude)
        counter+=1