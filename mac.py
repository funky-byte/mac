#!/usr/bin/python3

import sys


def help():
    print(
        "Convert mac-address with different separations.\n"
        "Without flags convert from normal mac-address separated by ':' or '-'\n"
        "-c convert from to cisco-like mac-address separated by '.' or '-'\n" )


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


def cisco_replace(mac):
     if "." in mac:
        mac = mac.replace('.','')
        out = [(mac[i:i+2]) for i in range(0, len(mac), 2)]
        print(*out, sep='-')
     if "-" in mac:
        mac = mac.replace('-','')
        out = [(mac.lower()[i:i+4]) for i in range(0, len(mac), 4)]
        print(*out, sep='.')
     if ":" in mac:
        mac = mac.replace(':','')
        out = [(mac.lower()[i:i+4]) for i in range(0, len(mac), 4)]
        print(*out, sep='.')


def cisco_mac():
    if len(sys.argv) > 2:
        if cyrillic_check(sys.argv[2]):
            cisco_replace(sys.argv[2])
    else:
        print("input cisco-like mac or normal mac separated by '-'")


if len(sys.argv) > 1 :
    if sys.argv[1] == "-h":
        help()
    elif sys.argv[1] == "-c":
        cisco_mac()
    else:
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
