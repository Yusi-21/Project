# Практическое занятие №1. Введение, основы работы в командной строке
## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
```
grep '.*' /etc/passwd | cut -d: -f1 | sort
```
![Notes_240927_130748_4ce](https://github.com/user-attachments/assets/22dbdb0c-df89-4def-b912-1cd949d0cfcc)

## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 7 наибольших портов, как показано в примере ниже:
```
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 7
```

![Notes_240927_130810_95f](https://github.com/user-attachments/assets/83b11b05-763a-4f54-928f-f89c09f505ca)

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
![Notes_240927_130826_b4c](https://github.com/user-attachments/assets/bebb87de-8998-471f-ba2e-15da235bebe3)

## Задача 4

Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).
```
#!/bin/bash

file="$1"

id=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)

grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | grep -vE '\b(int|void|return|if|else|for|while|include|stdio.h)\b' | sort | uniq 
```
![Notes_240927_130840_41f](https://github.com/user-attachments/assets/a42de18c-27e7-48e6-ac0d-ad497a0910b3)

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
![Notes_240927_130856_5d9](https://github.com/user-attachments/assets/a6631ff6-9e45-4e64-a407-2f5c8ef7d694)

## Задача 6

Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.
```
#!/bin/bash

find . -type f \( -name "*.c" -o -name "*.js" -o -name "*.py" \) | while read -r file; do
    first_line=$(head -n 1 "$file")

    if [[ $first_line == http*://* ]]; then
        echo "Links found in file $file: $first_line"
    else
        echo "Links not found in file $file"
    fi
done
```
![Notes_240927_130926_c6f](https://github.com/user-attachments/assets/bea575c2-f1d7-4272-9380-1cd21fdf704e)

## Задача 7

Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).
```
#!/bin/bash

tree

touch file_dup.txt
mkdir folder
cp file_dup.txt folder
find . -type f -iname "*_dup.txt"
```

![Notes_240927_130956_97f](https://github.com/user-attachments/assets/6586840a-dcce-4336-89bf-605e1e806635)

## Задача 8

Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.
```
#!/bin/bash

touch file1.py file2.py file3.py
tree

find . -type f -iname "*.py"

mkdir folder
mv file1.py file2.py file3.py folder
tree

cd folder
bzip2 file1.py file2.py file3.py

ls -l
```
![IMG_20240927_133622_921](https://github.com/user-attachments/assets/826e2580-b35b-43ad-b321-6aabc26c156d)


## Задача 9

Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.
```
#!/bin/bash

echo -e "RTU\tMIREA\t-THE\tBEST\tUNIVERSITY"
```

![Notes_240927_131018_351](https://github.com/user-attachments/assets/710567e5-0e1b-4789-82ae-474871e7371e)


