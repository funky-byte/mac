#!/usr/bin/python3

def cyrillic_check(a):
    alphabet = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    find_cyrillic = [x for x in alphabet if x in a.lower()]
    if not find_cyrillic:
        return True
    else:
        print("Сyrillic simbols: %s" % find_cyrillic) 

def replace(a):
    if "-" in a:
        print(a.replace('-',':'))
    if ":" in a:
        print(a.replace(':','-'))

i = 1
while i > 0:
    a = str(input("mac: "))
    if a == "q":
        break
    else:
        if cyrillic_check(a) == True:
            replace(a)