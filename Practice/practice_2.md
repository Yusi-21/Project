## Задача №1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

### Решение. 1 часть.
``` pip show matplotlib ```

### Результат.
![image](https://github.com/user-attachments/assets/6468ef21-cc3d-4969-ada7-575d2f355f97)

### Решение. 2 часть.

Чтобы получить пакет matplotlib без использования менеджера пакетов, мы можем скачать его напрямую из репозитория.

` git clone https://github.com/matplotlib/matplotlib.git ` - создает локальную копию репозитория на компьютере.

` cd matplotlib ` - переход в директорию пакета

` python setup.py install ` - установка matplotlib


## Задача №2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

### Решение. Часть 1.
Чтобы вывести служебную информацию о пакете express (после того, как были установлены Node.js и npm), нужно ввести следующую команду:

``` npm show express ```

### Результат.

![image](https://github.com/user-attachments/assets/567dadb4-8b38-4310-9a78-d0f42c1bd28c)

### Решение. Часть 2.
Чтобы получить пакет прямо из репозитория без использования менеджера пакетов, нужно клонировать репозиторий вручную.

``` git clone https://github.com/expressjs/express.git ``` - клонирование репозитория

``` cd express ``` - переход в нужную нам папку

В репозитории есть файл package.json, который содержит информацию о зависимостях, необходимых для работы пакета. Эти зависимости можно скачать и подключить вручную:
для этого надо найти зависимости в разделе "dependencies" файла package.json.
Надо загрузить необходимые библиотеки напрямую из их репозиториев или сайтов и добавить их в проект. Также можно использовать npm.

## Задача №3
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.
```bash
pipdeptree --packages matplotlib --graph-output dot > matplotlib_deps.dot
```
### Результат.

<img width="717" alt="expressgraph" src="https://github.com/user-attachments/assets/1de174ba-4c2a-4b26-a2f9-99b54d15b807">

<img width="719" alt="matplotlibgraph" src="https://github.com/user-attachments/assets/56ee71f5-2b9c-4323-84bf-3b03acea6267">

## Задача №4
Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.
Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

### Решение.
Я ознакомился с основами синтаксиса MiniZink.

Решение задачи о счастливых билетах:
```
include "globals.mzn";

% Определение переменных
array[1..6] of var 0..9: digits; % Цифры билета

% Ограничение на уникальность цифр
constraint all_different(digits);

% Ограничение на сумму первых и последних трех цифр
constraint sum(digits[1..3]) = sum(digits[4..6]);

% Минимизация суммы первых трех цифр
var int: sum_first_three = sum(digits[1..3]);
solve minimize sum_first_three;

% Печать решения
output [
    "Digits: ", show(digits), "\n",
    "Sum of first three digits: ", show(sum_first_three), "\n"
];

 ```

### Результат.

![image](https://github.com/user-attachments/assets/c19b5820-d3d2-43d5-bd03-07c3a0553bb0)

## Задача №5
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже (рисунок можно найти в методичке).

### Решение.

```
include "globals.mzn";

% Определяем версии пакетов
enum Version = {v1_0_0, v1_1_0, v1_2_0, v1_3_0, v1_4_0, v1_5_0, v1_8_0, v2_0_0, v2_1_0, v2_2_0, v2_3_0};

% Определяем пакеты
enum Package = {root, menu, dropdown, icons};

% Зависимости пакетов
array[Package] of set of Version: dependencies = [
    {v1_0_0, v1_1_0, v1_2_0, v1_3_0, v1_4_0, v1_5_0},  % menu
    {v1_8_0, v2_0_0, v2_1_0, v2_2_0, v2_3_0},  % dropdown
    {v1_0_0, v2_0_0},  % icons
    {}  % root (оставляем пустым, так как не определено)
];

% Переменные для версий пакетов
array[Package] of var Version: versions;

% Пример ограничения: root зависит от menu версии 1.5.0
constraint versions[root] in dependencies[menu];

% Установка значений для переменных
constraint versions[menu] = v1_0_0;  % Задаем конкретную версию для menu
constraint versions[dropdown] = v1_8_0;  % Задаем конкретную версию для dropdown
constraint versions[icons] = v1_0_0;  % Задаем конкретную версию для icons

solve satisfy;

% Вывод значений
output [
    "root = ", show(versions[root]), "\n",
    "menu = ", show(versions[menu]), "\n",
    "dropdown = ", show(versions[dropdown]), "\n",
    "icons = ", show(versions[icons]), "\n"
];

 ```

### Результат.

![image](https://github.com/user-attachments/assets/fb66f0e9-00b2-4310-b9fa-f8cf1036a45d)

## Задача №6
Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:
```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```

### Решение.

```
include "globals.mzn";

% Определяем версии пакетов
enum Version = {v1_0_0, v1_1_0, v2_0_0};

% Определяем пакеты
enum Package = {root, foo, left, right, shared, target};

% Зависимости пакетов
array[Package] of set of Version: dependencies = [
    {v1_0_0},          % root
    {v1_0_0, v1_1_0},  % foo
    {v1_0_0},          % left
    {v1_0_0},          % right
    {v1_0_0, v2_0_0},  % shared
    {v2_0_0}           % target
];

% Переменные для версий пакетов
array[Package] of var Version: versions;

% Ограничения
constraint versions[root] in dependencies[foo];   % root зависит от foo
constraint versions[foo] in dependencies[left];    % foo зависит от left
constraint versions[foo] in dependencies[right];   % foo зависит от right
constraint versions[left] in dependencies[shared];  % left зависит от shared
constraint versions[right] in dependencies[shared]; % right зависит от shared
constraint versions[shared] in dependencies[target]; % shared зависит от target

% solve
solve satisfy;

% Вывод значений
output [
    "root = ", show(versions[root]), "\n",
    "foo = ", show(versions[foo]), "\n",
    "left = ", show(versions[left]), "\n",
    "right = ", show(versions[right]), "\n",
    "shared = ", show(versions[shared]), "\n",
    "target = ", show(versions[target]), "\n"
];

 ```

### Результат.

![image](https://github.com/user-attachments/assets/a5820de2-f94c-47d7-87e0-24836eaf2b80)

## Задача №7
Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

### Решение.
Для того чтобы представить задачу о зависимостях пакетов в более общем виде, можно использовать структуру данных, такую как словарь в питоне, которая будет содержать метаданные о пакетах и их зависимостях.

Пакет: имя пакета, версии пакета, зависимости (другие пакеты и их версии)
Зависимости: зависимости могут быть описаны как список кортежей, где каждый кортеж содержит название зависимого пакета и его необходимую версию.

Я сделал такую структуру (ниже):
```
packages = {
    "root": {
        "versions": ["1.0.0"],
        "dependencies": [("foo", "1.0.0"), ("target", "2.0.0")]
    },
    "foo": {
        "versions": ["1.0.0", "1.1.0"],
        "dependencies": [("left", "1.0.0"), ("right", "1.0.0")]
    },
    "left": {
        "versions": ["1.0.0"],
        "dependencies": [("shared", ">=1.0.0")]
    },
    "right": {
        "versions": ["1.0.0"],
        "dependencies": [("shared", "<2.0.0")]
    },
    "shared": {
        "versions": ["1.0.0", "2.0.0"],
        "dependencies": [("target", "1.0.0")]  # shared 1.0.0 зависит от target ^1.0.0
    },
    "target": {
        "versions": ["1.0.0", "2.0.0"],
        "dependencies": []
    }
}

 ```
А также функция для проверки зависимостей:

```
def check_dependencies(package_name):
    package = packages[package_name]
    for dependency, version in package["dependencies"]:
        if dependency not in packages:
            return f"Package {dependency} not found."
        
        # Проверяем, соответствует ли версия зависимостям
        if version.startswith(">="):
            min_version = version[2:]
            if not any(v >= min_version for v in packages[dependency]["versions"]):
                return f"Dependency {dependency} does not meet the version requirement."
        elif version.startswith("<"):
            max_version = version[1:]
            if not any(v < max_version for v in packages[dependency]["versions"]):
                return f"Dependency {dependency} does not meet the version requirement."
        else:
            if version not in packages[dependency]["versions"]:
                return f"Dependency {dependency} version {version} not found."

    return f"All dependencies for {package_name} are satisfied."

# Проверка зависимостей для пакета 'root'
print(check_dependencies("root"))

```

### Результат.
```
All dependencies for root are satisfied.
````










# Практическое занятие №2. Менеджеры пакетов

## Задача 7

Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

