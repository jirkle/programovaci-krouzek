#!/usr/bin/env python3

import random

class Animal:
	def __init__(self, species, name, salutation, sound, deathsound, strength, lifes, canfly, canswim, canthink):
		self.lifemax = lifes
		self.lifes = lifes
		self.strength = strength
		self.salutation = salutation
		self.species = species
		self.sound = sound
		self.deathsound = deathsound
		self.name = name
		self.canfly = canfly
		self.canswim = canswim
		self.canthink = canthink

	def GetName(self):
		if self.name == "":
			return "Unnamed %s %s" % (self.salutation, self.species)
		else:
			return "%s, the %s %s" % (self.name, self.salutation)

	def Rename(self, name):
		self.name = name

	def DescribeAnimal(self):
		if self.name == "":
			return "Unnamed %s %s (strength %d, lives %d (%d))" % (self.salutation, self.species, self.strength, self.lifes, self.lifemax)
		else:
			return "%s, the %s %s (strength %d, lives %d (%d))" % (self.name, self.salutation, self.species, self.strength, self.lifes, self.lifemax)
	def Die(self):
		global score
		score = score + 1 
		print(self.deathsound)
		print("Unfortunately the %s is now dead." % (self.DescribeAnimal()))

	def __del__(self):
		self.Die()

	def Heal(self):
		if self.lifes < self.lifemax:
			tmp = self.lifes - self.lifemax
			maximum = max(tmp, 20)
			self.lifes = self.lifes + random.randint(5,20)

	def TakeDamage(self, damage):
		self.lifes = self.lifes - damage
		if self.lifes < 0:
			return None
		else:
			return self
		

	def Defend(self, attacker):
		return self.TakeDamage(attacker.strength)

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
	def HealMembers(self):
		for animal in self.members:
			animal.Heal()

	def ChooseMember(self, index):
		return self.members[index]

	def DeleteMember(self, index):
		del self.members[index]

	def DeleteAllMembers(self):
		del self.members[:]

	def DescribePack(self):
		description = "This Pack is named %s and consists of these animals:\n" % (self.name)
		for index, member in enumerate(self.members):
			description = "%s[%d] %s\n" % (description, index, member.DescribeAnimal())
		return description				


class Dog(Animal):
	def __init__(self, name):
		salutation = random.choice(["Mighty", "Ferocious", "Agressive", "Sinister", "Vicious", "Agressive puppy", "Skinny little something"])
		strength = 0
		lifes = 0
		if salutation == "Agressive puppy":
			strength = random.randint(40,50)
			lifes = random.randint(20,30)
		elif salutation == "Skinny little something":
			strength = random.randint(20,30)
			lifes = random.randint(100,120)

		else:
			strength = random.randint(30,60)
			lifes = random.randint(50,100)

		Animal.__init__(self, "Dog", name, salutation, "Arf!", "ARRRRrrrf!", strength, lifes, False, False, False)
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
		Animal.__init__(self, "Cow", name, salutation, "Moo!", "MooAAAAaaa!", strength, lifes, False, False, False)

class Duckling(Animal):
	def __init__(self, name):
		salutation = random.choice(["Little", "Tiny", "Cute"])
		strength = 0
		lifes = 0
		strength = random.randint(100, 200)
		lifes = random.randint(100, 200)
		Animal.__init__(self, "Duckling", name, salutation, "Quack!", "&*#X!!", strength, lifes, False, True, False)

class Crocodile(Animal):
	def __init__(self, name):
		salutation = random.choice(["Powerful", "Huge", "Bad", "Dangerous"])
		strength = 0
		lifes = 0
		strength = random.randint(50, 100)
		lifes = random.randint(100, 150)
		Animal.__init__(self, "Crocodile", name, salutation, "Roar!", "RRROOOOaar!", strength, lifes, False, True, False)

class Parrot(Animal):
	def __init__(self, name):
		salutation = random.choice(["Intelligent", "Tiny", "Cute"])
		strength = 0
		lifes = 0
		strength = random.randint(10, 50)
		lifes = random.randint(50, 100)
		Animal.__init__(self, "Parrot", name, salutation, "Tweet tweet!", "TWITER!", strength, lifes, True, False, True)

class Batman(Animal):
	def __init__(self, name):
		salutation = random.choice(["killer", "retarded"])
		strength = 0
		lifes = 0
		if salutation == "killer":
			strength = random.randint(1110,1120)
			lifes = random.randint(210,220)
		else:
			strength = random.randint(2,3)
			lifes = random.randint(10,12)
		Animal.__init__(self, "Batman", name, salutation, "Joker, don't try anything!", "Dark knight will RISE AGAIN!!", strength, lifes, False, False, False)

class Sheep(Animal):
	def __init__(self, name):
		salutation = random.choice(["undercut",])
		strength = 0
		lifes = 0
		if salutation == "undercut":
			strength = random.randint(37,54)
			lifes = random.randint(50,100)
		
		Animal.__init__(self, "Sheep", name, salutation, "Will you cut sheep?", "Will you cut sheep?", strength, lifes, False, False, False)




####################
# Helper functions #
####################

def duel(first, second):
	if random.randint(0,9) < 5:
		print("%s attacks!" % (first.DescribeAnimal()))
		second = second.Defend(first)
		if second == None:
			return (first, second)

	while (first != None and second != None):
		print("%s attacks!" % (second.DescribeAnimal()))
		first = first.Defend(second)
		if first == None:
			break
		print("%s attacks!" % (first.DescribeAnimal()))
		second = second.Defend(first)
	return (first, second)


def Combat(defender, attacker):
	print("Combat begins!")
	if isinstance(attacker, Animal):
		try:
			while (len(defender.members) > 0 and attacker != None):
				print(len(defender.members))
				print("You are facing %s"% (attacker.DescribeAnimal()))
				print("You have following options:")
				print(pack.DescribePack())
				x = GetNumber("who will fight now? >> ", len(defender.members))
				duelist = pack.ChooseMember(x)
				print(duelist.DescribeAnimal())
				duelant, duelist = duel(duelist, attacker)
				if duelant == None:
					pack.DeleteMember(x)
				else:
					del attacker
			if attacker:
				print("woho!")
			print("Everyone has died.")
		except NameError:
			print("You have won the fight!")
			print(pack.DescribePack())
#	elif isinstance(attacker, Pack):
#		while 

			
def GetNumber(desc, length):
	x = 0
	try:
		x = int(input(desc))

		if x < length:
			pass
		else:
			print("You have selected nonexistent option. If you can't count to %s I'll select it for you randomly." % (length-1))
			x = random.randint(0,length-1)
	except ValueError:
		print("You have not selected number. Selecting it for you randomly.")
		x =random.randint(0,length-1)
	return x
	

def GenRandomAnimal():
	return random.choice([Cow, Dog, Duckling, Crocodile, Parrot, Batman, Sheep])("")

def IntoDanger(pack):
	pass

def ClimbTheTree(pack):
	print("--------------------------------------------------------------")
	print("Animals decided to send one scout to climb the tree")
	print("The choice is following:")
	print(pack.DescribePack())
	x = GetNumber("Who will climb the tree? >> ", len(pack.members))
	tmp = random.randint(0,29)
	victim = pack.ChooseMember(x)
	print(tmp)
	if tmp < 10:
		print("%s climbed the tree but unfortunately an unstable branch collapsed and it fell off" % (victim.GetName()))
		damage = random.randint(10,40)
		if damage > 30:
			print("And it was spectacularly bad impact!")
		print("%s took %d damage" % (victim.GetName(), damage))
		victim.TakeDamage(damage)
	elif tmp < 20:
		newMember = GenRandomAnimal()
		print("%s successfully climbed the tree and found very scared %s" % (victim.GetName(), newMember.DescribeAnimal()))
		print("What it was doing there remains unknown...")
		pack.AddMembers(newMember)
	elif tmp < 30:
		print("%s successfully climbed the tree and looked over the forest for an adventure, but found nothing." % (victim.GetName()))
		
		

def ShowInfo(pack):
	print("--------------------------------------------------------------")
	print(pack.DescribePack())

def HealMembers(pack):
	print("--------------------------------------------------------------")
	print("All the animals gathered and helped each other to heal their terrible wounds.")
	pack.HealMembers()
	print(pack.DescribePack())

def DucklingOnPond(pack):
	print("--------------------------------------------------------------")
	print("The duckling happily flown... until an enormously giant crocodile ate it! And now it's up to you!")
	Combat(pack,Crocodile("The gharial"))

def Wander(pack):
	pass

def PrintScore():
	global score
	print("--------------------------------------------------------------")
	print("You may not have saved all the animals, but you murdered %d of them!" % (score))
	print("                      You murderous bastard!                        ")
	print("--------------------------------------------------------------")


def EndGame(pack):
	pack.DeleteAllMembers()
	PrintScore()
	exit(0)

def NewOne (pack):
	print("--------------------------------------------------------------")
	print("There is a lot of animals playing dead, someone from your pack could fetch them but might pay his life for this.")
	print(pack.DescribePack())
	x = GetNumber("who will be sacficed ? >> ", len(pack.members))
	victim = pack.ChooseMember(x)
	tmp = random.randint(0,29)
	if tmp < 10:
		pack.DeleteMember(x)
		print("%s has been unsuccessful. The wolves saw him and immediately killed him." % (victim.GetName()))
	elif tmp < 20:
		pack.DeleteMember(x)
		animal = GenRandomAnimal()
		print("%s has been unsuccessful. The wolves saw him at last but it was able to bring %s and immediately killed him." % (victim.GetName(), animal.DescribeAnimal()))
		pack.AddMembers(animal)
	else:
		animal = GenRandomAnimal()
		print("%s has been successful. The wolves haven't seen it and it was able to bring %s!" % (victim.GetName(), animal.DescribeAnimal()))
		pack.AddMembers(animal)
def MakingNewFriends (pack):
	print("--------------------------------------------------------------")
	print("You see a lovely tavern, and you can hear a noisy music. Will you go there?")
	print(pack.DescribePack())
	x = GetNumber("Which animal will come into tavern? >> ", len(pack.members))
	victim =  pack.ChooseMember(x)
	tmp = random.randint(0,29)
	if tmp < 15:
		pack.DeleteMember(x)
		print("Unfortunately the %s was secret drinker... and he drank so much alcohol that... he fell down into the barrel with wine and drowned himself." % (victim.GetName()))
	elif tmp < 20:
		pack.DeleteMember(x)
		animal = GenRandomAnimal()
		print("What a betrayal! %s found a new group and your animals decided to murder him instead" % (victim.GetName()))
		pack.AddMembers(animal)
	else:
		animal = GenRandomAnimal()
		print("%s has been successful. You have new friend %s!" % (victim.GetName(), animal.DescribeAnimal()))
		pack.AddMembers(animal)
	
##############
# Main plots #
##############

score = 0

# Common
heal = {"description":"Try to heal everyone in group", "function":HealMembers}
end = {"description":"Mischievously murder everyone in your group", "function":EndGame}
info = {"description":"Show how incredibly good (or bad) everyone is", "function":ShowInfo}
wander = {"description":"Do not waste time with this and wander further", "function":Wander}

#specific
duckling = {"description":"Put the duckling into the pond", "function":DucklingOnPond}
followTrail = {"description":"Follow the lead", "function":IntoDanger}
climbTree = {"description":"Climb the tree", "function":ClimbTheTree}
enterDen = {"description":"Hire a new animal but maybe sacrifice one of your pack", "function":NewOne}
enterTavern = {"description":"You may go to tavern and make some new friends", "function":MakingNewFriends}

pond = {"name": "Spooky pond", "description":"A pond with a lot of meanders, seems calm but it might be a trap! There is a brightly yellow duckling nerby.", "choices":[duckling, heal, info, wander, end]}
tree = {"name": "Big scary tree", "description":"A tree rising above all other trees with much wider treetop, it must be spectacular view up there!", "choices":[climbTree, heal, info, wander, end]}
cave = {"name": "A silent cave", "description":"A scary looking cave with strange loud noises. UARRrrgh! There is a trail behind the cave", "choices":[followTrail, heal, info, wander, end]}
den = {"name": "Wolf's den", "description":"Well known den full of wide range of animals and other stuff. Some of them still alive.", "choices":[enterDen, heal, info, wander, end]}
tavern = {"name": "Tavern at a happy animal", "description":"Famous local tavern with nice service, good food and unbeatable beverages where everyone gathers", "choices":[enterTavern, heal, info, wander, end]}

scenes = [pond, tree, cave, den, tavern]

########
# Init #
########

name = random.choice(["Strikeforce", "Humpty-Dumpty-Da", "Elaborate Animals", "Cheeky Chubbies", "The Forest Team", "X-Force Forest"])
pack = Pack(name)
for i in range(random.randint(2,5)):
	pack.AddMembers(GenRandomAnimal())
print(pack.DescribePack())
print("A pack of animals has gathered in order to avoid danger in the forest and defend themselves. Will this help them?")

#############
# Main loop #
#############

while len(pack.members) > 0:
	scene = random.choice(scenes)
	print("--------------------------------------------------------------")
	print("Your pack has been idle for a while, so it decided it is time for an action!")
	print("After a little bit of roaming through the forest a pack arrived to %s" % scene["name"])
	print(scene["description"])

	print("Choices are following:")
	for index, choice in enumerate(scene["choices"]):
		print("[%d] %s" % (index, choice["description"]))

	x = GetNumber("What would you like to do? (enter choice number) >> ", len(scene["choices"]))
	scene["choices"][x]["function"](pack)

PrintScore()

