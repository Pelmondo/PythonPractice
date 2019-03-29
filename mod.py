def make_coffe(size = 100, *topings):
	""" Make coffe, were size = 100ml and topings as some adds"""
	print("\nMaking coffe as " + str(size) + " with toppings:")
	for topping in topings:
		print("- " + topping)


def countdown(i):
	"""" Обратный отсчет """
	print(i)
	if i <= 0:
		return
	else:
		countdown(i-1)
			


