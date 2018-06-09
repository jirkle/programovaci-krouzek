#!/usr/bin/env python3

import time
import os
from scenes import *
from helpers import *

##############
# Main plots #
##############

name = random.choice(
    ["Strikeforce", "Humpty-Dumpty-Da", "Elaborate Animals", "Cheeky Chubbies", "The Forest Team", "X-Force Forest"])
pack = Pack(name)
for i in range(random.randint(2, 5)):
    pack.AddMembers(genRandomAnimal())

print("Once upon a time, there were small group of animals called %s!" % (name))
intro = ""
for animal in pack.members:
    intro += animal.name + ", the " + animal.salutation + " " + animal.species + ", "
intro += "them all belong to this herd."
intro = intro.capitalize()
print(intro)
print("They get together in order to avoid danger in the forest and defend themselves. Will this help them?")
print("Well, the adventrue begins!")
time.sleep(20)


scenes = [Pond, Tree, Tavern, Den, OldBridge]

#############
# Main loop #
#############
#terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
while len(pack.members) > 0:

    scene = random.choice(scenes)()  # Calls the constructor and creates new scene object
    while not scene.isComplete():
        scene.nextStage(pack)

    if len(pack.members) > 0:
        print("And story continues...")
    #TODO print lines to align ----- start to upper border
    if len(pack.members) > 0:
        time.sleep(10)

