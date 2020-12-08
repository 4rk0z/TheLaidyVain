#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import itertools

try:
    first  = ['a','e','g','H','i','k','k','l','n','r','s','y','y','Z',' ']
    second = ['a','c','e','i','r','r','s','t','w','w','y','z','z',' ']


    first_Henryk_Z____ski  = ['a','g','l','y']  # wystarczy zauważyć że imię i nazwisko zaczyna się dużą literą, rozdziela je spacja, nazwiska w Polsce kończą się na -ski -wski
    perm1 = itertools.permutations(first_Henryk_Z____ski)
    for i in list(perm1):
     wynik = 'Henryk Z'+''.join(i)+'ski'
     print (wynik)

    second_czwarty_  = ['e','i','r','s','w','z']  # wystarczy zauważyć że są dwa wyrazy, jeden z nich to np. czwarty
    perm2 = itertools.permutations(second_czwarty_)
    for i in list(perm2):
     wynik = 'czwarty '+''.join(i)
     print (wynik)

finally:
    print
