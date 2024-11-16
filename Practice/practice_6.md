# Практическое задание №6. Системы автоматизации сборки

Работа с утилитой Make.

Изучить основы языка утилиты make. Распаковать в созданный каталог [make.zip](make.zip), если у вас в в системе нет make.

Создать приведенный ниже Makefile и проверить его работоспособность.

```
dress: trousers shoes jacket
    @echo "All done. Let's go outside!"

jacket: pullover
    @echo "Putting on jacket."

pullover: shirt
    @echo "Putting on pullover."

shirt:
    @echo "Putting on shirt."

trousers: underpants
    @echo "Putting on trousers."

underpants:
    @echo "Putting on underpants."

shoes: socks
    @echo "Putting on shoes."

socks: pullover
    @echo "Putting on socks."
```

Визуализировать файл [civgraph.txt](civgraph.txt).

## Задача 1

Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: [civgraph.json](civgraph.json).

Пример:

```
> make mathematics
mining
bronze_working
sailing
astrology
celestial_navigation
pottery
writing
code_of_laws
foreign_trade
currency
irrigation
masonry
early_empire
mysticism
drama_poetry
mathematics
```

## Решение:

```Python
import json

def parse_civgraph(civgraph_file):
    # Чтение JSON-файла
    with open(civgraph_file, 'r') as file:
        data = json.load(file)

    return data

def generate_makefile(data, output_file):
    with open(output_file, 'w') as file:
        for target, dependencies in data.items():
            # Формируем правило для Makefile
            dep_str = " ".join(dependencies) if dependencies else ""
            file.write(f"{target}: {dep_str}\n")
            file.write(f"\t@echo {target}\n\n")  # Простое действие для примера

def main():
    civgraph_file = "civgraph.json"  # Имя файла с графом зависимостей
    output_file = "Makefile"  # Имя итогового Makefile

    # Чтение данных из civgraph.json
    data = parse_civgraph(civgraph_file)

    # Генерация Makefile
    generate_makefile(data, output_file)
    print(f"Makefile был сгенерирован в {output_file}")

if __name__ == "__main__":
    main()
```

## Результат:

![image](https://github.com/user-attachments/assets/21070e62-e08a-4838-8556-5768d234efdd)

## Задача 2

Реализовать вариант трансляции, при котором повторный запуск make не выводит для civgraph на экран уже выполненные "задачи".

## Решение:

```Python
import json
import os

# Файл для сохранения завершенных задач
TASKS_FILE = "my_task2.txt"

# Загрузка списка завершенных задач из файла
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return set(f.read().splitlines())
    return set()

# Сохранение завершенных задач в файл
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        f.write('\n'.join(tasks))

# Загрузка графа зависимостей из JSON-файла
def load_dependency_graph(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при загрузке файла {filename}: {e}")
        return {}

# Функция генерации Makefile с проверкой на уже выполненные задачи
def generate_makefile(dependency_graph, target_task):
    visited_tasks = set()
    tasks_to_process = []
    completed_tasks = load_tasks()

    def process_task(task):
        if task in visited_tasks or task in completed_tasks:
            return
        visited_tasks.add(task)
        for dependency in dependency_graph.get(task, []):
            process_task(dependency)
        tasks_to_process.append(task)

    process_task(target_task)

    if not tasks_to_process:
        print("Все задачи уже были выполнены.")
    else:
        for task in tasks_to_process:
            if task not in completed_tasks:
                print(f"{task}")
                completed_tasks.add(task)

        save_tasks(completed_tasks)

if __name__ == '__main__':
    # Загружаем граф зависимостей из файла
    dependency_graph = load_dependency_graph('civgraph.json')

    if not dependency_graph:
        print("Не удалось загрузить граф зависимостей. Программа завершена.")
    else:
        target_task = input('>make ')
        generate_makefile(dependency_graph, target_task)
```

## Результат:

![image](https://github.com/user-attachments/assets/bf12a24a-0eee-4323-87dd-3962e712a543)

## Задача 3

Добавить цель clean, не забыв и про "животное".

## Решение:

```Python
import json
import os

# Файл для сохранения завершенных задач
TASKS_FILE = "my_task3.txt"

# Загрузка списка завершенных задач из файла
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return set(f.read().splitlines())
    return set()

# Сохранение завершенных задач в файл
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        f.write('\n'.join(tasks))

# Загрузка графа зависимостей из JSON-файла
def load_dependency_graph(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при загрузке файла {filename}: {e}")
        return {}

# Функция генерации Makefile с проверкой на уже выполненные задачи
def generate_makefile(dependency_graph, target_task):
    visited_tasks = set()
    tasks_to_process = []
    completed_tasks = load_tasks()

    def process_task(task):
        if task in visited_tasks or task in completed_tasks:
            return
        visited_tasks.add(task)
        for dependency in dependency_graph.get(task, []):
            process_task(dependency)
        tasks_to_process.append(task)

    process_task(target_task)

    if not tasks_to_process:
        print("Все задачи уже были выполнены.")
    else:
        for task in tasks_to_process:
            if task not in completed_tasks:
                print(f"{task}")
                completed_tasks.add(task)

        save_tasks(completed_tasks)

# Функция для очистки задач
def clean():
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)
        print(f"Файл с завершенными задачами {TASKS_FILE} удален.")
    else:
        print("Файл с завершенными задачами не найден. Нечего очищать.")

if __name__ == '__main__':
    # Загружаем граф зависимостей из файла
    dependency_graph = load_dependency_graph('civgraph.json')

    if not dependency_graph:
        print("Не удалось загрузить граф зависимостей. Программа завершена.")
    else:
        action = input('Выберите действие make/clean: ')

        if action == 'make':
            target_task = input('>make ')
            generate_makefile(dependency_graph, target_task)
        elif action == 'clean':
            clean()
        else:
            print("Неизвестное действие. Пожалуйста, введите 'build' или 'clean'.")
```

## Результат:

![image](https://github.com/user-attachments/assets/f859e2fe-f19e-4ee9-a5be-d00376455c34)

![image](https://github.com/user-attachments/assets/49079d27-9958-4f4a-be7c-c15d21957e0b)

## Задача 4

Написать makefile для следующего скрипта сборки:

```
gcc prog.c data.c -o prog
dir /B > files.lst
7z a distr.zip *.*
```

Вместо gcc можно использовать другой компилятор командной строки, но на вход ему должны подаваться два модуля: prog и data.
Если используете не Windows, то исправьте вызовы команд на их эквиваленты из вашей ОС.
В makefile должны быть, как минимум, следующие задачи: all, clean, archive.
Обязательно покажите на примере, что уже сделанные подзадачи у вас не перестраиваются.

## Решение:

```Makefile
# Компилятор и флаги
CC = gcc
CFLAGS = -o prog

# Исходные файлы
SRC = prog.c data.c
OUTPUT = prog
FILE_LIST = files.lst
ARCHIVE = distr.zip

# Основная цель
all: $(ARCHIVE)

# Компиляция программы
$(OUTPUT): $(SRC)
	$(CC) $(SRC) $(CFLAGS)

# Создание списка файлов
$(FILE_LIST): $(OUTPUT)
	dir /B > $(FILE_LIST)

# Создание архива
$(ARCHIVE): $(FILE_LIST)
	powershell Compress-Archive -Path *.* -DestinationPath $(ARCHIVE)

# Очистка
clean:
	del $(OUTPUT) $(FILE_LIST) $(ARCHIVE)

```

## Результат:

![image](https://github.com/user-attachments/assets/d89dfa66-74fb-4311-b8b3-771b143d6298)


## Полезные ссылки

Описание (рус.): https://unix1.jinr.ru/faq_guide/programming/make/make.html

Шпаргалка: https://devhints.io/makefile

Топологическая сортировка: https://ru.wikipedia.org/wiki/Топологическая_сортировка
