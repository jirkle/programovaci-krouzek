#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VAROVÁNÍ: Jestliže rádi kopírujete a špagetový kód vám nevadí, rozhodně následující řádky nečtěte!

# Následující řádky obsahují cykly. Často potřebujeme nějaký příkaz/y vykonat několikrát za sebou pouze s nějakým měnícím se parametrem.
# K tomu nám slouží cykly. První cyklus postupně ukládá do proměnné x čísla od 1 do 3 a spouští odsazené příkazy, v tomto případě pouze vypíše obsah proměnné x.

print("Umím počítat do tří! Podívej!")
for x in range(1, 4):
    print("%d" % x)


# K druhému cyklu si nejdříve vytvoříme seznam se čtyřmi položkami. Potom všechny položky vypíšeme s mezerou za.
# Ještě stojí za povšimnutí, že v tomto případě funkci print předáváme parametr end=''.
# Funkce print totiž automaticky vypisuje za řetězec konec řádku,
# tímto jí řekneme, že chceme na konec vypsat prázdný řetězec, jinými slovy nechceme tam vypsat nic.

seznam = ["Jedna", "dvě", "Honza", "nejde"]

for x in seznam:
    print("%s " % x, end='')

# Předchozí výpis není ukončený koncem řádku, proto jeden vypíšeme
print("")

# To byly cykly omezené počtem, co si ale počít, když nevíme, kolikrát konkrétně chceme nějaký/é příkaz/y vykonat?
# Víme jen, že někdy v budoucnu nastane situace, kdy budeme chtít skončit. Příkladem může být herní smyčka,
# kdy ve hrách chceme opakovat vykreslování na monitor až dokud uživatel nezvolí, že chce skončit. Jak se s tím teda vyrovnat?
# Od toho exituje cyklus while:

x = 1
while True:
    print("Do nekonečna a ještě dál! Už se blížíme - %d" % (x))
    x += 1

# Následující zápisy dvou cyklů jsou ekvivalentní:

x = 1
while x <= 4:
    print("Do čtyř a konec! Už se blížíme - %d" % (x))
    x += 1

x = 1
while True:
    print("Do čtyř a konec! Už se blížíme - %d" % (x))
    x += 1
    if x > 4:
    	break
