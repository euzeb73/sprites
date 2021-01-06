import pygame
class Character():
    def __init__(self):
        self.x=0 #position en pixels du coin sup gauche
        self.y=0
        self.sprites=dict() #dictionnaire de sprites contenant les actions possibles
        self.actions=self.sprites.keys
        self.action='IdleR'
        self.goingleft=False
        self.goingright=False
        self.speed=5
        self.width=10
        self.height=10
    def add_sprites(self,spritesdic):
        #à automatiser en fonction d'une liste d'action plus tard)
        self.sprites=spritesdic
        self.sprite=spritesdic[self.action]
    def change_action(self,action):
        self.action=action
        self.sprite=self.sprites[self.action]
        self.sprite.index=0
    def go_left(self):
        if self.action!='WalkL':
            self.change_action('WalkL')
        self.goingleft=True
        self.update()
    def go_rigth(self):
        if self.action!='WalkR':
            self.change_action('WalkR')
        self.goingright=True
        self.update()
    def stop(self):
        if self.goingleft:
            self.change_action('IdleL')
        else:
            self.change_action('IdleR')
        self.goingleft=False
        self.goingright=False
        self.update()
    def update(self):
        self.width=self.sprite.image.get_width()
        self.height=self.sprite.image.get_height()
        if self.goingleft:
            self.x-=self.speed
        if self.goingright:
            self.x+=self.speed
        self.sprite.rect[0]=self.x
        self.sprite.rect[1]=self.y
        self.sprite.update()
    def hit_right(self):
        self.x-=self.speed
        self.sprite.rect[0]=self.x
        self.sprite.rect[1]=self.y
        self.sprite.update()
    def hit_left(self):
        self.x+=self.speed
        self.sprite.rect[0]=self.x
        self.sprite.rect[1]=self.y
        self.sprite.update()



class Player(Character):
    def __init__(self):
        super().__init__()