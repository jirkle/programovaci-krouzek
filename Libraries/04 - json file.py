#!/usr/bin/env python3

import json

with open('data/data.json') as f:
    data = json.load(f)

print(data)
for key, value in data.items():
	print("--------------")
	print(value)
