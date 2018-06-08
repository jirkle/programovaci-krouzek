#!/usr/bin/env python3

import random

class Animal:
	def __init__(self, species, name, salutation, sound, deathsound, strength, lifes, canfly, canswim, canthink):
		self.lifemax = lifes
		self.lifes = lifes
		self.strength = strength
		self.salutation = salutation
		self.species = species
		self.deathsound = deathsound
		self.name = name
		self.canfly = false
		self.canswim = false
		self.canthink = false

	def Rename(self, name):
		self.name = name

	def DescribeAnimal(self):
		if self.name == "":
			return "Unnamed %s %s (strength %d, lives %d (%d))" % (self.salutation, self.species, self.strength, self.lifes, self.lifemax)
		else:
			return "%s, the %s %s (strength %d, lives %d (%d))" % (self.name, self.salutation, self.species, self.strength, self.lifes, self.lifemax)
	def Die(self):
		print(self.deathsound)
		print("Unfortunately the %s is now dead." % (self.DescribeAnimal()))

	def __del__(self):
		self.Die()

	def Heal(self):
		if self.lifes < self.lifemax:
			tmp = self.lifes - self.lifemax
			maximum = max(tmp, 20)
			self.lifes = self.lifes + random.randint(5,20)
	
	def Defend(self, attacker):
		self.lifes = self.lifes - attacker.strength
		if self.lifes < 0:
			return None
		else:
			return self

	def __str__(self):
		if(self.name != ""):
			if(self.species != ""):
				return "This " + self.species.lower() + "'s name is "+self.name
			return "This animal's name is "+self.name
		else:
			if(self.species != ""):
				return "This " + self.species.lower() + " does not have a name"
			return "This animal does not have a name"

	def DoSound(self):
		print(self.sound)

	def Call(self):
		print(self.name + ", the " + self.species.lower() + "!")

	def AddTricks(self, *tricks):
		for trick in tricks:
			self.tricks.append(trick)

	def ListTricks(self):
		print(self.tricks)


class Pack:
	def __init__(self, name, *animals):
		self.name = name
		self.members = []
		for animal in animals:
			if isinstance(animal, Animal):
				self.members.append(animal)

	def AddMembers(self, *animals):
		for animal in animals:
			if isinstance(animal, Animal):
				self.members.append(animal)

	def ChooseMember(self, index):
		return self.member[index]

	def DeleteMember(self, index):
		self.members = [self.members[:index], self.members[index+1:]]

	def DeleteAllMembers(self):
		del self.members[:]

	def DescribePack(self):
		description = "This Pack is named %s and consists of these animals:\n" % (self.name)
		for index, member in enumerate(self.members):
			description = "%s[%d] %s\n" % (description, index, member.DescribeAnimal())
		return description				


class Dog(Animal):
	def __init__(self, name):
		salutation = random.choice(["Mighty", "Ferocious", "Agressive", "Sinister", "Vicious"])

		strength = random.randint(30,60)
		lifes = random.randint(50,100)

		Animal.__init__(self, "Dog", name, salutation, "Arf!", "ARRRRrrrf!", strength, lifes, false, false, false)
		self.tricks = []


class Cow(Animal):
	def __init__(self, name):
		salutation = random.choice(["Mighty", "Ferocious", "Agressive", "Sinister", "Vicious", "Unfeeded"])
		strength = 0
		lifes = 0
		if salutation == "Unfeeded":
			strength = random.randint(5,10)
			lifes = random.randint(30,40)
		else:
			strength = random.randint(20,30)
			lifes = random.randint(100,120)
		Animal.__init__(self, "Cow", name, salutation, "Moo!", "MooAAAAaaa!", strength, lifes, false, false, false)

class Duckling(Animal):
	def __init__(self, name):
		salutation = random.choice(["Little", "Tiny", "Cute"])
		strength = 0
		lifes = 0
		strength = random.randint(100, 200)
		lifes = random.randint(100, 200)
		Animal.__init__(self, "Duckling", name, salutation, "Quack!", "&*#X!!", strength, lifes, false, true, false)

class Crocodile(Animal):
	def __init__(self, name):
		salutation = random.choice(["Powerful", "Huge", "Bad", "Dangerous"])
		strength = 0
		lifes = 0
		strength = random.randint(50, 100)
		lifes = random.randint(100, 150)
		Animal.__init__(self, "Crocodile", name, salutation, "Roar!", "RRROOOOaar!", strength, lifes, false, true, false)

class Parrot(Animal):
	def __init__(self, name):
		salutation = random.choice(["Intelligent", "Tiny", "Cute"])
		strength = 0
		lifes = 0
		strength = random.randint(10, 50)
		lifes = random.randint(50, 100)
		Animal.__init__(self, "Parrot", name, salutation, "Tweet tweet!", "TWITER!", strength, lifes, true, false, true)

def GenRandomAnimal():
	AnimalType = random.choice(["Cow", "Dog", "Duckling", "Crocodile", "Parrot"])
	if AnimalType == "Cow":
		return Cow("")
	if AnimalType == "Dog":
		return Dog("")
	if AnimalType == "Duckling":
		return Duckling("")
	if AnimalType == "Crocodile":
		return Crocodile("")
	if AnimalType == "Parrot":
		return Parrot("")

def IntoDanger(pack):
	pass

def HealMembers(pack):
	pass

def EndGame(pack):
	pack.DeleteAllMembers()
	exit(0)
	pass


name = random.choice(["Strikeforce", "Humpty-Dumpty-Da", "Elaborate Animals", "Cheeky Chubbies", "The Forest Team", "X-Force Forest"])
pack = Pack(name)
for i in range(random.randint(2,5)):
	pack.AddMembers(GenRandomAnimal())
print(pack.DescribePack())
print("A pack of animals has gathered in order to avoid danger in the forest and defend themselves. Will this help them?")

scenes = {"name": "Spooky pond", "Description":""}

choice1 = {"description":"Follow the lead", "function":IntoDanger}
choice2 = {"description":"Heal everyone", "function":HealMembers}
end = {"description":"Mischievously murder everyone in your group", "function":EndGame}
choices = [choice1, choice2, end]


while len(pack.members) > 0:
	print("--------------------------------------------------------------")
	print("Your pack has been idle for a while, it is time for an action!")
	print("Choices are following:")
	for index, choice in enumerate(choices):
		print("[%d] %s" % (index, choice["description"]))
	try:
		x = int(input("What would you like to do? (enter choice number) >> "))
		choices[x]["function"](pack)

	except ValueError:
		print("You have not selected number. Selecting it for you randomly.")
		choice = random.choice(choices)
		print("And random choice is %s!" % (choice["description"]))
		choice["function"](pack)

	except IndexError:
		print("You have selected nonexistent option. If you can't count to %s I'll select it for you randomly." % (len(choices)))
		choice = random.choice(choices)
		print("And random choice is %s!" % (choice["description"]))
		choice["function"](pack)