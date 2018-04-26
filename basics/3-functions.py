#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Následující řádky obsahují definici funkce. Funkce se hodí, když chceme kód nějak logicky členit,
# uspořádat do "přihrádek", případně když máme části kódu, které vykonáváme ve více částech programu a díky funkcím nám je stačí napsat jednou.
# Interpretr si pamatuje definici funkce, její název a také odkaz na příkazy.
# Když jí potom zavoláme jménem a předáme parametry, už ví, kde jí má hledat a co vykonat.
print("")
print("FUNCTIONS")

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
# Když to dáme dohromady, následující řádky zavolají naše funkce a postupně vypíšou "Foo!", potom "Jedna dvě!" a na konec "Honza Tě sleduje!"

foo()
vracenaHodnota = skvelaFunkce("Jedna dvě!")
print(vracenaHodnota)

# Poslední dva řádky jdou ještě zjednodušit a napsat jako jeden, tímto nám odpadá nutnost pamatovat si v proměnné vracenaHodnota vrácenou hodnotu:
# print(skvelaFunkce("Jedna dvě!"))

# ----------------------------------------------------------------------------------------
#
# Vrátit můžeme současně více hodnot, k tomu využijeme tuple (víc o něm v souboru k datovým strukturám)
print("")
print("MULTIPLE PARAMETERS RETURN")

def skvelaFunkceVracejiciHodneVeci():
	return ("Honza Tě sleduje!", 0, True, "Ale ne!", 42)

print(skvelaFunkceVracejiciHodneVeci())

#
# ----------------------------------------------------------------------------------------
#
# A ještě trocha teorie :) Parametry se předávají buď hodnotou, nebo odkazem. Jaký je v tom rozdíl? Pokud předáme proměnnou odkazem a ve funkci
# jí změníme, zjistíme, že se nám změnila i tam, odkud jsme funkci zavolali.
# Pokud předáme hodnotou, interpretr proměnnou zkopíruje, a tak na ní jakékoliv změny ve funkci nebudou mít vliv.
#
# A jak to je v Pythonu? Je to trochu složitější...
# Všechny proměnné základních typů (číslo, řetězec, znak, boolean - hodnota True/False, tuple, ...) se předávají hodnotou.
# Ostatní složitější objekty potom referencí.

# Příklad: Řetězec se předává hodnotou a proto zůstane nezměněný
print("")
print("PASS BY REFERENCE/VALUE")

def upravRetezec(retezec):
	retezec = "Honza Tě sleduje!"

s = "Jedna dvě!"
print("Před: {0}".format(s))
upravRetezec(s)
print("Po: {0}".format(s))

# Seznam je jedním ze složitějších typů a proto ho následující funkce změní:

def upravSeznam(seznam):
	seznam[2] = "Pepa"

seznam = ["Jedna", "dvě", "Honza", "nejde"]
print("Před: {0}".format(seznam))
upravSeznam(seznam)
print("Po: {0}".format(seznam))
