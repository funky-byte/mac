#!/usr/bin/python3

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
        replace(a)