#!/usr/bin/env python3

import string
import math


MORSE_CODE_DICT = {'.-': 'A',
                   '-...': 'B',
                   '-.-.': 'C',
                   '-..': 'D',
                   '.': 'E',
                   '..-.': 'F',
                   '--.': 'G',
                   '....': 'H',
                   '..': 'I',
                   '.---': 'J',
                   '-.-': 'K',
                   '.-..': 'L',
                   '--': 'M',
                   '-.': 'N',
                   '---': 'O',
                   '.--.': 'P',
                   '--.-': 'Q',
                   '.-.': 'R',
                   '...': 'S',
                   '-': 'T',
                   '..-': 'U',
                   '...-': 'V',
                   '.--': 'W',
                   '-..-': 'X',
                   '-.--': 'Y',
                   '--..': 'Z',
                   '.----': '1',
                   '..---': '2',
                   '...--': '3',
                   '....-': '4',
                   '.....': '5',
                   '-....': '6',
                   '--...': '7',
                   '---..': '8',
                   '----.': '9',
                   '-----': '0',
                   '--..--': ',',
                   '.-.-.-': '.',
                   '..--..': '?',
                   '-..-.': '/',
                   '-....-': '-',
                   '-.--.': '()',
                   '-.--.-': ')'}


def decryptMorseCode(message):
    plain = ''
    for letter in message:
        plain += MORSE_CODE_DICT[letter] + ''
    return plain


def is_prime(x):
    x = int(x)
    if x <= 1:
        return "."
    if x == 2:
        return "-"
    if x > 2 and x % 2 == 0:
        return "."
    max_div = math.floor(math.sqrt(x))
    for i in range(3, 1 + max_div, 2):
        if x % i == 0:
            return "."
    return "-"


with open("sources/Liczby.txt", "rb") as f:
    lines = f.read()

numbers = lines.replace(b'\xc2', b'\x20\x2b\x20').replace(b'\xa0', b'')
numbers = numbers.decode('utf-8').split()
password = ""
for item in numbers:
    if item.isnumeric():
        password += is_prime(item)
    else:
        password += " "

print(password.split())
print(decryptMorseCode(password.split()))
