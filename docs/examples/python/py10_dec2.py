from functools import wraps

def off_by_one(original_function):
	def new_function(x, y):
		return original_function(x, y) + 1
	return new_function

@off_by_one
def add(x, y):
	""" THIS IS MY TEST DOCSTRING """
	return x + y

print(add(2, 2))
print(add.__name__)
print(add.__doc__)

def off_by_one_W(original_function):
	@wraps(original_function)
	def new_function(x, y):
		return original_function(x, y) + 1
	return new_function

@off_by_one_W
def add_W(x, y):
	""" THIS IS MY TEST DOCSTRING """
	return x + y

print(add_W(2, 2))
print(add_W.__name__)
print(add_W.__doc__)
