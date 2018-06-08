#!/usr/bin/env python3

import random
from animals import *

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
			description += "[%d] %s\n" % (index, member.DescribeAnimal())
		return description

####################
# Helper functions #
####################

def showInfo(pack):
	print("--------------------------------------------------------------")
	print(pack.DescribePack())


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


def combat(defender, attacker):
	print("COMBAT begins!")
	if isinstance(attacker, Animal):
		try:
			while (len(defender.members) > 0 or attacker != None):
				print("You are facing %s"% (attacker.DescribeAnimal()))
				print("You have following options:")
				print(defender.DescribePack())
				x = getNumber("who will fight now? >> ", len(defender.members))
				duelist = defender.ChooseMember(x)
				print(duelist.DescribeAnimal())
				duelant, duelist = duel(duelist, attacker)
				if duelant == None:
					defender.DeleteMember(x)
				else:
					del attacker
			if attacker:
				print("woho!")
			print("Everyone has died.")
		except NameError:
			print("You have won the fight!")
			print(defender.DescribePack())
	elif isinstance(attacker, Pack):
		pass

			
def getNumber(desc, length):
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