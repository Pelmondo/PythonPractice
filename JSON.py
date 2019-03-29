import json

numbers = [2,3,4,5,6,7]

fileName = "numbers.json"

with open(fileName, 'w') as f_obj:
	json.dump(numbers, f_obj)