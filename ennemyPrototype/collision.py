from baseEnnemy import *


def collision(enemy):
    if enemy.speedx!=0:
                
        if enemy.x%64<4 and enemy.speedx%64<4:
            if enemy.speedx<0:
                if  etagetest.niveaudata.datasalle[enemy.ys[1]][enemy.xs[0]-1][2:4]!="01":
                    enemy.x+=enemy.speedx
                    enemy.speedx+=1.5
                else:
                    if (enemy.x+enemy.speedx)-enemy.xs[0]*64>0:
                        enemy.x+=enemy.speedx
                        enemy.speedx+=1.5
                    else:
                        enemy.speedx=0
                        enemy.x=enemy.xs[0]*64
            else:
                    
        
                if etagetest.niveaudata.datasalle[enemy.ys[1]][enemy.xs[1]+1][2:4]!="01":
                    enemy.x+=enemy.speedx
                    enemy.speedx-=1
                else:
                    if (enemy.xs[0]+1)*64-(enemy.x+enemy.speedx)>0:
                        enemy.x+=enemy.speedx
                        enemy.speedx-=1
                    else:
                        enemy.speedx=0
                        enemy.x=enemy.xs[1]*64-1
        else:
            if enemy.speedx<0:
                if etagetest.niveaudata.datasalle[enemy.ys[0]][enemy.xs[0]-1][2:4]!="01" and etagetest.niveaudata.datasalle[enemy.ys[1]][enemy.xs[0]-1][2:4]!="01":
                    enemy.x+=enemy.speedx
                    enemy.speedx+=1.5
                else:
                    if (enemy.x+enemy.speedx)-enemy.xs[0]*64>0:
                        enemy.x+=enemy.speedx
                        enemy.speedx+=1.5
                    else:
                        enemy.speedx=0
                        enemy.x=enemy.xs[0]*64
            else:
                    
        
                if etagetest.niveaudata.datasalle[enemy.ys[0]][enemy.xs[1]+1][2:4]!="01" and etagetest.niveaudata.datasalle[enemy.ys[1]][enemy.xs[1]+1][2:4]!="01":
                    enemy.x+=enemy.speedx
                    enemy.speedx-=1
                else:
                    if (enemy.xs[0]+1)*64-(enemy.x+enemy.speedx)>0:
                        enemy.x+=enemy.speedx
                        enemy.speedx-=1
                    else:
                        enemy.speedx=0
                        enemy.x=enemy.xs[1]*64-1
            if enemy.liane==0:
                
                a=enemy.x%64
                textsurface = myfont.render(str(a), False, (0, 0, 0))
                screen.blit(textsurface,(70,25+32))
                if enemy.x%64==0:
                    if (etagetest.niveaudata.datasalle[enemy.ys[0]-1][enemy.xs[1]][2:4]=="01" or etagetest.niveaudata.datasalle[enemy.ys[0]-1][enemy.xs[0]][2:4]=="01") :
                            if (enemy.ys[0])*64<(enemy.y+enemy.speedy):
                                enemy.y+=enemy.speedy
                                enemy.speedy+=2   
                                
                            else:
                                
                                enemy.speedy=3
                                enemy.y+=enemy.speedy
                    if etagetest.niveaudata.datasalle[enemy.ys[1]+1][enemy.xs[1]][2:4]!="01" and etagetest.niveaudata.datasalle[enemy.ys[1]+1][enemy.xs[0]][2:4]!="01" :
            
                            enemy.y+=enemy.speedy
                            enemy.speedy+=2
                    else:
                        
                        if enemy.ys[1]*64>(enemy.y+enemy.speedy):
                                    enemy.y+=enemy.speedy
                                    enemy.speedy+=1
                        else:
                                    enemy.speedy=0
                                    enemy.jump=0
                                    enemy.y=enemy.ys[1]*64-1
                elif enemy.x%64>54 and enemy.direction=="+" :

                    if etagetest.niveaudata.datasalle[enemy.ys[0]-1][enemy.xs[1]][2:4]=="01":
                            if (enemy.ys[0])*64<(enemy.y+enemy.speedy):
                                enemy.y+=enemy.speedy
                                enemy.speedy+=2   
                                
                            else:
                                
                                enemy.speedy=3
                                enemy.y+=enemy.speedy
                    
                    if etagetest.niveaudata.datasalle[enemy.ys[1]+1][enemy.xs[1]][2:4]!="01":
                    
                            enemy.y+=enemy.speedy
                            enemy.speedy+=2
                    else:   
                        if enemy.ys[1]*64>(enemy.y+enemy.speedy):
                                enemy.y+=enemy.speedy
                                enemy.speedy+=1
                        else:
                                enemy.speedy=0
                                enemy.jump=0
                                enemy.y=enemy.ys[1]*64-1
                elif enemy.x%64<10 and enemy.direction=="-":

                    if etagetest.niveaudata.datasalle[enemy.ys[0]-1][enemy.xs[0]][2:4]=="01":
                            if (enemy.ys[0])*64<(enemy.y+enemy.speedy):
                                enemy.y+=enemy.speedy
                                enemy.speedy+=2   
                                
                            else:
                                
                                enemy.speedy=3
                                enemy.y+=enemy.speedy
                    if etagetest.niveaudata.datasalle[enemy.ys[1]+1][enemy.xs[0]][2:4]!="01":
                            enemy.y+=enemy.speedy
                            enemy.speedy+=2
                    else:   
                        
                        if enemy.ys[1]*64>(enemy.y+enemy.speedy):
                                enemy.y+=enemy.speedy
                                enemy.speedy+=1
                        else:
                                enemy.speedy=0
                                enemy.jump=0
                                enemy.y=enemy.ys[1]*64-1
                
                else: 
                    if etagetest.niveaudata.datasalle[enemy.ys[0]-1][enemy.xs[1]][2:4]=="01" or etagetest.niveaudata.datasalle[enemy.ys[0]-1][enemy.xs[0]][2:4]=="01":
                            if (enemy.ys[0])*64<(enemy.y+enemy.speedy):
                                enemy.y+=enemy.speedy
                                enemy.speedy+=2   
                                
                            else:
                                
                                enemy.speedy=3
                                enemy.y+=enemy.speedy
                    if etagetest.niveaudata.datasalle[enemy.ys[1]+1][enemy.xs[1]][2:4]!="01" and etagetest.niveaudata.datasalle[enemy.ys[1]+1][enemy.xs[0]][2:4]!="01":
            
                            enemy.y+=enemy.speedy
                            enemy.speedy+=2
                    else:
                        
                        if enemy.ys[1]*64>(enemy.y+enemy.speedy):
                                    enemy.y+=enemy.speedy
                                    enemy.speedy+=1
                        else:
                                    enemy.speedy=0
                                    enemy.jump=0
                                    enemy.y=enemy.ys[1]*64-1
            else:
                if etagetest.niveaudata.datasalle[enemy.ys[0]-1][enemy.xs[1]][2:4]=="01" or etagetest.niveaudata.datasalle[enemy.ys[0]-1][enemy.xs[0]][2:4]=="01":
                            if (enemy.ys[0])*64<(enemy.y+enemy.speedy):
                                pass
                            else:
                                enemy.speedy=0
                enemy.y+=enemy.speedy