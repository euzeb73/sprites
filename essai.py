from app import App
from world import World
from character import Character
from sprite import Sprite

#Lucky
Lucky=Character()
Lucky.add_sprites('spirit')
Lucky.change_size(1.5)
Lucky.jumptop=150        
Lucky.speed=15

#Abigaelle
Abigaelle=Character()
Abigaelle.add_sprites('gdton')
Abigaelle.change_size(1.5)
Abigaelle.change_animspeed(10,['Jump'])
Abigaelle.faceleft=True
Abigaelle.x=900
# Abigaelle.y=400-(Abigaelle.sprite.rect[3]-Lucky.sprite.rect[3])
Abigaelle.y=390
Abigaelle.jumptop=8
Abigaelle.speed=30

monde=World(Lucky)
monde.characters.append(Abigaelle)

appli=App()
appli.add_world(monde)
appli.run()