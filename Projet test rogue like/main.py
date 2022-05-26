import pygame
import level
screen =pygame.display.set_mode((1280,704))
continu=1 
save=level.ouverture("save.txt")[0]
lev=0   
niveau=0
niv=[]
time=0
image=pygame.transform.scale(pygame.image.load("Data\main.png"), (1280,704))
image2=pygame.transform.scale(pygame.image.load("Data\main2.png"), (1280,704))
clock = pygame.time.Clock()
clock.tick(60)
ally=[]
while continu>0:
    for event in pygame.event.get():
        if niveau==0:
            if time<15:
                screen.blit(image,(0,0))
                
            else:
                screen.blit(image2,(0,0))
                
                
                
            
            pygame.display.flip()
            if time==30:
                time=0
            time+=1 
        if event.type == pygame.QUIT:
            continu=0
        if event.type== pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0]>320 and pos[0]<594:
                if pos[1]>535 and pos[1]<648:
                    for i in range(3):
                        (continu,lastlevel)=level.main(save[lev][0],niv,screen,ally)
                        niv.append(lastlevel)
                        niveau+=1
                            
                    delta=level.main("Chooselevel.txt",[],screen)
          
            if pos[0]>673 and pos[0]<925:
                if pos[1]>535 and pos[1]<648:
                    continu=0
            