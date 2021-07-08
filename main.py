import random
import numpy as np
from types import SimpleNamespace
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from utils import Spritesheet
# https://www.ursinaengine.org/
app = Ursina()

random_color = lambda: color.colors[random.choice(color.color_names)]

sp = Spritesheet('assets/spritesheet_tiles.png', sprite_count = (9, 10), sprite_size = (128, 128))
textures = SimpleNamespace()
textures.grass = Texture(Spritesheet.create(sp.size, top=sp[6, 1], under=sp[7, 5], other=sp[7, 4]))
textures.stone = Texture(Spritesheet.create(sp.size, other=sp[3, 4]))
textures.diamond = Texture(Spritesheet.create(sp.size, other=sp[2, 8]))
textures.wood = Texture(Spritesheet.create(sp.size, top=sp[0, 9], under=sp[0, 9], other=sp[1, 0]))
textures.stop = Texture(Spritesheet.create(sp.size, other=sp[5, 7]))

class Voxel(Entity):
	def __init__(self, position):
		super().__init__(model='cube', collider='box', texture=textures.grass, position=position)
		self.model.uvs = Spritesheet.uvs
		self.model.generate()
	
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
