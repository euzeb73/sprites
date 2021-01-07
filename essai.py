from app import App
from world import World
from character import Character
from sprite import Sprite

stop=Sprite('Idle')
stop.animslowingfact=3
go=Sprite('Walk')
go.animslowingfact=2
jump=Sprite('Jump')
jump.animslowingfact=2
spritesdic=dict()
spritesdic['Idle']=stop
spritesdic['Walk']=go
spritesdic['Jump']=jump
perso=Character()
perso.add_sprites(spritesdic)
monde=World(perso)

appli=App()
appli.add_world(monde)
appli.run()