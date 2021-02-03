import pygame
import glob
from sprite import Sprite

class Character():
    def __init__(self):
        self.x=0 #position en pixels du coin sup gauche
        self.y=0
        self.sprites=dict() #dictionnaire de sprites contenant les actions possibles
        self.actions=self.sprites.keys()
        self.action='Idle'
        self.moving=False
        self.faceleft=False
        self.speed=5 #vitesse horizontale (nb de pixels à chaque appui)
        self.jumptop=25  #hauteur du saut en nombre de speed 25
        self.width=10
        self.height=10

    def add_sprites(self,directory):
        '''charger les sprites situés dans le répertoire dic'''
        actions_files=glob.glob("{}/*(1).png".format(directory))
        spritesdic=dict()
        for file in actions_files:
            action=file.split(' ')[0].split('\\')[1]
            sprite=Sprite(action,directory)
            sprite.animslowingfact=3
            spritesdic[action]=sprite
        self.sprites=spritesdic
        self.sprite=spritesdic[self.action]
        self.actions=self.sprites.keys()

    
    def change_size(self,reducratio):
        '''change la taille de tous les sprites'''
        for action in self.actions:
            self.sprites[action].change_size(reducratio)

    def change_animspeed(self,animspeed,spritesaction=[]):
        '''change la vitesse danim pour les sprites dde la liste spritesaction
        ou pour tous si pas d'argument ou liste vide'''
        if spritesaction:
            for sprite in spritesaction:
                self.sprites[sprite].animslowingfact=animspeed
        else:
            for sprite in self.sprites.values:
                sprite.animslowingfact=animspeed

    def change_action(self,action):
        self.action=action
        self.sprite=self.sprites[self.action]
        self.sprite.index=0
    def go_left(self):
        if self.action!='Walk' and self.action!='Jump':
            self.change_action('Walk')
        self.moving=True
        self.faceleft=True
        self.update()
    def go_rigth(self):
        if self.action!='Walk' and self.action!='Jump':
            self.change_action('Walk')
        self.moving=True
        self.faceleft=False
        self.update()
    def jump(self):
        if self.action!='Jump':
            self.change_action('Jump')
            self.jumpcount=0
            self.startingalt=self.y #plus tard sera remplacé par des tests de collision
        self.update()
    def stop(self):
        if self.action!='Idle' and self.action!='Jump':
            self.change_action('Idle')
        self.moving=False
        self.update()
    def update(self):  
        if self.moving:
            if self.faceleft:
                self.x-=self.speed
            else:
                self.x+=self.speed
        if self.action=='Jump':
            if self.jumpcount<self.jumptop:
                self.y-=self.speed
            elif self.jumpcount>self.jumptop:
                if self.y<self.startingalt:
                    self.y+=self.speed
                elif self.moving:
                    self.change_action('Walk')
                else:
                    self.change_action('Idle')
            self.jumpcount+=1
        self.sprite.recttight[0]=self.x
        self.sprite.recttight[1]=self.y
        self.sprite.update(self.faceleft)
        self.width=self.sprite.recttight[2]
        self.height=self.sprite.recttight[3]
    def hit_right(self):
        self.x-=self.speed
        self.sprite.recttight[0]=self.x
        self.sprite.recttight[1]=self.y
        self.sprite.update(False)
    def hit_left(self):
        self.x+=self.speed
        self.sprite.recttight[0]=self.x
        self.sprite.recttight[1]=self.y
        self.sprite.update(True)



class Player(Character):
    def __init__(self):
        super().__init__()