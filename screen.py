import pygame


class Font():
    def __init__(self, font=None, size=48):

        self.font = pygame.font.SysFont(font, size)  # initialise la police
        self.textdic = dict()  # Dictionnaire vide

    def addtext(self, text, txtname=None, color=(255, 0, 0)):
        '''fabrique une image(surface) associée à text prete à coller'''
        if txtname == None:
            self.textdic[text] = self.font.render(text, True, color)
        else:
            self.textdic[txtname] = self.font.render(text, True, color)



class Screen():
    def __init__(self,width,height):
        self.width=width
        self.height =height
        self.fullscreen=False
        self.window=pygame.display.set_mode(
            (self.width, self.height))
        self.fontsmall = Font('segoescript', 16)  # initialise la police petite
    def switch_full(self):
        if self.fullscreen:
            flag=0
        else:
            flag=pygame.FULLSCREEN
        self.fullscreen=not(self.fullscreen)
        self.window=pygame.display.set_mode(
            (self.width, self.height),flag)
    
    def affiche_life(self,player):
        life=player.life
        self.fontsmall.addtext('Life: {}'.format(
            life), 'Life', (0, 200, 255))
        window=self.window.get_rect()
        surface = self.fontsmall.textdic['Life']
        w, h = surface.get_size()
        self.window.blit(surface, (window.left+w, window.top+2*h))

    def affiche(self,world):
        #Fond
        self.window.fill(world.bgcolor)
        #Sol
        pygame.draw.line(self.window,(100,100,50),(0,world.ground),(self.width,world.ground),4)
        #Sprites
        group_to_draw=pygame.sprite.Group()
        for movbod in world.movbods:
            group_to_draw.add(movbod.sprite)
        group_to_draw.draw(self.window)
        self.affiche_life(world.player)
        #LEs rectangles pour suivre ce qu'il se passse
        # for movbod in world.movbods:
        #     gdrec=movbod.sprite.rect
        #     ptrec=movbod.sprite.recttight
        #     pygame.draw.rect(self.window,(255,0,0),gdrec,1)
        #     pygame.draw.rect(self.window,(0,0,255),ptrec,1)
        pygame.display.update()