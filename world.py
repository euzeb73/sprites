import pygame
import random
from movbod import Bullet

class World():
    def __init__(self,player):
        self.player=player
        self.movbods=[self.player] #Moving bodies
        self.ground=600
        self.player.x=0
        self.player.y=self.ground
        self.bgcolor=(200,0,100)
        self.enemyclock=pygame.time.get_ticks() #time in ms
        self.enemyperiod=2000 #en ms la période moyenne pour spwan les ennemis
        
    def add_movbod(self,movbod):
        movbod.y=self.ground
        self.movbods.append(movbod)

    def generate_enemies(self,screen):
        current_time=pygame.time.get_ticks() #time in ms
        if current_time - self.enemyclock>random.gauss(self.enemyperiod,self.enemyperiod*0.1):            
            self.enemyclock=current_time
            #####
            # Faire une classe enemy et des sous classe pour chaque type
            # Faire une sous classe hache de la classe bullet avec tout les paramètres
            #####
            ax=Bullet()
            self.add_movbod(ax)
            ax.add_sprites('hache')
            ax.change_size(1.25) #taille
            ax.change_animspeed(4) #un peu moins vite
            height=ax.sprite.recttight[3]
            width=ax.sprite.recttight[2]
            ax.y=max(self.ground-random.gauss(height,0.3*height),0)
            ax.x=screen.width-width
            ax.faceleft=True
            ax.speed=random.gauss(10,3)
            ax.update()
            
    def handle_collision(self,target):
        for movbod2 in self.movbods:
            if target is not movbod2 and movbod2.damage>0:
                if pygame.sprite.collide_mask(target.sprite,movbod2.sprite):
                    target.life-=movbod2.damage
                    target.invicible_clock=pygame.time.get_ticks()
                    target.hitable=False
        

    def update(self,screen):
        self.generate_enemies(screen)
        for movbod in self.movbods:
            movbod.update()
            if movbod.x+movbod.width > screen.width:
                movbod.hit_right(self)
            if movbod.x < 0:
                movbod.hit_left(self)
        if self.player.hitable:
            self.handle_collision(self.player)