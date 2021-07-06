import random
import numpy as np
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

random_color = lambda: color.colors[random.choice(color.color_names)]

class Voxel(Entity):
	def __init__(self, position):
		super().__init__(model='cube', collider='box', texture='white_cube', color=random_color(), position=position)
	
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

################################################################################

app.run()
