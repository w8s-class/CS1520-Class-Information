def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print("result is", result)
	finally:
		print("executing finally clause")

divide(4, 2)
divide(4, 0)

try:
	raise Exception("foo", "bar")
except Exception as e:
	print(e)
	print(type(e))
	print(e.args)
