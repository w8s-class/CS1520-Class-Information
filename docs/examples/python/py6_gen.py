# mimic the functionality of the builtin enumerate()
def enum(seq):
	n = 0
	for i in seq:
		yield n, i
		n += 1

print("enum fruit:")
for f in enum(["apple", "orange", "banana"]):
	print(f)

print("\nenum foo:")
for c in enum("foo"):
	print(c)

# a never ending generator!
def fibonacci():
	i = j = 1
	while True:
		r, i, j = i, j, i + j
		yield r

print("\nfib:")
for fib in fibonacci():
	print(fib)
	if fib > 100:
		break
