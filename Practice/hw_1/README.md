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
![git02](https://github.com/user-attachments/assets/54e6a045-8d8a-4fbc-b0a0-02adfd662821)

![git03](https://github.com/user-attachments/assets/58cfaf41-18d8-402d-a7d9-5b97bfa3759c)

## Структура проекта
```
app.log # логи проекта
config.xml # конфиг для эмулятора
core.py # ядро эмулятора
generate_vfs.py # генерирует виртуальное пространство
```
