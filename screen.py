import pygame

class Screen():
    def __init__(self,width,height):
        self.width=width
        self.height =height
        self.fullscreen=False
        self.window=pygame.display.set_mode(
            (self.width, self.height))
    def switch_full(self):
        if self.fullscreen:
            flag=0
        else:
            flag=pygame.FULLSCREEN
        self.fullscreen=not(self.fullscreen)
        self.window=pygame.display.set_mode(
            (self.width, self.height),flag)
    def affiche(self,world):
        self.window.fill(world.bgcolor)
        group_to_draw=pygame.sprite.Group()
        for character in world.characters:
            group_to_draw.add(character.sprite)
        group_to_draw.draw(self.window)
        pygame.display.update()