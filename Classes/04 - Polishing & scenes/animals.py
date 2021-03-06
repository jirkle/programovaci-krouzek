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
            return "%s, the %s %s" % (self.name, self.salutation, self.species)

    def Rename(self, name):
        self.name = name

    def DescribeAnimal(self):
        if self.name == "":
            return "Unnamed %s %s (strength %d, lives %d (%d))" % (
            self.salutation, self.species, self.strength, self.lifes, self.lifemax)
        else:
            return "%s, the %s %s (strength %d, lives %d (%d))" % (
            self.name, self.salutation, self.species, self.strength, self.lifes, self.lifemax)

    def Die(self):
        print(self.deathsound)
        print("%s is now dead." % (self.DescribeAnimal()))

    def __del__(self):
        self.Die()

    def Heal(self):
        if self.lifes < self.lifemax:
            tmp = self.lifes - self.lifemax
            maximum = max(tmp, 20)
            self.lifes = self.lifes + random.randint(5, 20)

    def TakeDamage(self, damage):
        self.lifes = self.lifes - damage
        if self.lifes < 0:
            return None
        else:
            return self

    def Defend(self, attacker):
        return self.TakeDamage(attacker.strength)

    def __str__(self):
        if (self.name != ""):
            if (self.species != ""):
                return "This " + self.species.lower() + "'s name is " + self.name
            return "This animal's name is " + self.name
        else:
            if (self.species != ""):
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


class Dog(Animal):
    def __init__(self, name):
        salutation = random.choice(
            ["Mighty", "Ferocious", "Agressive", "Sinister", "Vicious", "Agressive puppy", "Skinny little something"])
        strength = 0
        lifes = 0
        if salutation == "Agressive puppy":
            strength = random.randint(40, 50)
            lifes = random.randint(20, 30)
        elif salutation == "Skinny little something":
            strength = random.randint(20, 30)
            lifes = random.randint(100, 120)

        else:
            strength = random.randint(30, 60)
            lifes = random.randint(50, 100)

        Animal.__init__(self, "Dog", name, salutation, "Arf!", "ARRRRrrrf!", strength, lifes, False, False, False)
        self.tricks = []


class Cow(Animal):
    def __init__(self, name):
        salutation = random.choice(["Mighty", "Ferocious", "Agressive", "Sinister", "Vicious", "Unfeeded"])
        strength = 0
        lifes = 0
        if salutation == "Unfeeded":
            strength = random.randint(5, 10)
            lifes = random.randint(30, 40)
        else:
            strength = random.randint(20, 30)
            lifes = random.randint(100, 120)
        Animal.__init__(self, "Cow", name, salutation, "Moo!", "MooAAAAaaa!", strength, lifes, False, False, False)


class Duckling(Animal):
    def __init__(self, name):
        salutation = random.choice(["Little", "Tiny", "Cute"])
        strength = random.randint(100, 200)
        lifes = random.randint(100, 200)
        Animal.__init__(self, "Duckling", name, salutation, "Quack!", "&*#X!!", strength, lifes, False, True, False)


class Crocodile(Animal):
    def __init__(self, name):
        salutation = random.choice(["Powerful", "Huge", "Bad", "Dangerous"])
        strength = random.randint(50, 100)
        lifes = random.randint(100, 150)
        Animal.__init__(self, "Crocodile", name, salutation, "Roar!", "RRROOOOaar!", strength, lifes, False, True,
                        False)


class Parrot(Animal):
    def __init__(self, name):
        salutation = random.choice(["Intelligent", "Tiny", "Cute"])
        strength = random.randint(10, 50)
        lifes = random.randint(50, 100)
        Animal.__init__(self, "Parrot", name, salutation, "Tweet tweet!", "TWITER!", strength, lifes, True, False, True)

class Ogre(Animal):
    def __init__(self, name):
        salutation = random.choice(["Bad", "Scared", "Stupid"])
        strenght = 0
        lifes = 0
        canThink = True
        if salutation == "Stupid":
            canThink = False
            lifes = random.randint(120, 190)
            strenght = random.randint(25, 50)
        if salutation == "Bad":
            lifes = random.randint(50, 100)
            strenght = random.randint(70, 90)
        if salutation == "Scared":
            lifes = random.randint(70, 90)
            strenght = random.randint(70, 90)
        Animal.__init__(self, "Ogre", name, salutation, "Ogrrr Uhrrr!", "OGGGR!", strenght, lifes, True, False,
                        canThink)


class Batman(Animal):
    def __init__(self, name):
        salutation = random.choice(["Killer", "Retarded"])
        strength = 0
        lifes = 0
        if salutation == "killer":
            strength = random.randint(1110, 1120)
            lifes = random.randint(210, 220)
        else:
            strength = random.randint(2, 3)
            lifes = random.randint(10, 12)
        Animal.__init__(self, "Batman", name, salutation, "Joker, don't try anything!", "Dark knight will RISE AGAIN!!",
                        strength, lifes, False, False, False)


class Sheep(Animal):
    def __init__(self, name):
        salutation = random.choice(["Undercut"])
        strength = 0
        lifes = 0
        if salutation == "Undercut":
            strength = random.randint(37, 54)
            lifes = random.randint(50, 100)

        Animal.__init__(self, "Sheep", name, salutation, "Will you cut sheep?", "Will you cut sheep?", strength, lifes,
                        False, False, False)

class Snail(Animal):
    def __init__(self, name):
        salutation = random.choice(["Slowly", "Ferocious", "Agressive", "Nice", "Happy", "Hidden"])
        strength = 0
        lifes = 0
        if salutation == "Slowly":
            strength = random.randint(8,10)
            lifes = random.randint(40,50)
        elif salutation == "Hidden":
            strength = random.radint(18,30)
            lifes = random.randint(200,210)
        else:
            strength = random.randint(18,30)
            lifes = random.randint(101,129)
        Animal.__init__(self, "Snail", name, salutation, "Vruuuu!", "VruAAAhhhh!", strength, lifes, False, False,True)

def genRandomAnimal():
    return random.choice([Cow, Dog, Duckling, Crocodile, Parrot, Batman, Sheep, Snail])(genRandomName())

def genRandomEnemy():
    return random.choice([Ogre, Batman])(genRandomName())

def genRandomName():
    return random.choice(["Melman", "Andy", "Brandy", "Whiskey", "Goal", "Flute", "Brute", "Crude"])
