from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()
player = FirstPersonController(collider="box")
ground = Entity(model="plane",collider="mesh",texture="grass",scale=(30,0,3))

p1 = Entity(model="plane",color=color.violet,scale=(0.4,0.1,53),z=28,x=0.7)
p2 = duplicate(p1, x=-3.7)
p3 = duplicate(p1, x=-0.6)
p4 = duplicate(p1, x=3.6)

blocks = []
for f in range(12):
	block = Entity(model="cube",color=color.white33,
position=(2,0.1,3+f*4),scale=(3,0.1,2.5))

block2 = duplicate(block, x=-2.2)
blocks.append( 
(block,block2,randint(0,3)>0, randint(0,3)>0) 
)

app.run()