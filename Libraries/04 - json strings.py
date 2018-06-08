#!/usr/bin/env python3

import json

structure = ['foo', {'bar': ('baz', None, 1.0, 2)}] 
string = json.dumps(structure)
print("{!r}".format(string))
anotherStructure = json.loads(string)
print("{!r}".format(anotherStructure))
