# Задание №4

![hw4+](https://github.com/user-attachments/assets/7ace307d-29a8-401f-8440-ffb3ef02a50e)
#

# Учебная Виртуальная Машина (УВМ): Ассемблер и Интерпретатор

## Описание проекта

Этот проект реализует учебную виртуальную машину (УВМ), ассемблер и интерпретатор для работы с системой команд УВМ. Виртуальная машина предназначена для выполнения низкоуровневых операций с регистрами и памятью на основе заданного набора команд. Ассемблер позволяет преобразовывать текстовые программы на языке ассемблера в бинарный код, который затем может быть исполнен интерпретатором.

### Основные компоненты:
1. **Ассемблер** (`assembler.py`) — переводит текстовую программу в бинарный код.
2. **Интерпретатор** (`interpreter.py`) — выполняет бинарный код, изменяет состояние регистров и памяти.
3. **Тесты** (`test_assembler.py` и `test_interpreter.py`) — проверяют работу ассемблера и интерпретатора.
4. **Тестовая программа** (`test_program.asm`) — пример программы, которая выполняет поэлементно операцию popcnt() над вектором длины 4 и результаты записывает в исходном векторе.

## Как запустить проект

### 1. Ассемблирование программы

Для ассемблирования программы на ассемблере используйте следующий код:

```bash
python C:\Users\user\PycharmProjects\pythonProject\hw_4\assembler.py -i C:\Users\user\PycharmProjects\pythonProject\hw_4\test_program.asm -o test_program.bin -l test_program_log.csv
```

Это преобразует файл `test_program.asm` в бинарный файл `test_program.bin` и создаст лог-файл `test_program_log.csv`.

![assembler-zapusk](https://github.com/user-attachments/assets/a279522f-dfd8-41f6-93b5-46055e446ce6)

### 2. Интерпретирование программы

Чтобы итнерпретировать программу, используйте следующий код:

```bash
python C:\Users\user\PycharmProjects\pythonProject\hw_4\interpreter.py -i C:\Users\user\PycharmProjects\pythonProject\hw_4\test_program.bin -o C:\Users\user\PycharmProjects\pythonProject\hw_4\test_program_result.csv -s 1000 -e 1003
```

Это исполнит бинарный код и создаст файл результата `test_program_result.csv`, где будет содержаться результат `popcnt()`.

![interpreter-zapusk](https://github.com/user-attachments/assets/71391a6d-58b7-4d4f-bef7-770e4d77c4ce)

### 3. Тестирование

Запустите тесты для проверки правильности работы:

```bash
pytest test_assembler.py
```
![test-assembler](https://github.com/user-attachments/assets/3e946410-4f02-4872-9a83-66ace8ae49e3)


```bash
pytest test_interpreter.py
```
![test-interpreter1](https://github.com/user-attachments/assets/202c10d2-eab3-441e-95e1-56faee4db027)

![test-interpreter2](https://github.com/user-attachments/assets/457dfa98-dfc5-4bc8-82ca-d9cdf7f47f27)

Все тесты должны завершиться успешно.

## Ожидаемый результат

После выполнения тестовой программы (`test_program.asm`), исходный вектор (по адресам памяти с 1000 по 1003) будет содержать:

- Memory initialized: {1000: 5, 1001: 15, 1002: 256, 1003: 7}
    PC: 0, Code size: 29
- LOAD_CONST executed: accumulator set to 1000
    PC: 5, Code size: 29
- POP_CNT executed: operand at 1000 is 5, popcnt=2, stored at 1000
    PC: 11, Code size: 29
- POP_CNT executed: operand at 1001 is 15, popcnt=4, stored at 1001
    PC: 17, Code size: 29
- POP_CNT executed: operand at 1002 is 256, popcnt=1, stored at 1002
    PC: 23, Code size: 29
- POP_CNT executed: operand at 1003 is 7, popcnt=3, stored at 1003

![image](https://github.com/user-attachments/assets/7f147693-3d04-4454-b1d2-425958611c95)

## Структура проекта

- `assembler.py` — ассемблер, который преобразует текстовые программы в бинарный код.
- `interpreter.py` — интерпретатор, который исполняет бинарный код.
- `test_assembler.py` и `test_interpreter.py` — тесты, проверяющие корректность работы ассемблера и интерпретатора.
- `test_program.asm` — пример программы на ассемблере, выполняющий операцию `popcnt()`.


*********************

## Ожидаемый результат


- Элемент 0: `0` (250 != 247)
- Элемент 1: `1` (247 == 247)
- Элемент 2: `0` (123 != 247)
- Элемент 3: `1` (247 == 247)

