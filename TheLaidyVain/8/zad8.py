#!/usr/bin/env python3
#-*- coding: utf-8 -*-


try:
    szyfrogram = ['B','E','D','Fis','Ces','Des','C2','His','Ces','Eis','G','Ces2','Ces','Ais','Fis','Gis','Ais','B']
    ces  = ['Ces','Des','Es','Fes','Ges','As','B','Ces2']     #  (b - obnizony)
    cdur = ['C','D','E','F','G','A','H','C2']                      #  (kasownik)
    cis  = ['Cis','Dis','Eis','Fis','Gis','Ais','His','Cis2']        #  (# - podwyzszony)
    alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','Y','Z']
    gama = []
    for i in range(8):
        gama.append(ces[i])
        gama.append(cdur[i])
        gama.append(cis[i])
    for i in list(szyfrogram):
        print(alfabet[int(gama.index(i))], end='', flush=True)
finally:
    print()
