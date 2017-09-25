class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def display(self):
		print("Name:", self.name)
		print("Age:", self.age)
		print()

class Student(Person):
	def __init__(self, name, age):
		super().__init__(name, age)

		self.classes = []

	def add_class(self, new):
		self.classes.append(new)

	def display(self):
		super().display()
		print("Classes:", self.classes)
		print()

def display_person(p):
	p.display()

alice = Person("Alice", 25)

display_person(alice)
	
bob = Student("Bob", 20)
display_person(bob)

bob.add_class("CS1520")
display_person(bob)

