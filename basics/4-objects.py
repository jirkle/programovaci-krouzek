#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Následující řádky obsahují definici objektů. Dalo by se říct, že objekt je takový balíček proměnných a funkcí.
# Slouží především k tomu, abychom kód dokázali ještě více logicky rozčlenit.
# Zároveň platí, že se programy nechají psát i bez objektů, ale ve spoustě případů nám velmi usnadní práci.
# 
# Zápisu se říká třída, objektu potom už konkrétně vytvořené instanci (tady si to zaslouží popsat trochu přesněji:
# 
# Třída slouží k definování objektu – z čeho se objekt skládá, jaké obsahuje funkce, proměnné atp.
# Objekt je potom instancí třídy. Objekt už obsahuje reálná data, jejichž struktura je popsaná třídou.
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

# Na vytvořeném objektu už můžeme volat funkce přes tzv. tečkovou notaci:

instance.vypis()
instance.nastav(4)
instance.vypis()

# Objektů můžeme vytvořit více, zkuste přijít na to, co dělá a co vypíše následující kód:
# Malá nápověda - l je seznam prvků, l[x] vrátí prvek na x-té pozici a append připojí předaný parametr na konec seznamu.

l = []
for x in range(0, 10):
	l.append(Objekt())
	l[x].nastav(x)

for x in range(0, 10):
	l[x].vypis()
