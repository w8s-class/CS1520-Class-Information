outf = open("example.txt", "w")
for i in range(10):
	outf.write(str(i) + "\n")
outf.close()

inf = open("example.txt")
for line in inf:
	print(line.strip())
inf.close()

print()

with open("example.txt") as inf:
	for line in inf:
		print(line.strip())

print()
		
from contextlib import contextmanager

@contextmanager
def tag(name):
	print("<{}>".format(name))
	yield
	print("</{}>".format(name))

with tag("h1"):
	print("foo")
