from app import App
from world import World
from character import Character
from sprite import Sprite

stopL=Sprite('IdleL')
stopL.animslowingfact=3
stopR=Sprite('IdleR')
stopR.animslowingfact=3
goL=Sprite('WalkL')
goL.animslowingfact=2
goR=Sprite('WalkR')
goR.animslowingfact=2
spritesdic=dict()
spritesdic['IdleL']=stopL
spritesdic['IdleR']=stopR
spritesdic['WalkL']=goL
spritesdic['WalkR']=goR
perso=Character()
perso.add_sprites(spritesdic)
monde=World(perso)

appli=App()
appli.add_world(monde)
appli.run()