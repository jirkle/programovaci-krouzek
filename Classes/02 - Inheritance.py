#!/usr/bin/env python3

class Animal:
	def __init__(self, species,  name, sound):
		self.species = species
		self.sound = sound
		self.name = name


class Dog(Animal):
	def __init__(self, name):
		Animal.__init__(self, "Dog", name, "Bark!")
		self.tricks = []

	def AddTricks(self, *tricks):
		for trick in tricks:
			self.tricks.append(trick)

	def ListTricks(self):
		print(self.tricks)


	def Bark(self):
		print(self.sound)

	def Call(self):
		print(self.name+"!")

	def __str__(self):
		return "This dog's name is "+self.name

	tricks = []


names = ["Henry", "Jack", "Rocky", "Lucy", "Daisy"]

cage = []
for name in names:
	cage.append(Dog(name))

cage[3].sound = "ARF!"
cage[1].sound = "Arf!"

for dog in cage:
	print(dog)
	dog.Call()
	dog.Bark()


print("Let's learn Rocky and Jack few tricks!")
Rocky = cage[2]
Rocky.AddTricks("Aport", "Sit down", "Lie down")
Jack = cage[1]
Jack.AddTricks("Sit down")

print("Rocky can now do these tricks")
Rocky.ListTricks()
print("Jack can now do these tricks")
Jack.ListTricks()
