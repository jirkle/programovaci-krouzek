#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tímto říkáme, že v kódu budeme pracovat s knihovnou sys
import sys

# VAROVÁNÍ: Jestliže rádi kopírujete a špagetový kód vám nevadí, rozhodně následující řádky nečtěte!

print("")
print("FOR CYCLES")

# Následující řádky obsahují cykly. Často potřebujeme nějaký příkaz/y vykonat několikrát za sebou pouze s nějakým měnícím se parametrem.
# K tomu nám slouží cykly. První cyklus postupně ukládá do proměnné x čísla od 1 do 3 a spouští odsazené příkazy. 
# V tomto případě vypíše obsah proměnné x.

print("Umím počítat do tří! Podívej!")
for x in range(1, 4):
    print("{0}".format(x))

# ----------------------------------------------------------------------------------------

# K druhému cyklu si nejdříve vytvoříme seznam se čtyřmi položkami. Potom všechny položky vypíšeme s mezerou za.
# Ještě stojí za povšimnutí, že v tomto případě funkci print předáváme parametr end=''.
# Funkce print totiž automaticky vypisuje za řetězec konec řádku,
# tímto jí řekneme, že chceme na konec vypsat prázdný řetězec, jinými slovy nechceme tam vypsat nic.

print("")
print("FOR CYCLES LIST")

seznam = ["Jedna", "dvě", "Honza", "nejde"]

for x in seznam:
    print("{0} ".format(x), end='')

# Předchozí výpis není ukončený koncem řádku, proto jeden vypíšeme
print("")

# ----------------------------------------------------------------------------------------

print("")
print("FOR CYCLES ARGS")

# Z minulého souboru už víme, kde se nacházejí všechny argumenty, se kterými byl skript spuštěný, můžeme si je tedy takto jednoduše vypsat:

for x in sys.argv:
    print(x)

# ----------------------------------------------------------------------------------------

# To byly cykly omezené intervalem/počtem prvků, co si ale počít, když nevíme, kolikrát konkrétně chceme nějaký/é příkaz/y vykonat?
# Víme jen, že někdy v budoucnu nastane situace, kdy budeme chtít skončit. Příkladem může být herní smyčka,
# kdy ve hrách chceme opakovat vykreslování až dokud uživatel nezvolí, že chce skončit. Jak se s tím teda vypořádat?
# Od toho exituje cyklus while, který se vykonává do té doby, dokud je podmínka vyhodnocená jako True (pravdivá):

print("")
print("WHILE CYCLES")

# NÁSLEDUJÍCÍ KÓD DOPORUČUJU ZAKOMENTOVAT :)
x = 1
while True:
    print("Do nekonečna a ještě dál! Už se blížíme - {0}".format(x))
    x += 1


# Následující zápisy dvou cyklů jsou ekvivalentní:
x = 1
while x <= 4:
    print("Do čtyř a konec! Už se blížíme - {0}".format(x))
    x += 1

x = 1
while True:
    print("Do čtyř a konec! Už se blížíme - {0}".format(x))
    x += 1
    if x > 4:
    	break
