l = [1, 2, 5]
l.append(3)

if 3 in l:
	print(3, "is in", l)

if 7 not in l:
	print("not in works, too")

print("l[1] is", l[1])

print("slicing works here, too:  l[2:] is ", l[2:])

print("\nlist comprehension:")
squares = [x**2 for x in range(10)]
print(squares)

crazy_list = ["a", 1, 1.0, "d"]

print("\ncrazy list 1:")
for item in crazy_list:
	print(item)

print("\ncrazy list 2:")
temp_iter = iter(crazy_list)
while True:
	try:
		item = temp_iter.__next__()
	except StopIteration:
		break

	print(item)
	
print("\ncrazy list 3:")
for i in range(len(crazy_list)):
	print(crazy_list[i])

d = {"Farnan":1520, "Garrison":8}
d["Ramirez"] = 1501
	
print("\ndict 1:")
for k in d:
	print(k, d[k])

print("\ndict 2:")
for k, v in d.items():
	print(k, v)

print("\ndict 3:")
for k in d.keys():
	print(k)

print("\ndict 4:")
for v in d.values():
	print(v)

print("\ndict values:")
print(d.values())
print(type(d.values()))
print(list(d.values()))

print("\ntuple test:")
t = ("Farnan", "CS1520")
t[0] = "Garrison"
