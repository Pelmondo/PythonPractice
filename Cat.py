class Cat():
	""" Simple cat """

	def __init__(self, name, age):
		""" Инициализирует атрибуты """
		self.name = name
		self.age = age

	def meow(self):
		""" The cat say: MEOW """
		print(self.name.title() + " - MEOW")
	def birthday(self):
		""" The cat be older """
		self.age += 1
		print("Happy Birthday! " + self.name.title())


my_cat = Cat("Stipa", 10)
my_cat.birthday()
print(my_cat.age)	
your_cat = Cat("Hui", 11)
my_cat.meow()
your_cat.meow()		