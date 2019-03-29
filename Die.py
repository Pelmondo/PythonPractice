from random import randint


class Die():

	def __init__(self,sides = 6):
		self.sides = sides

	def roll_die(self):
		x = randint(1, self.sides)
		return x

cube_with_six = Die(6)
# print(cube_with_six.roll_die())
cube_with_twelw = Die(20)
# print(cube_with_twelw.roll_die())	
for i in range(1,10):
 	print(cube_with_twelw.roll_die())
 	print(cube_with_six.roll_die())