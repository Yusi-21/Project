## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
```
grep '.*' /etc/passwd | cut -d: -f1 | sort
```
```
adm
at
bin
cron
cyrus
daemon
dhcp
ftp
games
guest
halt
lp
mail
man
news
nobody
ntp
operator
postmaster
root
shutdown
smmsp
squid
sshd
svn
sync
uucp
vpopmail
xfs
```
## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 7 наибольших портов, как показано в примере ниже:
```
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 7
```

```
103 pim
98 encap
94 ipip
89 ospf
81 vmtp
73 rspf
60 ipv6-opts
```

## Задача 3

Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):
```
#!/bin/bash

text=$*
length_txt=${#text}

for a in $(seq 1 $((length_txt + 26))); do
    line+="-"
done

echo "+${line}+"
echo "| Hello from Turkmenistan! |"
echo "+${line}+"
```

```
+--------------------------+
| Hello from Turkmenistan! |
+--------------------------+
```


## Задача 4

Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).
```
#!/bin/bash

file="$1"

id=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)

grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | grep -vE '\b(int|void|return|if|else|for|while|include|stdio.h)\b' | sort | uniq 
```


```
h
hello 
main
n
printf
stdio
world
```

## Задача 5

Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

```
#!/bin/bash

ls -l
touch usa.cpp
echo " "

ls -l
chmod 766 usa.cpp
echo " "
ls -l

sudo mv usa.cpp /usr/local/bin/   //здесь можно написать cp(copy) вместо mv(move),
                                  //чтобы вывод было понятно написал mv
cd /usr/local/bin/
ls -l 
```

```
localhost:~# bash zad5.sh
total 20
-rw-r--r--    1 root     root           114 Jul  5  2020 bench.py
-rw-r--r--    1 root     root            76 Jul  3  2020 hello.c
-rw-r--r--    1 root     root            22 Jun 26  2020 hello.js
-rw-r--r--    1 root     root           151 Jul  5  2020 readme.txt
-rw-r--r--    1 root     root           141 Sep 20 20:47 zad5.sh
 
total 20
-rw-r--r--    1 root     root           114 Jul  5  2020 bench.py
-rw-r--r--    1 root     root            76 Jul  3  2020 hello.c
-rw-r--r--    1 root     root            22 Jun 26  2020 hello.js
-rw-r--r--    1 root     root           151 Jul  5  2020 readme.txt
-rw-r--r--    1 root     root             0 Sep 20 20:47 usa.cpp    //создал 
-rw-r--r--    1 root     root           141 Sep 20 20:47 zad5.sh
 
total 20
-rw-r--r--    1 root     root           114 Jul  5  2020 bench.py
-rw-r--r--    1 root     root            76 Jul  3  2020 hello.c
-rw-r--r--    1 root     root            22 Jun 26  2020 hello.js
-rw-r--r--    1 root     root           151 Jul  5  2020 readme.txt
-rwxrw-rw-    1 root     root             0 Sep 20 20:47 usa.cpp    //поменял права доступа
-rw-r--r--    1 root     root           141 Sep 20 20:47 zad5.sh
total 4404
-rwxr-xr-x    1 root     root         42500 Jul  5  2020 export_file
-rwxr-xr-x    1 root     root        325844 Jul  6  2020 ffasn1dump
-rwxr-xr-x    1 root     root        205012 Aug 17  2020 fldev
lrwxrwxrwx    1 root     root             6 Jul  5  2020 qe -> qemacs
-rwxr-xr-x    1 root     root        712292 Jul  5  2020 qemacs
-rwxr-xr-x    1 root     root       1045720 Jul  5  2020 qjs
-rwxr-xr-x    1 root     root        816284 Jul  5  2020 qjsc
lrwxrwxrwx    1 root     root             3 Jul  5  2020 qjscalc -> qjs
lrwxrwxrwx    1 root     root            11 Jul  5  2020 set_import_dir -> expor
t_file
-rwxr-xr-x    1 root     root         13404 Nov 21  2020 settime
-rwxr-xr-x    1 root     root        267584 Jul  5  2020 tcc
-rwxr-xr-x    1 root     root        678504 Jan  9  2021 temu
-rwxr-xr-x    1 root     root         50268 Jul  5  2020 tinypi
-rwxrw-rw-    1 root     root             0 Sep 20 20:47 usa.cpp   //переместил
-rwxr-xr-x    1 root     root         45636 Jul  5  2020 vfagent
-rwxr-xr-x    1 root     root         35304 Jul  5  2020 vflogin
-rwxr-xr-x    1 root     root        204336 Jul  5  2020 vfsync
-rwxr-xr-x    1 root     root         24360 Jul  5  2020 vmtime
```

## Задача 6

Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.

## Задача 7

Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

## Задача 8

Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

## Задача 9

Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.

## Задача 10

Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром. 

## Полезные ссылки

Линукс в браузере: https://bellard.org/jslinux/

ShellCheck: https://www.shellcheck.net/

Разработка CLI-приложений

Общие сведения

https://ru.wikipedia.org/wiki/Интерфейс_командной_строки
https://nullprogram.com/blog/2020/08/01/
https://habr.com/ru/post/150950/

Стандарты

https://www.gnu.org/prep/standards/standards.html#Command_002dLine-Interfaces
https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html

Реализация разбора опций

Питон

https://docs.python.org/3/library/argparse.html#module-argparse
https://click.palletsprojects.com/en/7.x/
