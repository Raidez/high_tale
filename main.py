import random
from ursina import *

app = Ursina()

################################################################################

a_lot_of_cubes = list()
for x in range(16 * 16):
	random_color = color.colors[random.choice(color.color_names)]
	random_position = (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))

	a_lot_of_cubes.append(Entity(model='cube', texture='white_cube', color=random_color, position=random_position))

def update():
	pass

################################################################################

app.run()
