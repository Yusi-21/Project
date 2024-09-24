# Практическое занятие №2. Менеджеры пакетов

## Задача 1

Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
```
Перейдите по ссылке: ( https://colab.research.google.com/drive/1ln_HcwTevZzH7YP-3arso7VB9aZ2KeYT?usp=sharing )

или в файле "practice_2_1.ipynb"  можете посмотреть!
```

## Задача 2

Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
```
Перейдите по ссылке: ( https://colab.research.google.com/drive/1JjhOhyg7dR0Imfa37TL1LETGwrp-2aog?usp=sharing )

или в файле "practice_2_2.ipynb"  можете посмотреть!
```

## Задача 3

Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

## Задача 4

**Следующие задачи можно решать с помощью инструментов на выбор:**

* Решатель задачи удовлетворения ограничениям (MiniZinc).
* SAT-решатель (MiniSAT).
* SMT-решатель (Z3).

Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

```
include "globals.mzn";  % Подключение глобальных функций

% Определяем 3 переменные для цифр билета
var 0..9: x1;  % Первая цифра
var 0..9: x2;  % Вторая цифра
var 0..9: x3;  % Третья цифра

% Ограничение на уникальные цифры
constraint all_different([x1, x2, x3]);

% Ограничение на сумму цифр
constraint x1 + x2 + x3 = 3;

% Определяем вывод
output ["x1 = \(x1), x2 = \(x2), x3 = \(x3)"];

% Минимизация суммы цифр
solve minimize (x1 + x2 + x3);

```

```

￼
Running happy_ticket.mzn
675msec

x1 = 2, x2 = 1, x3 = 0
----------
==========
Finished in 675msec.

![](https://github.com/Yusi-21/Project/blob/main/Practice/happy_ticket.jpg)

```


```
Решено при помощи Google Colab-a можете посмотреть по ссылке:
https://colab.research.google.com/drive/1dsWc_5G_EjEpP0mY9WHzTEv4ww6xwDaZ?usp=sharing
```
```
# Создаем переменные
x1 = Int('x1')
x2 = Int('x2')
x3 = Int('x3')

# Создаем решатель
solver = Solver()

# Ограничение: цифры должны быть от 0 до 9
solver.add(And(x1 >= 0, x1 <= 9))
solver.add(And(x2 >= 0, x2 <= 9))
solver.add(And(x3 >= 0, x3 <= 9))

# Ограничение: все цифры должны быть различными
solver.add(Distinct(x1, x2, x3))

# Ограничение: сумма трех цифр равна 3
solver.add(x1 + x2 + x3 == 3)

# Решение задачи
if solver.check() == sat:
    model = solver.model()
    print(f"Решение: x1 = {model[x1]}, x2 = {model[x2]}, x3 = {model[x3]}")
else:
    print("Решений нет")
```

```
Collecting z3-solver
  Downloading z3_solver-4.13.0.0-py2.py3-none-manylinux2014_x86_64.whl.metadata (757 bytes)
Downloading z3_solver-4.13.0.0-py2.py3-none-manylinux2014_x86_64.whl (57.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.3/57.3 MB 9.6 MB/s eta 0:00:00
Installing collected packages: z3-solver
Successfully installed z3-solver-4.13.0.0
Решение: x1 = 2, x2 = 0, x3 = 1
```
## Задача 5

Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![](images/pubgrub.png)

## Задача 6

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

## Задача 7

Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

## Полезные ссылки

Semver: https://devhints.io/semver

Удовлетворение ограничений и программирование в ограничениях: http://intsys.msu.ru/magazine/archive/v15(1-4)/shcherbina-053-170.pdf

Скачать MiniZinc: https://www.minizinc.org/software.html

Документация на MiniZinc: https://www.minizinc.org/doc-2.5.5/en/part_2_tutorial.html

Задача о счастливых билетах: https://ru.wikipedia.org/wiki/%D0%A1%D1%87%D0%B0%D1%81%D1%82%D0%BB%D0%B8%D0%B2%D1%8B%D0%B9_%D0%B1%D0%B8%D0%BB%D0%B5%D1%82
