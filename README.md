Конвертирование разделителя в MAC-адресе с "-" на ":" и на оборот с проверкой наличии кириллицы в адресе.
q - выход

Converting the separator in the MAC address from "-" to ":" and vice versa, checking for the presence of Cyrillic in the address.
q - quit


```
shell ~ $ ./mac.py 00-17-9A-05-85-56
00:17:9A:05:85:56
shell ~ $

```


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

