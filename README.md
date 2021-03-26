Конвертирование разделителя в MAC-адресе с "-" на ":" и на оборот с проверкой наличии кириллицы в адресе.


Интерактивный режим (без флагов):
```
h - сравка
q - выход
v - узнать с сайта macvendors.com производителя устройства
```

Флаги:
```
-c - конвертировать из/в cisco-mac синтаксис
-h - сравка
-v - узнать с сайта macvendors.com производителя устройства
```



Converting the separator in the MAC address from "-" to ":" and vice versa, checking for the presence of Cyrillic in the address.
Interractive mode (w/o flags):
```
h - help
q - quit
v - check device vendor from macvendors.com
```

Flags:
```
-c - convert from to cisco-like mac-address separated by '.' or '-'
-h - help
-v - check device vendor from macvendors.com

```


How to install and usage:
```
shell ~ $ git clone --depth=1 https://github.com/anamorfis/mac
shell ~ $ cd mac
shell ~ $ ./mac.py
mac: 00-17-9A-05-85-56
00:17:9A:05:85:56
mac: 00:17:9A:05:85:56
00-17-9A-05-85-56
mac: 00:17:9A:05:85:ВС
Сyrillic simbols: ['в', 'с']
mac: q
shell ~ $
```

```
shell ~ $ ./mac.py 00-17-9A-05-85-56
00:17:9A:05:85:56
shell ~ $
```

```
shell ~ $ ./mac.py -c 00-17-9A-05-85-56
0017.9a05.8556
shell ~ $ ./mac.py -c 00:17:9A:05:85:56
0017.9a05.8556
shell ~ $ ./mac.py -c 0017.9a05.8556
00-17-9A-05-85-56
shell ~ $
```

```
shell ~ $ ./mac.py -v 00-17-9A-05-85-56
 D-Link Corporation
shell ~ $ ./mac.py -v 00:17:9A:05:85:56
 D-Link Corporation
shell ~ $ ./mac.py -v 0017.9a05.8556
 D-Link Corporation
shell ~ $
```
