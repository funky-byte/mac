#!/usr/bin/python3

import sys

def cyrillic_check(a):
    alphabet = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    find_cyrillic = [x for x in alphabet if x in a.lower()]
    if find_cyrillic:
        print("Сyrillic simbols: %s" % find_cyrillic) 
        return False
    return True

def replace(a):
    if "-" in a:
        print(a.replace('-',':'))
    if ":" in a:
        print(a.replace(':','-'))

if len(sys.argv) > 1 :
    if cyrillic_check(sys.argv[1]):
        replace(sys.argv[1])
else:
    while True:
        a = str(input("mac: "))
        if a == "q":
            break
        else:
            if cyrillic_check(a):
                replace(a)

