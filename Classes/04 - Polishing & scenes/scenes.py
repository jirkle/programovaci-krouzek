#!/usr/bin/env python3

import random
from helpers import *
from animals import *


def IntoDanger(pack):
    pass


def HealMembers(pack):
    print("You decided to heal every member of your pack:")
    pack.HealMembers()
    print(pack.DescribePack())


def EndGame(pack):
    pack.DeleteAllMembers()
    exit(0)
    pass


choice1 = {"description": "Follow the lead", "function": IntoDanger}
heal = {"description": "Heal everyone", "function": HealMembers}
end = {"description": "Mischievously murder everyone in your group", "function": EndGame, "nextStage": -1}


class Scene:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.stage = 0
        self.stages = []

    def printHeader(self):
        print("--------------------------------------------------------------")
        print("Your pack has been idle for a while, so it decided it is time for an action!")
        print("After a little bit of roaming through the forest a pack arrived to %s" % self.name)
        if (self.stage == 0): print(self.description)
        print(self.stages[self.stage]["description"])

    def nextStage(self, pack):
        curStage = self.stages[self.stage]
        self.printHeader()
        print("Choices are following:")
        for index, choice in enumerate(curStage["choices"]):
            print("[%d] %s" % (index, choice["description"]))

        x = GetNumber("What would you like to do? (enter choice number) >> ", len(curStage["choices"]))
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
        duckling1 = {"description": "Put the duckling into the pond", "function": self.ducklingOnPond, "nextStage": -1}
        self.stages = [{"description": "There is a brightly yellow duckling nerby.", "choices": [duckling1, heal, end]}]

    def ducklingOnPond(self, pack):
        print("--------------------------------------------------------------")
        print("The duckling happily flown... until an enormously giant crocodile ate it! And now it's up to you!")
        Combat(pack, Crocodile("The gharial"))


class Tree(Scene):
    def __init__(self):
        Scene.__init__(self, "Big scary tree", "")
        self.stages = [{"description": "Nothing happens.", "choices": [choice1, heal, end]}]


class Cave(Scene):
    def __init__(self):
        Scene.__init__(self, "A silent cave", "")
        self.stages = [{"description": "Nothing happens.", "choices": [choice1, heal, end]}]
