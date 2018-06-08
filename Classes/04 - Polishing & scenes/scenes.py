#!/usr/bin/env python3

import random
from helpers import *
from animals import *


def intoDanger(pack):
    pass


def wander(pack):
    pass


def healMembers(pack):
    print("--------------------------------------------------------------")
    print("All the animals gathered and helped each other to heal their terrible wounds.")
    pack.HealMembers()
    print(pack.DescribePack())


def endGame(pack):
    pack.DeleteAllMembers()
    exit(0)


def leave(pack):
    pass


heal = {"description": "Try to heal everyone in group", "function": healMembers}
end = {"description": "Mischievously murder everyone in your group", "function": endGame, "nextStage": -1}
info = {"description": "Show how incredibly good (or bad) everyone is", "function": showInfo}
wander = {"description": "Do not waste time with this and wander further", "function": wander, "nextStage": -1}


class Scene:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.stage = 0
        self.stages = []
        self.descPrinted = False

    def printHeader(self):
        print("--------------------------------------------------------------")
        print("Your pack has been idle for a while, so it decided it is time for an action!")
        print("After a little bit of roaming through the forest a pack arrived to %s" % self.name)
        if (not self.descPrinted) and self.stage == 0 and self.description != "":
            print(self.description)
            self.descPrinted = True
        print(self.stages[self.stage]["description"])

    def nextStage(self, pack):
        curStage = self.stages[self.stage]
        self.printHeader()
        print("Choices are following:")
        for index, choice in enumerate(curStage["choices"]):
            print("[%d] %s" % (index, choice["description"]))

        x = getNumber("What would you like to do? (enter choice number) >> ", len(curStage["choices"]))
        curStage["choices"][x]["function"](pack)
        if ("nextStage" in curStage["choices"][x]):
            self.stage = curStage["choices"][x]["nextStage"]

    def isComplete(self):
        return self.stage == -1

    def reset(self):
        self.stage = 0


class Pond(Scene):
    def __init__(self):
        Scene.__init__(self, "Spooky pond",
                       "A pond with a lot of meanders, seems calm but it might be a trap!")
        duckling = {"description": "Put the duckling into the pond", "function": self.ducklingOnPond, "nextStage": -1}
        self.stages = [{"description": "There is a brightly yellow duckling nerby.",
                        "choices": [duckling, heal, info, wander, end]}]

    def ducklingOnPond(self, pack):
        print("--------------------------------------------------------------")
        print("The duckling happily flown... until an enormously giant crocodile ate it! And now it's up to you!")
        combat(pack, Crocodile("The gharial"))


class Tree(Scene):
    def __init__(self):
        Scene.__init__(self, "Big scary tree", "")
        climbTree = {"description": "Climb the tree", "function": self.climbTheTree, "nextStage": -1}
        self.stages = [{"description": "A tree rising above all other trees with much wider treetop, it must be spectacular view up there!", "choices": [climbTree, heal, info, wander, end]}]

    def climbTheTree(self, pack):
        print("--------------------------------------------------------------")
        print("Animals decided to send one scout to climb the tree")
        print("The choice is following:")
        print(pack.DescribePack())
        x = getNumber("Who will climb the tree? >> ", len(pack.members))
        victim = pack.ChooseMember(x)
        if not victim.canfly:
            tmp = random.randint(0, 29)
            print(tmp)
            if tmp < 10:
                print("%s climbed the tree but unfortunately an unstable branch collapsed and it fell off" % (
                    victim.GetName()))
                damage = random.randint(10, 40)
                if damage > 30:
                    print("And it was spectacularly bad impact!")
                print("%s took %d damage" % (victim.GetName(), damage))
                victim.TakeDamage(damage)
            elif tmp < 20:
                newMember = GenRandomAnimal()
                print("%s successfully climbed the tree and found very scared %s" % (
                    victim.GetName(), newMember.DescribeAnimal()))
                print("What it was doing there remains unknown...")
                pack.AddMembers(newMember)
            elif tmp < 30:
                print("%s successfully climbed the tree and looked over the forest for an adventure, but found nothing." % (
                    victim.GetName()))
        else:
            tmp = random.randint(0, 19)
            print(tmp)
            if tmp < 10:
                print("What a great choice! %s successfully flew upon the tree and looked over the forest for an adventure, but found nothing." % (
                    victim.GetName()))
            elif tmp < 20:
                newMember = GenRandomAnimal()
                print("What a great choice! %s successfully flew upon the tree and found very scared %s" % (
                    victim.GetName(), newMember.DescribeAnimal()))
                print("What was doing there remains unknown...")
                pack.AddMembers(newMember)

class Cave(Scene):
    def __init__(self):
        Scene.__init__(self, "A silent cave", "A scary looking cave with strange loud noises.")
        follow = {"description": "Follow the lead", "function": self.trail, "nextStage": -1}
        self.stages = [{"description": "UARRrrgh! There is a trail behind the cave.", "choices": [follow, heal, info, wander, end]}]

    def trail(self, pack):
        pass


class Den(Scene):
    def __init__(self):
        Scene.__init__(self, "Wolf's den", "Well known den full of wide range of animals and other stuff. Some of them still alive.")
        follow = {"description": "Follow the lead", "function": self.trail, "nextStage": -1}
        self.stages = [{"description": "What to do next?", "choices": [follow, heal, info, wander, end]}]

    def trail(self, pack):
        pass