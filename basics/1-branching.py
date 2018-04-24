#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
