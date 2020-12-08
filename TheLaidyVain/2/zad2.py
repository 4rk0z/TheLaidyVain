#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii

tab = []
try:

    with open("sources/Regulamin organizacyjny BT.txt", 'rb') as f:
        while True:
            byte = f.read(1)
            if not byte:  # eof
                break
            if hex(ord(byte)) == '0x61':
                tab.append('0')
            elif hex(ord(byte)) == '0xd0':
                byte = f.read(1)
                if hex(ord(byte)) >= '0xb0':
                    tab.append('1')
    znak = '0b'
    for elem in tab:
        znak = znak + elem
        if int(znak,2) >= 32 and int(znak,2) <= 126 and len(znak) == 10:
            print(chr(int(znak, 2)), end='', flush=True)
            znak = '0b'
finally:
    f.close()
    print()
