def foo(*args, **kwargs):
	print(args)
	print(kwargs)
	print()

foo(1, 2, 3, one=1, two=2, three=3)

def bar(a, b, c):
	print(a)
	print(b)
	print(c)
	print()

l = [1, 2, 3]
bar(*l)

d = {"b":2, "a":1, "c":3}
bar(**d)
