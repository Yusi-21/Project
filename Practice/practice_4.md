# Практическое задание №4. Системы контроля версий

Работа с Git.

## Задача 1

На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.
```
git commit
git tag IN
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout IN
```
![image](https://github.com/user-attachments/assets/8968d478-b217-4698-b42c-83cf5ed0727b)


## Задача 2

Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.

## Решение:

```bash
git init
git config user.name "coder1"
git config user.email "coder1@mirea.ru"
echo print("Hello, Mirea!") > prog.py
git add prog.py
git commit -m "first commit"
git status
git log
```

## Результат:

![image](https://github.com/user-attachments/assets/b410cda3-e148-445e-90bc-aa2026731712)

```bash
Microsoft Windows [Version 10.0.19045.5011]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\mygitrepo>git init
Initialized empty Git repository in C:/mygitrepo/.git/

C:\mygitrepo>git config user.name "coder1"

C:\mygitrepo>git config user.email "coder1@mirea.ru"

C:\mygitrepo>echo print("Hello, Mirea!") > prog.py

C:\mygitrepo>git add prog.py

C:\mygitrepo>git commit -m "first commit"
[master (root-commit) 44ef337] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py

C:\mygitrepo>git status
On branch master
nothing to commit, working tree clean

C:\mygitrepo>git log
commit 44ef3379e63cd30e4f05b6023b2e07a6a15d7fa3 (HEAD -> master)
Author: coder1 <coder1@mirea.ru>
Date:   Thu Nov 7 15:04:14 2024 +0300

    first commit

C:\mygitrepo>
```

## Задача 3

Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.

Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.

Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.

Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.

Прислать список набранных команд и содержимое git log.

Пример лога коммитов:

```bash
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Sun Oct 11 11:27:09 2020 +0300
| | 
| |     readme fix
| | 
| * commit d731ba84014d603384cc3287a8ea9062dbb92303
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Sun Oct 11 11:22:52 2020 +0300
| | 
| |     coder 1 info
| | 
* | commit 48ce28336e6b3b983cbd6323500af8ec598626f1
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Sun Oct 11 11:24:00 2020 +0300
|   
|       coder 2 info
| 
* commit ba9dfe9cb24316694808a347e8c36f8383d81bbe
| Author: Coder 2 <coder2@corp.com>
| Date:   Sun Oct 11 11:21:26 2020 +0300
| 
|     docs
| 
* commit 227d84c89e60e09eebbce6c0b94b41004a4541a4
  Author: Coder 1 <coder1@corp.com>
  Date:   Sun Oct 11 11:11:46 2020 +0300
  
      first commit
```

## Решение:

```bash
git init
git config user.name "coder1"
git config user.email "coder1@mirea.ru"
echo print("Hello, Mirea!") > prog.py
git add prog.py
git commit -m "first commit"
git status
git log

cd D:\mygitrepo
git init --bare server

git remote add server D:\mygitrepo\server
git remote -v

git push server master

git clone D:\mygitrepo\server D:\mygitrepo\client
cd D:\mygitrepo\client
git config user.name "coder2"
git config user.email "coder2@mirea.ru"

echo "Author Information:" > readme.md
git add readme.md
git commit -m "docs"

git remote rename origin server

git push server master

cd D:\mygitrepo
git pull server master

echo "Author: coder1" >> readme.md
git add readme.md
git commit -m "coder1 info"
git push server master

cd D:\mygitrepo\client
echo "Author: coder2" >> readme.md
git add readme.md
git commit -m "coder2 info"
git push server master

git pull server master

git add readme.md
git commit -m "readme fix"
git push server master

cd ..
cd server
git log -n 5 --graph --decorate --all
```

## Результат:

![image](https://github.com/user-attachments/assets/60d7ffaf-f1e5-433c-a1b4-66b0f49d1f8f)

![image](https://github.com/user-attachments/assets/8a33789a-5367-40a9-be64-922c2d083da0)

![image](https://github.com/user-attachments/assets/8427230a-a91f-40d7-8292-d6450180827d)

![image](https://github.com/user-attachments/assets/11b0ad91-a9d6-4885-a3e1-efa510addc7c)

```bash
C:\mygitrepo\server>git log -n 5 --graph --decorate --all
*   commit 0144a7a9873b5dbbe1c1116d094b3a8ee53fb81b (HEAD -> master)
|\  Merge: 1c6d5a4 65523b9
| | Author: coder2 <coder2@mirea.ru>
| | Date:   Thu Nov 7 15:24:20 2024 +0300
| |
| |     readme fix
| |
| * commit 65523b9d3feb31031eba117fd82076704db8cc60
| | Author: coder1 <coder1@mirea.ru>
| | Date:   Thu Nov 7 15:20:47 2024 +0300
| |
| |     coder1 info
| |
* | commit 1c6d5a465c39ad35407482b7759235cff6885902
|/  Author: coder2 <coder2@mirea.ru>
|   Date:   Thu Nov 7 15:22:36 2024 +0300
|
|       coder2 info
|
* commit 3f778482c576ef449cfac571c21ddeb620af5817
| Author: coder2 <coder2@mirea.ru>
| Date:   Thu Nov 7 15:17:50 2024 +0300
|
|     docs
|
* commit 44ef3379e63cd30e4f05b6023b2e07a6a15d7fa3
  Author: coder1 <coder1@mirea.ru>
  Date:   Thu Nov 7 15:04:14 2024 +0300

      first commit

D:\mygitrepo\server>
```

## Задача 4

Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.

## Решение:

```python
import subprocess


def get_git_objects():
    # Получаем список всех объектов в репозитории
    try:
        # Выполняем команду 'git rev-list --all' для получения всех хешей коммитов
        commits = subprocess.check_output(['git', 'rev-list', '--all']).decode('utf-8').splitlines()

        # Для каждого коммита получаем содержимое объекта
        for commit in commits:
            print(f'Contents of commit {commit}:')
            try:
                # Используем 'git cat-file -p' для получения содержимого
                content = subprocess.check_output(['git', 'cat-file', '-p', commit]).decode('utf-8')
                print(content)
            except subprocess.CalledProcessError as e:
                print(f'Error retrieving object {commit}: {e}')
            print('-' * 40)
    except subprocess.CalledProcessError as e:
        print(f'Error retrieving commits: {e}')


if __name__ == '__main__':
    get_git_objects()
```

## Результат:

![image](https://github.com/user-attachments/assets/21287f60-70b6-4672-8118-5e17b039a7ec)

