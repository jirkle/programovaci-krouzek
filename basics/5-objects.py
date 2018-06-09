#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Následující řádky obsahují definici objektů. Dalo by se říct, že objekt je takový balíček proměnných a funkcí.
# Slouží především k tomu, abychom kód dokázali ještě více logicky rozčlenit.
# Zároveň platí, že se programy nechají psát i bez objektů, ale ve spoustě případů nám to hodně usnadní práci.
# 
# Zápisu se říká třída, objekt potom už je konkrétně vytvořená instance. Tedy třída slouží k definování objektu – z čeho se objekt skládá,
# jaké obsahuje funkce, proměnné atp. Objekt už obsahuje reálná data, jejichž struktura a funkce jsou popsané třídou.
# Zároveň platí, že z každé třídy můžeme vytvořit libovolné množství objektů a každý můžeme měnit podle potřeby, volat jeho funkce...)
# 
# Takto se tedy zapíše třída:

class Objekt:
	promenna = 3

	def vypis(self):
		print("%d" % self.promenna)

	def nastav(self, p):
		self.promenna = p

# A teď si z ní vytvoříme objekt:

instance = Objekt()

# V pravé části probíhá vytvoření (inicializace) objektu. Ta funguje tak, že se zavolá konstruktor dané třídy a objekt se uloží do proměnné vlevo.
# Konstruktor je speciální funkce ve třídě, která se v pythonu jmenuje __init__() a slouží k nastavení počátečního stavu objektu.
# My jí v našem objektu nemáme a tedy se volá nějaký přednastavený (implicitní) konstruktor.

# Na vytvořeném objektu už můžeme volat funkce a přistupovat k proměnným přes tzv. tečkovou notaci takto:

instance.vypis()
instance.nastav(4)
instance.vypis()
instance2 = Objekt()
instance2.vypis()

# ----------------------------------------------------------------------------------------

# Objektů můžeme vytvořit více, zkuste přijít na to, co dělá a co vypíše následující kód:
# Malá nápověda - l je seznam prvků, l[x] vrátí prvek na x-té pozici a funkce append připojí předaný objekt na konec seznamu.

l = []
for x in range(0, 10):
	l.append(Objekt())
	l[x].nastav(x)

for x in range(0, 10):
	l[x].vypis()
