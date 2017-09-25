def off_by_one(original_function):
	def new_function(x, y):
		return original_function(x, y) + 1
	return new_function

@off_by_one
def add(x, y):
	return x + y

print(add(2, 2))
