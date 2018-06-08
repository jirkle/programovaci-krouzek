#!/usr/bin/env python3

class Dog:
	sound = "Bark!"
	tricks = []

	def Bark(self):
		print(self.sound)
	def AddTrick(self, name):
		self.tricks.append(name)
	def ListTricks(self):
		print(self.tricks)

Jack = Dog()
Rocky = Dog()

Rocky.sound = "Arf!"

Jack.Bark()
Rocky.Bark()


Rocky.AddTrick("Aport")
Jack.AddTrick("Sit down")

Rocky.ListTricks()
