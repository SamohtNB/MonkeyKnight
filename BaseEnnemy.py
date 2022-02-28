from unicodedata import name
from pygame import*

'''
state = is the ennemy alive or dead
if state = true , the ennemy is alive
if state = false, the ennemy is dead
'''

class Ennemy:
    def __init__(self,dmg,hp,mv,aggression):
        self.dmg = dmg
        self.hp = hp
        self.mv = mv
        self.agression =  aggression
        self.state = True
        
    def __str__(self):
        return "this unites deals {} damage, possesses {} health points and moves {} unites".format(self.dmg,self.hp,self.mv)
    
    def hurt(self,dmg):
        self.hp -= dmg
    
class Scout:
    def __init__(self,x,y):
        self.stats=Ennemy(7,100,4,True)
        self.x = x
        self.y = y
        #self.hb = pygame.rect(x,y,64,64)
        
    def __str__(self) -> str:
        return "the scout deals {} dmg, possesses {} hp, moves {} u/f and is at position ({},{}) and is agressive".format(self.stats.dmg,self.stats.hp,self.stats.mv,self.x,self.y)
    
    def movement(self):
        self.x += self.stats.mv

class BobLeGLorieux:
    def __init__(self):
        self.stats = Ennemy(10000000000,10**20,1,True)
        
    def __str__(self):
        return "voici l'être le plus glorieux qui a jamais éxiste, Bob Le Glorieux\nIl est invincible({} hp), te tues en un coup({} dmg),mais est très lent ({} u/s)\nLe concept de genre ou sexe ne s'applique pa sa lui dû à sa grandeur".format(self.stats.hp,self.stats.dmg,self.stats.mv)
            
    
if __name__ == '__main__':
    jacob = Scout(0,0)
    print(jacob)
    jacob.movement()
    jacob.stats.hurt(3)
    print(jacob)
    Bob = BobLeGLorieux()
    print(Bob)