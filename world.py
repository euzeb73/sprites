import pygame
class World():
    def __init__(self,player):
        self.player=player
        self.characters=[self.player]
        self.player.x=0
        self.player.y=400
        self.bgcolor=(200,0,100)
    def update(self,screen):
        for character in self.characters:
            character.update()
            if character.x+character.width > screen.width:
                character.hit_right()
            if character.x < 0:
                character.hit_left()