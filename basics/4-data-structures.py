#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Při programování často potřebujeme nějakým strukturovaným způsobem uložit větší množství prvků, aby se nám s nimi dobře pracovalo.
# K tomu slouží datové struktury. Taková datová struktura obsahuje data a současně nám poskytuje funkce pro manipulaci s těmito daty.
# Např. přístup k prvku, mazání a přidání prvků, iteraci ve for cyklu přes všechny prvky v ní uložené, apod.
# Takové základní datové struktury jsou v Pythonu list (seznam), dict (slovník), tuple (ntice), set (množina) a string (řetězec)
# S listem a stringem už jsme se setkali, podíváme se tedy na ně nejdříve:

# LIST
# List je seznam prvků, které jsou všechny stejných typů. Co to znamená? Do listu můžeme ukládat zvlášť čísla, řetězce, booleovské hodnoty,
# ale dohromady, že bychom do jednoho seznamu uložili jedno číslo a jeden řetězec, už neuděláme (k tomuto nám potom slouží tuple).
# Do seznamu můžeme přidávat prvky nakonec (pomocí funkce append), přistupovat k jednotlivým prvkům, porovnávat dva seznamy a podobně

# Takto se seznam vytvoří:

nakupBillaGatese = ["mléko", "vejce", "zelenina", "brambory", "Nokia", "What's up"] 
nakupLaryhoPage = ["maso", "mléko", "Youtube", "jogurty"]

# K jednotlivým položkám můžeme přistupovat pomocí indexů (začínáme od nuly, tedy první položka má index nula, druhá jedna, ...):

print("Druhá položka na nákupním seznamu Billa Gatese je: %s" % nakupBillaGatese[1])

# Můžeme si vypsat, co si Bill Gates chce koupit:
print("Bill si chce koupit:")
for x in nakupBillaGatese:
	print(x)

# Stejně tak u Laryho Page:
print("Lary si chce koupit:")
for x in nakupLaryhoPage:
	print(x)

# Do nákupních lístků můžeme další položky přidávat na konec následujícím způsobem:
nakupBillaGatese.append("svět")
nakupLaryhoPage.append("svět")

# Když bychom chtěli prvek vložit na určitou pozici, použijeme funkci insert:
nakupLaryhoPage.insert(2, "ilumináti")

# Seznamy můžeme i spojovat, k tomu slouží funkce extend nebo operátor plus.
# V těchto případech se prvky ze seznamu Laryho Page připojí na konec seznamu Billa Gatese:

nakupMocnych = nakupBillaGatese + nakupLaryhoPage
nakupMocnych = nakupBillaGatese.extend(nakupLaryhoPage)

# Teď by nás zajímalo, které položky si chce koupit Lary i Bill současně.
# Uděláme to tak, že projdeme Billův seznam a pro každou položku se podíváme, jestli jí na seznamu nemá také Lary.

print("Lary i Bill si chtějí oba koupit:")

for x in nakupBillaGatese:
	if x in nakupLaryhoPage:
		print(x)

print("A to nebude náhoda!")

# Ze seznamu potom můžeme prvky mazat více způsoby - z konce pomocí funkce pop a konkrétní položku potom pomocí funkce remove:

odstranenaPolozka = nakupBillaGatese.pop()
nakupLaryhoPage.remove("jogurty")


# ----------------------------------------------------------------------------------------
# STRING
# String je speciální verze seznamu určená pro uložení znaků, fungují tady teda stejné principy jako u seznamů.
# V Pythonu máme spoustu možností, jak se stringy pracovat:

retezec1 = "Ahoj světe!"
retezec2 = "Jak se vede?"

print(retezec1)

# Stejně jako seznam, můžeme stringy spojovat:

odstavec = retezec1 + " " + retezec2
print(odstavec)

# String můžeme také procházet postupně po jednotlivých znacích ve for cyklu:

for znak in retezec1:
	print(znak)

# Atp. :)

# ----------------------------------------------------------------------------------------
# TUPLE
# Další verzí seznamu je tuple, jak už bylo zmíněné, je to heterogenní seznam. To znamená, že do něj můžeme ukládat prvky různých typů.
# Jinak funguje na úplně stejných principech...

ntice = ("retezec", 0, True, 'a')

# ----------------------------------------------------------------------------------------
# SET
# Set zastupuje matematickou množinu. Zjednodušeně řečeno, každý prvek se v setu nachází jenom jednou a jednotlivé prvky nejsou nijak uspořádané.

mnozina = set()

# TODO

# ----------------------------------------------------------------------------------------
# DICTIONARY (v jiných programovacích jazycích se jmenuje taky map)
# Dictionary je další zajímavá struktura.
# Funguje podobně jako klasický slovník, ve kterém máme nějaká klíčová slova a ke každému tomuto slovu jeho vysvětlení/význam.
# Tady je to stejné, jenom ke klíčovým slovům můžeme uložit cokoliv - objekty, řetězce, seznamy, ...

slovnik = dict()
# TODO