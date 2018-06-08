#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Jazyk Python je interpretovaný a imperativní jazyk. Doufám, že jsem vás přemírou cizích slov na začátek neodradil :D hned popíšu, co to znamená.

# Interpretovaný jazyk je takový, u kterého se programy nepřekláda do strojového kódu procesoru před spuštěním, ale uchovávají se v textové podobě.
# K jejich spuštění musí v systému běžet tzv. interpretr, který za běhu (on the fly) překládá ty části kódu, které se zrovna mají vykonat.
# Potom Pythoní skripty spouštíme z příkazové řádky pomocí volání interpretru takto:
# python3 nazevSouboruSeSkriptem argumenty...

# Naproti tomu existují překládané programovací jazyky. U nich se překladače postarají o překlad do strojového kódu ještě před jejich spuštěním.
# My už teda spouštíme jen výslednou binárku. (např. ve Windowsech to jsou typicky *.exe soubory)

# To druhé slovo - imperativní - by se nechalo přeložit jako přikazovací jazyk. Jednoduše to znamená, že počítači v programu explicitně říkáme, co má dělat (např. uložit nějakou hodnotu do proměnné, vypsat řetězec na výstup, konstruovat obejkt, apod.)

# A teď už teda k programování, začneme zlehka :)
# Následující řádek vypíše důležité sdělení světu!
# Voláme tu knihovní funkci pythonu s názvem print a parametrem "Hello world", víc funkce probereme v dalších příkladech...

print("{0}".format("Hello world"))


