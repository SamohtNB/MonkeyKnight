import pygame
import level
screen =pygame.display.set_mode((1280,704))
continu=1
save=level.ouverture("save.txt")[0]
lev=0
while continu>0:
    for event in pygame.event.get():
        screen.blit(pygame.image.load("liam.jpg"),(0,0))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            continu=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print(save[lev][0])
                continu=level.main(save[lev][0])
    