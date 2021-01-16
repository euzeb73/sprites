from app import App
from world import World
from character import Character
from sprite import Sprite
#player Lucky
stop=Sprite('Idle','png')
stop.animslowingfact=3
go=Sprite('Walk','png')
go.animslowingfact=2
jump=Sprite('Jump','png')
jump.animslowingfact=2
spritesdic=dict()
spritesdic['Idle']=stop
spritesdic['Walk']=go
spritesdic['Jump']=jump
Lucky=Character()
Lucky.add_sprites(spritesdic)
Lucky.jumptop=40
Lucky.speed=10

#Abigaelle
stop=Sprite('Idle','avgirl')
stop.animslowingfact=3
go=Sprite('Walk','avgirl')
go.animslowingfact=4
jump=Sprite('Jump','avgirl')
jump.animslowingfact=2
spritesdic=dict()
spritesdic['Idle']=stop
spritesdic['Walk']=go
spritesdic['Jump']=jump
Abigaelle=Character()
Abigaelle.add_sprites(spritesdic)
Abigaelle.faceleft=True
Abigaelle.x=900
# Abigaelle.y=400-(Abigaelle.sprite.rect[3]-Lucky.sprite.rect[3])
Abigaelle.y=390
Abigaelle.jumptop=20
Abigaelle.speed=13

monde=World(Lucky)
monde.characters.append(Abigaelle)

appli=App()
appli.add_world(monde)
appli.run()