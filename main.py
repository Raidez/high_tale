import random
import numpy as np
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from utils import Spritesheet
# https://www.ursinaengine.org/
app = Ursina()

random_color = lambda: color.colors[random.choice(color.color_names)]

t = Entity(model='cube', collider='box', texture='assets/furnace')
t.model.uvs = [
		(1., .5), (.75, 0.), (1., 0.), # under
		(.5, 1.), (.25, .5), (.5, .5), # top
		(1., .5), (.75, 0.), (1., 0.), # right
		(.5, .5), (.25, 0.), (.5, 0.), # front
		(.25, .5), (0., 0.), (.25, 0.), # left
		(0, 0), (0, 0), (0, 0), # back
		(1., .5), (.75, .5), (1., 0.), # under
		(.5, 1.), (.5, .5), (.25, 1.), # top
		(1., .5), (.75, .5), (.75, 0.), # right
		(.5, .5), (.25, .5), (.25, 0.), # front
		(.25, .5), (0., .5), (0., 0.), # left
		(0, 0), (0, 0), (0, 0) # back
]
t.model.generate()

def update():
	if held_keys['z']:
		camera.position += (0, 0, time.dt)
	if held_keys['q']:
		camera.position -= (time.dt, 0, 0)
	if held_keys['s']:
		camera.position -= (0, 0, time.dt)
	if held_keys['d']:
		camera.position += (time.dt, 0, 0)
	if held_keys['space']:
		camera.position += (0, time.dt, 0)
	if held_keys['control']:
		camera.position -= (0, time.dt, 0)

# https://gitpod.io
# https://github.com/pokepetter/ursina/issues/44
# spritesheet = Spritesheet('assets/spritesheet_tiles.png', sprite_count = (9, 10), sprite_size = (128, 128))
'''
class Voxel(Entity):
	def __init__(self, position):
		super().__init__(model='cube', collider='box', texture='white_cube', position=position)
	
	def input(self, key):
		if not self.hovered:
			return
		
		distance_from_player = distance(player.position, self.position + mouse.normal)
		if key == 'left mouse up' and distance_from_player < 3:
			destroy(self) ## supprime le bloc
		elif key == 'right mouse up' and distance_from_player < 4:
			Voxel(position=self.position + mouse.normal) ## créer un nouveau bloc

################################################################################

player = FirstPersonController(position=(5, 10, 5))

# génération du monde
world = np.ones((16, 16), dtype=int)
chunk = list()
for (x, z), value in np.ndenumerate(world):
	chunk.append(Voxel((x, 0, z)))
'''
################################################################################

app.run()
