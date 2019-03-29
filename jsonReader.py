import json

fileName = "numbers.json"

with open(fileName) as f_obj:
	numbers = json.load(f_obj)
print(numbers)

