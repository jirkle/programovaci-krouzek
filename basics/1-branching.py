#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tímto říkáme, že v kódu budeme pracovat s knihovnou sys, tu využimeme pro získání sys.argv, kde jsou uložené argumenty z příkazové řádky
import sys

# Následující řádky obsahují větvení. Často potřebujeme nějaký příkaz/y vykonat pouze v závislosti na stavu programu (v tomto případě na obsahu proměnné promenna).
# V následující ukázce varujeme uživatele programu na příchod některých individuí, konkrétně bychom všechny chtěli upozornit na příchod Honzy.
# Ptáme se tedy, jestli je v proměnné promenna uložený Honza nebo Jan a pokud ano, všechny varujeme!
# Pokud tam Jan ani Honza není, zajímá nás ještě, jestli v ní není uložené auto. To přece nechodí, ale jezdí, proto vypíšeme varování, že jede auto.
# Když už víme, že ani Honza ani Jan nejdou a auto nejede, varujeme jen tak obecně - někdo jde!

promenna = "Honza"

if promenna == "Honza" or promenna == "Jan":
	print("Honza jde!")
elif promenna == "Auto":
	print("Auto jede!")
else:
	print("Někdo jde!")

# K tomuto je potřeba ještě trocha teorie - podmínky vychází z logiky. Když skript v kódu dojde k nějaké podmínce, vyhodnotí jí a můžou nastat dva stavy:
# Buď je True (pravdivá) a vykoná se bezprostředně následující větev, nebo je False (nepravdivá) a vyhodnotí se následující větev elif/else.
# V podmínkách využíváme několik základních operátorů - rovná se ==, nerovná se !=, větší než >, menší něž <, větší nebo rovno >=, menší nebo rovno <=
# Současně můžeme spojovat více jednoduchých podmínek pomocí klíčových slov and (logické a), or (logické nebo), atp.
# Takto se stalo v první podmínce v minulém příkladu.

# Vyhodnocení podmínek probíhá líným způsobem, to znamená, že interpretr nevyhodnocuje zbytek podmínky, pokud už ví, že do které větve má skočit.
# Tohle už je kapku pokročilejší látka, koho to zajímá, zkuste si na Googlu vyhledat podrobnosti a promyslet, jak to funguje a k čemu to může být dobré.

# ----------------------------------------------------------------------------------------

# Rozhodování z minulého příkladu můžeme upravit tak, abychom vyhodnocovali vstup od uživatele.
# Protože náš skript spouštíme z příkazové řádky, můžeme toto rozhodování použít na předané argumenty
# (tedy podmínky zůstaly stejné, pouze vyhodnocujeme na argumentech - zda některý z nich nebyl Honza, Jan nebo Auto)

if "Honza" in sys.argv or "Jan" in sys.argv:
	print("Honza jde!")
elif "Auto" in sys.argv:
	print("Auto jede!")
else:
	print("Někdo jde!")

# Pár vysvětlivek:
# sys.args je proměnná, která obsahuje seznam všech argumentů, se kterými byl skript spuštěný.
# Klíčové slovo in vrací True/False podle toho, jestli se řetězec vlevo nachází v seznamu vpravo.
