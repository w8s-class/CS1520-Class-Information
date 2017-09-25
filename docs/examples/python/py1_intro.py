import random

r = random.randint(0, 100)
while r < 85:
	if r > 70:
		print(r, ":  so close!", sep="")
	elif r > 45:
		print(r, end="")
		print(":  Getting there...")
	else:
		print("{}:  Still so far away!".format(r))

	r = random.randint(0, 100)

print("OUT!")
