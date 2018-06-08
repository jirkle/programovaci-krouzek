#!/usr/bin/env python3

import random
from scenes import *
from helpers import *

##############
# Main plots #
##############

name = random.choice(["Strikeforce", "Humpty-Dumpty-Da", "Elaborate Animals", "Cheeky Chubbies", "The Forest Team", "X-Force Forest"])
pack = Pack(name)

for i in range(random.randint(2,5)):
	pack.AddMembers(GenRandomAnimal())
print(pack.DescribePack())
print("A pack of animals has gathered in order to avoid danger in the forest and defend themselves. Will this help them?")

scenes = [Pond(), Tree(), Cave()]

#############
# Main loop #
#############

while len(pack.members) > 0:
	scene = random.choice(scenes)
	while not scene.isComplete():
		scene.nextStage(pack)
	scene.reset()