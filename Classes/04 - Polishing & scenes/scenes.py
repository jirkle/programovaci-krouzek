#!/usr/bin/env python3

import random
from helpers import *
from animals import *


class Scene:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.stage = 0
        self.stages = []
        self.descPrinted = False
        self.choices = dict()
        self.choices["heal"] = {"description": "Try to heal everyone in group", "function": self.healMembers}
        self.choices["end"] = {"description": "Mischievously murder everyone in your group", "function": self.endGame}
        self.choices["info"] = {"description": "Show how incredibly good (or bad) everyone is",
                                "function": self.printInfo}
        self.choices["wander"] = {"description": "Do not waste time with this and wander further",
                                  "function": self.wander}

    def nextStage(self, pack):
        cur_stage = self.stages[self.stage]
        self.printHeader()
        print("Choices are following:")
        for index, choice in enumerate(cur_stage["choices"]):
            print("[%d] %s" % (index, self.choices[choice]["description"]))

        x = getNumber("What would you like to do? (enter choice number) >> ", len(cur_stage["choices"]))
        choice_name = cur_stage["choices"][x]
        self.stage = self.choices[choice_name]["function"](pack)

    def isComplete(self):
        if self.stage == -1:
            return True
        if self.stage >= len(self.stages[self.stage]["choices"]):
            print("Stage %d of scene %s is not there!" % (self.stage, self.name))
            return True

    def printHeader(self):
        print("--------------------------------------------------------------")
        if (not self.descPrinted) and self.stage == 0:
            print("Your pack has been idle for a while, so it decided it is time for an action!")
            print("After a little bit of roaming through the forest a pack arrived to %s" % self.name)
            if self.description != "":
                print(self.description)
            self.descPrinted = True
        print(self.stages[self.stage]["description"])

    def printInfo(self, pack):
        print("--------------------------------------------------------------")
        print(pack.DescribePack())
        return self.stage

    def wander(self, pack):
        return -1

    def healMembers(self, pack):
        print("--------------------------------------------------------------")
        print("All the animals gathered and helped each other to heal their terrible wounds.")
        pack.HealMembers()
        print(pack.DescribePack())
        return self.stage

    def endGame(self, pack):
        pack.DeleteAllMembers()
        return -1


class Pond(Scene):
    def __init__(self):
        Scene.__init__(self, "Spooky pond",
                       "A pond with a lot of meanders, seems calm but it might be a trap!")
        self.choices["duckling"] = {"description": "Put the duckling into the pond", "function": self.ducklingOnPond,
                                    "nextStage": -1}
        self.stages = [
            {"description": "There is a brightly yellow duckling nerby.",
             "choices": ["duckling", "heal", "info", "wander", "end"]}
        ]

    def ducklingOnPond(self, pack):
        print("--------------------------------------------------------------")
        print("The duckling happily flown... until an enormously giant crocodile ate it! And now it's up to you!")
        combat(pack, Crocodile("Gharial"))
        return -1


class Tree(Scene):
    def __init__(self):
        Scene.__init__(self, "Big scary tree", "")
        self.choices["climbtree"] = {"description": "Climb the tree", "function": self.climbTheTree}
        self.stages = [{
            "description": "A tree rising above all other trees with much wider treetop, it must be spectacular view up there!",
            "choices": ["climbtree", "heal", "info", "wander", "end"]}]

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
                new_member = genRandomAnimal()
                print("%s successfully climbed the tree and found very scared %s" % (
                    victim.GetName(), new_member.DescribeAnimal()))
                print("What it was doing there remains unknown...")
                pack.AddMembers(new_member)
            elif tmp < 30:
                print(
                    "%s successfully climbed the tree and looked over the forest for an adventure, but found nothing." % (
                        victim.GetName()))
        else:
            tmp = random.randint(0, 19)
            print(tmp)
            if tmp < 10:
                print(
                    "What a great choice! %s successfully flew upon the tree and looked over the forest for an adventure, but found nothing." % (
                        victim.GetName()))
            elif tmp < 20:
                new_member = genRandomAnimal()
                print("What a great choice! %s successfully flew upon the tree and found very scared %s" % (
                    victim.GetName(), new_member.DescribeAnimal()))
                print("What was doing there remains unknown...")
                pack.AddMembers(new_member)
        return -1


class Cave(Scene):
    def __init__(self):
        Scene.__init__(self, "A silent cave", "A scary looking cave with strange loud noises.")
        self.choices["follow"] = {"description": "Follow the lead", "function": self.follow}
        self.stages = [{"description": "UARRrrgh! There is a trail behind the cave.",
                        "choices": ["follow", "heal", "info", "wander", "end"]}]

    def follow(self, pack):
        return -1


class Den(Scene):
    def __init__(self):
        Scene.__init__(self, "Wolf's den",
                       "Well known den full of wide range of animals and other stuff. Some of them still alive.")
        self.choices["follow"] = {"description": "Follow the lead", "function": self.follow}
        self.stages = [{"description": "What to do next?", "choices": ["follow", "heal", "info", "wander", "end"]}]

    def follow(self, pack):
        print("--------------------------------------------------------------")
        print(
            "There is a lot of animals playing dead, someone from your pack could fetch them but might pay his life for this.")
        print(pack.DescribePack())
        x = getNumber("who will be sacficed ? >> ", len(pack.members))
        victim = pack.ChooseMember(x)
        tmp = random.randint(0, 29)
        if tmp < 10:
            pack.DeleteMember(x)
            print("%s has been unsuccessful. The wolves saw him and immediately killed him." % (victim.GetName()))
        elif tmp < 20:
            pack.DeleteMember(x)
            animal = genRandomAnimal()
            print(
                "%s has been unsuccessful. The wolves saw him at last but it was able to bring %s and immediately killed him." % (
                    victim.GetName(), animal.DescribeAnimal()))
            pack.AddMembers(animal)
        else:
            animal = genRandomAnimal()
            print("%s has been successful. The wolves haven't seen it and it was able to bring %s!" % (
                victim.GetName(), animal.DescribeAnimal()))
            pack.AddMembers(animal)
        return -1


class OldBridge(Scene):
    def __init__(self):
        Scene.__init__(self, "Old Bridge", "Do you see that bridge? It is very old!")
        self.ogre = Ogre("Stone")
        self.selectedAnimal = 0
        # Choices:
        self.choices["bridge"] = {"description": "Send scout", "function": self.bridgeWalk}
        self.choices["killogre"] = {"description": "Kill Ogre", "function": self.animalKillOgre}
        self.choices["talktoogre"] = {"description": "Talk to Ogre", "function": self.animalTalkToOgre}

        # Stages:
        self.stages = [
            {"description": "What will they do?", "choices": ["bridge", "heal", "info", "end"]},
            {"description": "What will they do?", "choices": ["killogre", "talktoogre", "info", "end"]}
        ]

    def bridgeWalk(self, pack):
        print("Animals decided to send a scout to this old bridge")

        print(pack)
        self.selectedAnimal = getNumber("Who will go there? >> ", len(pack.members))
        victim = pack.ChooseMember(self.selectedAnimal)
        tmp = random.randint(0, 29)
        print(tmp)
        if tmp < 10:
            if not victim.canfly:
                print("%s got on bridge, but unfortunately it fell off and wound himself" % (victim.GetName()))
            else:
                print("%s got on bridge, but unfortunately the tree branch has fell down and hit his %s head" % (
                    victim.GetName(), victim.salutation))
            damage = random.randint(10, 35)
            if damage > 30:
                print("And it was spectacularly bad impact!")
                print("%s took %d damage" % (victim.GetName(), damage))
            victim.TakeDamage(damage)
            return -1
        elif tmp < 20:
            print("%s successfully passed bridge and find a way to forest" % (victim.GetName()))
            return -1
        elif tmp < 30:
            print("%s passed the bridge and saw a big ogre hiding under the bridge" % (victim.GetName()))
            return 1

    def animalKillOgre(self, pack):
        combat(pack, self.ogre)
        return -1

    def animalTalkToOgre(self, pack):
        victim = pack.ChooseMember(self.selectedAnimal)
        tmp = random.randint(0, 21)
        if tmp < 10:  # BeFriend
            pack.AddMembers(self.ogre)
            print("%s has talked to ogre and successfully invited him so he joins the pack!" % (victim.GetName()))
        elif tmp > 10:  # NoFriend
            print("%s has talked to ogre but he's not friendly at all" % (victim.GetName()))
            combat(pack, self.ogre)
        return -1


class Tavern(Scene):
    def __init__(self):
        Scene.__init__(self, "Tavern at a happy animal",
                       "Famous local tavern with nice service, good food and unbeatable beverages where everyone gathers")
        self.selectedAnimal = 0

        # Choices:
        self.choices["enterTavern"] = {"description": "Go inside", "function": self.makingNewFriends}

        # Stages:
        self.stages = [
            {"description": "You may go to tavern and make some new friends.",
             "choices": ["enterTavern", "heal", "info", "end"]}
        ]

    def makingNewFriends(self, pack):
        print("--------------------------------------------------------------")
        print("You see a lovely tavern, and you can hear a noisy music. Will you go there?")
        print(pack.DescribePack())
        self.selectedAnimal = getNumber("Which animal will come into tavern? >> ", len(pack.members))
        victim = pack.ChooseMember(self.selectedAnimal)
        tmp = random.randint(0, 29)
        if tmp < 15:
            pack.DeleteMember(self.selectedAnimal)
            print(
                "Unfortunately the %s was secret drinker... and he drank so much alcohol that... he fell down into the barrel with wine and drowned himself." % (
                    victim.GetName()))
        elif tmp < 20:
            pack.DeleteMember(self.selectedAnimal)
            animal = genRandomAnimal()
            print("What a betrayal! %s found a new group and your animals decided to murder him instead" % (
                victim.GetName()))
            pack.AddMembers(animal)
        else:
            animal = genRandomAnimal()
            print("%s has been successful. You have new friend %s!" % (victim.GetName(), animal.DescribeAnimal()))
            pack.AddMembers(animal)
        return -1


class ScaryHouse(Scene):
    def __init__(self):
        Scene.__init__(self, "A silent house", "Your dead pack members are there.")
        self.choices["follow"] = {"description": "Yes, I will!", "function": self.follow}
        self.stages = [{"description": "Would you go inside?", "choices": ["follow", "heal", "info", "wander", "end"]}]

    def follow(self, pack):
        return -1


def genRandomScene():
    return random.choice([Pond, Tree, Den, Tavern, OldBridge, ScaryHouse])()
