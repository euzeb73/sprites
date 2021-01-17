from app import App
from world import World
from character import Character
from sprite import Sprite

#Lucky
Lucky=Character()
Lucky.add_sprites('png')
Lucky.change_size(2)
Lucky.jumptop=1000
Lucky.speed=40

#Abigaelle
Abigaelle=Character()
Abigaelle.add_sprites('avgirl')
Abigaelle.change_size(2.5)
Abigaelle.faceleft=True
Abigaelle.x=900
# Abigaelle.y=400-(Abigaelle.sprite.rect[3]-Lucky.sprite.rect[3])
Abigaelle.y=390
Abigaelle.jumptop=40
Abigaelle.speed=90 

monde=World(Lucky)
monde.characters.append(Abigaelle)

appli=App()
appli.add_world(monde)
appli.run()