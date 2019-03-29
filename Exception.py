# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("you can't do this")

fileName = 'Text/alice.txt'

with open(fileName) as f_obj:
	contents = f_obj.read()
print(contents)	

words = contents.split()
num_words = len(words)
print(num_words)