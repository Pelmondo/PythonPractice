class Car():
	""" Simple car """
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.gas = "benzin"

	def discription(self):
		print("This is " + self.make.title() + " model: " + self.model + " year is "
		+ str(self.year) )

my_car = Car('devyatca', "9", 2002)
my_car.discription()		

class ElecticCar(Car):
	def __init__ (self, make, model, year):
		super().__init__(make,model,year)
		self.battery = 70

my_tesla = ElecticCar('tesla', 's', 2016)
my_tesla.discription()	
print(my_tesla.battery)	