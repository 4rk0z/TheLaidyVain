#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def deszyfruj(zrodlo, klucz):
    pozycja = 1
    jawny = []
    roznica = [0]
    przyrostModulo = []
    sumaPrzyrostowModulo = 0
    i = 0
    for szyfrogram in zrodlo:
        if pozycja == 2:
            roznica.append(pozycja * przyrostModulo[i - 1])
        elif pozycja > 2:
            sumaPrzyrostowModulo += przyrostModulo[i - 2]
            roznica.append(
                (pozycja * przyrostModulo[i - 1]) + sumaPrzyrostowModulo)
        jawny.append(chr(szyfrogram - roznica[i]))
        przyrostModulo.append((szyfrogram - roznica[i]) % klucz)
        i += 1
        pozycja += 1
    return "".join(jawny)


passw = [102, 136, 152, 158, 85, 134, 151, 208, 153, 140, 236, 315, 195,
         246, 257, 296, 230, 280, 317, 410, 359, 360, 424, 282, 518, 474]
szyfr = [84, 101, 124, 131, 58, 149, 157, 162, 140, 176, 165, 120, 185, 173, 181,
         170, 221, 162, 257, 258, 228, 286, 240, 288, 281, 269, 256, 289, 325]

# print (deszyfruj(szyfr,7)) # kontrola
print(deszyfruj(passw, 13))
