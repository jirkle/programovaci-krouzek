#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Následující řádky obsahují definici funkce. Funkce se hodí, když chceme kód nějak logicky členit,
# uspořádat do "přihrádek", případně když máme části kódu, které vykonáváme ve více částech programu a díky funkcím nám je stačí napsat jednou.
# Interpretr si pamatuje definici funkce, její název a také odkaz na příkazy.
# Když jí potom zavoláme jménem a předáme parametry, už ví, kde jí má hledat a co vykonat.

# Takto může vypadat funkce, která vypíše na příkazový řádek "Foo!"
def foo():
	print("Foo!")

# Co si ale počít, jestli chceme měnit chování funkce v různých situacích a vrátit vypočítanou hodnotu? Od toho existují parametry a návratová hodnota.
# Parametrem předáme funkci obsah některé proměnné a poté ho v těle funkce můžeme určitým požadovaným způsobem využít.
# Co se má vrátit potom uvedeme klíčovým slovem return.
# Takto tedy zapíšeme funkci, která vypíše obsah proměnné parametr a vrátí řetězec s varováním o Honzovi:
def skvelaFunkce(parametr):
	print(parametr)
	return "Honza Tě sleduje!"

# Teď už překladač ví, že máme skvelouFunkci a funkci foo, můžeme je teda zavolat a mrknout se, co dělají.
# Když to dáme dohromady, následující řádky nejdříve vypíšou "Foo!", potom "Jedna dvě!" a na konec "Honza Tě sleduje!"

foo()
vracenaHodnota = skvelaFunkce("Jedna dvě!")
print(vracenaHodnota)

# Poslední dva řádky jdou ještě zjednodušit a napsat jako jeden, tímto nám odpadá nutnost pamatovat si v proměnné vracenaHodnota vrácenou hodnotu:
# print(skvelaFunkce("Jedna dvě!"))
