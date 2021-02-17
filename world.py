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
        self.bonusclock=pygame.time.get_ticks() #time in ms
        self.bonusperiod=self.enemyperiod*5 #en ms la période moyenne pour spwan les ennemis
        
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
            ax.y=min(self.ground-random.gauss(height,0.3*height),self.ground)
            ax.x=screen.width-width
            ax.faceleft=True
            ax.speed=random.gauss(10,3)
            ax.update()

    def generate_bonus(self,screen):
        current_time=pygame.time.get_ticks() #time in ms
        if current_time - self.bonusclock>random.gauss(self.bonusperiod,self.bonusperiod*0.1):            
            self.bonusclock=current_time
            #####
            # Faire une classe enemy et des sous classe pour chaque type
            # Faire une sous classe hache de la classe bullet avec tout les paramètres
            #####
            apple=Bullet()
            apple.action='Idle'
            self.add_movbod(apple)
            apple.add_sprites('pomme')
            apple.change_size(3) #taille
            apple.change_animspeed(4) #un peu moins vite
            width=apple.sprite.recttight[2]
            ph=self.player.height
            apple.y=min(self.ground-random.gauss(2*ph,0.5*ph),self.ground)
            # apple.x=min(max(random.gauss(screen.width/2,screen.width/10),width),screen.width-width)
            apple.x=random.uniform(0,screen.width-width)
            apple.moving=False
            apple.damage=-1
            apple.update()
            
    def handle_collision(self,target):
        for movbod2 in self.movbods:
            if target is not movbod2 and movbod2.damage!=0:
                if pygame.sprite.collide_mask(target.sprite,movbod2.sprite):
                    damage=movbod2.damage
                    if damage>0 and self.player.hitable: #pour les collisions avec les bullets
                        target.invicible_clock=pygame.time.get_ticks()
                        target.hitable=False
                        target.life-=damage
                    elif damage<0: #Pour les bonus pas d'invincibilité
                        target.life-=damage

                    movbod2.kill()
                    self.movbods.remove(movbod2)
        

    def update(self,screen):
        self.generate_enemies(screen)
        self.generate_bonus(screen)
        for movbod in self.movbods:
            movbod.update()
            if movbod.x+movbod.width > screen.width:
                movbod.hit_right(self)
            if movbod.x < 0:
                movbod.hit_left(self)
        self.handle_collision(self.player)