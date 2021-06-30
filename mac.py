#!/usr/bin/python3

from sys import argv, exit
from requests import get

def help():
    print("\n"
        "Convert mac-address with different separations.\n\n"
        "\033[1m 1) \033[0m Without flags convert from normal mac-address separated by ':' or '-'\n"
        "\033[1m 2) -c \033[0m convert from to cisco-like mac-address separated by '.' or '-'\n"
        "\033[1m 3) -v \033[0m show mac vendor from site macvendors.com \n" )


def cyrillic_check(mac):
    alphabet = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    find_cyrillic = [x for x in alphabet if x in mac.lower()]
    if find_cyrillic:
        print("Сyrillic simbols: %s" % find_cyrillic) 
        return False
    return True


def replace(mac):
    if "-" in mac:
        print(mac.replace('-',':'))
    if ":" in mac:
        print(mac.replace(':','-'))


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
    if len(argv) > 2:
        if cyrillic_check(argv[2]):
            cisco_replace(argv[2])
    else:
        print("input cisco-like mac or normal mac separated by '-'")

def macvendor():
    if len(argv)> 2:
        if cyrillic_check(argv[2]):
            r = get('https://api.macvendors.com/%s' % argv[2])
            print("\033[1m %s \033[0m \n" % r.text)

if len(argv) > 1 :
    if argv[1] == "-h" or "--help":
        help()
    elif argv[1] == "-c":
        cisco_mac()
    elif argv[1] == "-v":
        macvendor()
    else:
        if cyrillic_check(argv[1]):
            replace(argv[1])
else:
    while True:
        try:
          mac = str(input("mac: "))
        except KeyboardInterrupt:
          break
        except KeyboardInterrupt:
            exit(0)
        else:
          if mac == "q":
              break
          elif mac == "h":
              help()
          else:
              if cyrillic_check(mac):
                  replace(mac)
