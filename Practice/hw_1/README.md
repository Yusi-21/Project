## Задание №1
![image](https://github.com/user-attachments/assets/26f62591-f510-4c0b-8575-dfce571d4c0e)

## Клонирование репозитория
Склонируйте репозиторий с исходным кодом и тестами:
```
git clone https://github.com/Yusi-21/Project.git
cd Project
```
![git01](https://github.com/user-attachments/assets/dbec465a-8be2-4524-8e5f-718152951743)

## Установка зависимостей 
Активириуем виртуальное окружение
```
# Активировал виртуальное окружение
python -m venv venv
# Для Windows:
venv\Scripts\activate
```
![git01](https://github.com/user-attachments/assets/dbec465a-8be2-4524-8e5f-718152951743)

## Запуск
Запуск эмулятора
```
python core.py
```
![image](https://github.com/user-attachments/assets/56f02892-b8f4-47c6-a0c2-11db271061e5)

## Структура проекта
```
tests
 - tests.py # тесты
app.log # логи проекта
config.xml # конфиг для эмулятора
core.py # ядро эмулятора
generate_vfs.py # генерирует виртуальное пространство
```

## Запуск тестов
```
python -m tests.tests
```
![image](https://github.com/user-attachments/assets/d1a5c96c-122e-488f-827d-fda3d6000361)
