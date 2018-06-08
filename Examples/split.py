#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def split(text, delimiter):
	l = []
	tmp = ""
	i = 0
	while i < len(text):
#		print(tmp)
		if text[i] != delimiter[0]:
			tmp = tmp+text[i]
			i += 1
			continue

		s = True
		for j,d in enumerate(delimiter):
			if i+j>len(text) or text[i+j] != d:
				s = False
				break
		if s:
			l.append(tmp)
			tmp = ""
			i = i+len(delimiter)
		else:
			tmp = tmp+text[i]
			i += 1
	l.append(tmp)
	return l

def splitmany(texty, delimiter):
	r = []
	for text in texty:
		r.append(split(text, delimiter))
	return r


texty = ["jmeno, prijmeni, email, cislo", "aaa,aaaa, a,a ,a, a"]
vysledky = [["jmeno", "prijmeni", "email", "cislo"], ["aaa,aaaa", "a,a ,a", "a"]]

tmp = splitmany(texty, ", ")
if tmp == vysledky:
	print("Test prošel!", tmp)
else:
	print("Test neprošel!", tmp)

for i, test in enumerate(texty):
	tmp = split(test, ", ")
	if tmp == vysledky[i]:
		print("Test prošel!", tmp)
	else:
		print("Test neprošel!", tmp)
