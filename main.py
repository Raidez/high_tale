import random
import numpy as np
from ursina import *

app = Ursina()

################################################################################

camera.position = (7.5, 15, -20)
camera.rotation = (30, 0, 0)

world = np.ones((16, 16), dtype=int)
for (x, z), value in np.ndenumerate(world):
	random_color = color.colors[random.choice(color.color_names)]
	Entity(model='cube', collider='box', texture='white_cube', color=random_color, position=(x, 0, z))

def update():
	pass

################################################################################

app.run()
