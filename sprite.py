import pygame
import glob

class Sprite(pygame.sprite.Sprite):
    def __init__(self,action):
        super().__init__()
        self.action = action
        self.images = []
        self.index=-1
        self.animslowingfact=1
        self.reducratio=5 #par rapport au fichier d'origine facteur pour diminuer la taille du sprite
        self.load_images()
        self.update(False)
        
 
    def load_images(self):
        list_imgs = glob.glob("dino/{}*.png".format(self.action)) #liste des fichiers image
        temp_imgs=[]
        for img in list_imgs:
            #On charge et réduit l'image
            image=pygame.image.load(img)
            width=image.get_width()
            height=image.get_height()
            image=pygame.transform.smoothscale(image,(width//self.reducratio,height//self.reducratio))
            #On stocke les images dans une liste
            if len(img) == len(list_imgs[0]): #de 0 à 9
                self.images.append(image)
            else: #de 10 à plus mais moins de 100...
                temp_imgs.append(image)
        self.images+=temp_imgs
        self.index = 0
        self.rect=self.images[0].get_bounding_rect()
 
    def update(self,faceleft):
        imagenum=self.index//self.animslowingfact
        if imagenum == len(self.images)-1:
            self.index = 0
        else:
            self.index += 1
        if faceleft:
            self.image = pygame.transform.flip(self.images[self.index//self.animslowingfact],True,False)
        else:
            self.image = self.images[self.index//self.animslowingfact]
