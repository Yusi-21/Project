# Практическое занятие №3. Конфигурационные языки  
## Введение

В рамках данного занятия было изучено понятие программируемых конфигурационных языков, таких как **Jsonnet**, **Dhall** и **CUE**. Основное внимание уделялось принципам **DRY** (Don't Repeat Yourself) и **программируемости**, которые позволяют эффективно управлять конфигурациями.

## Задачи

### Задача 1

Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

#### Исходный JSON:

```
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    {
      "age": 23,
      "group": "ИКБО-63-23",
      "name": "Абдырахманов Ю."
    }
  ],
  "subject": "Конфигурационное управление"
}

```
#### Реализация:
```
// Функция для создания группы
local group(name) = name;

// Функция для создания студента
local student(age, groupName, name) = {
  age: age,
  group: groupName,
  name: name,
};

// Используем функции для создания данных
{
  groups: [
    group("ИКБО-1-20"),
    group("ИКБО-2-20"),
    group("ИКБО-3-20"),
    group("ИКБО-4-20"),
    group("ИКБО-5-20"),
    group("ИКБО-6-20"),
    group("ИКБО-7-20"),
    group("ИКБО-8-20"),
    group("ИКБО-9-20"),
    group("ИКБО-10-20"),
    group("ИКБО-11-20"),
    group("ИКБО-12-20"),
    group("ИКБО-13-20"),
    group("ИКБО-14-20"),
    group("ИКБО-15-20"),
    group("ИКБО-16-20"),
    group("ИКБО-17-20"),
    group("ИКБО-18-20"),
    group("ИКБО-19-20"),
    group("ИКБО-20-20"),
    group("ИКБО-21-20"),
    group("ИКБО-22-20"),
    group("ИКБО-23-20"),
    group("ИКБО-24-20"),
  ],
  students: [
    student(19, "ИКБО-4-20", "Иванов И.И."),
    student(18, "ИКБО-5-20", "Петров П.П."),
    student(18, "ИКБО-5-20", "Сидоров С.С."),
    student(23, "ИКБО-63-23", "Абдырахманов Ю."),
  ],
  subject: "Конфигурационное управление",
}
```
![image](https://github.com/user-attachments/assets/bb0a770f-3d62-47a5-af50-a5a071a49f25)

## Задача 2

Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
```
let Group = List Text

let Student = { age : Natural, group : Text, name : Text }

let groups : Group =
      [ "ИКБО-1-20"
      , "ИКБО-2-20"
      , "ИКБО-3-20"
      , "ИКБО-4-20"
      , "ИКБО-5-20"
      , "ИКБО-6-20"
      , "ИКБО-7-20"
      , "ИКБО-8-20"
      , "ИКБО-9-20"
      , "ИКБО-10-20"
      , "ИКБО-11-20"
      , "ИКБО-12-20"
      , "ИКБО-13-20"
      , "ИКБО-14-20"
      , "ИКБО-15-20"
      , "ИКБО-16-20"
      , "ИКБО-17-20"
      , "ИКБО-18-20"
      , "ИКБО-19-20"
      , "ИКБО-20-20"
      , "ИКБО-21-20"
      , "ИКБО-22-20"
      , "ИКБО-23-20"
      , "ИКБО-24-20"
      ]

let students : List Student =
    [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }
    , { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }
    , { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." }
    , { age = 23, group = "ИКБО-63-23", name = "Абдырахманов Ю." }
    ]

in
  { groups = groups
  , students = students
  , subject = "Конфигурационное управление"
  }
```
```
groups:
  - "ИКБО-1-20"
  - "ИКБО-2-20"
  - "ИКБО-3-20"
  - "ИКБО-4-20"
  - "ИКБО-5-20"
  - "ИКБО-6-20"
  - "ИКБО-7-20"
  - "ИКБО-8-20"
  - "ИКБО-9-20"
  - "ИКБО-10-20"
  - "ИКБО-11-20"
  - "ИКБО-12-20"
  - "ИКБО-13-20"
  - "ИКБО-14-20"
  - "ИКБО-15-20"
  - "ИКБО-16-20"
  - "ИКБО-17-20"
  - "ИКБО-18-20"
  - "ИКБО-19-20"
  - "ИКБО-20-20"
  - "ИКБО-21-20"
  - "ИКБО-22-20"
  - "ИКБО-23-20"
  - "ИКБО-24-20"
students:
  - age: 19
    group: "ИКБО-4-20"
    name: "Иванов И.И."
  - age: 18
    group: "ИКБО-5-20"
    name: "Петров П.П."
  - age: 18
    group: "ИКБО-5-20"
    name: "Сидоров С.С."
  - age: 23
    group: "ИКБО-63-23"
    name: "Абдырахманов Ю."
subject: "Конфигурационное управление"
```
![image](https://github.com/user-attachments/assets/0bae48b4-e458-4c85-9c2d-0b0c5179f79c)
## Задача 3

Язык нулей и единиц.

```
import random
def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
S = A | B | C | D 
A = 1 | 1 A | 0 B
B = 1 | 0 B
C = 1 1
D = 1 1 0 1
'''

for i in range(5):
    print(generate_phrase(parse_bnf(BNF), 'S'))   
```

![image](https://github.com/user-attachments/assets/9b56953c-26b4-4d7a-b194-eba375309ddb)

## Задача 4

Язык правильно расставленных скобок двух видов.
```
import random
def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
S = A | B | C
A = ( S ) | { S } | 俄国
B = ( A ) | { A }
C = 俄国
'''

for i in range(7):
    print(generate_phrase(parse_bnf(BNF), 'S'))

```
![image](https://github.com/user-attachments/assets/beb8a4f2-eb08-49af-8441-26450eda7da4)

## Задача 5

Язык выражений алгебры логики.
```
import random
def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
S = E
E = E & U | E | U
U = U | F | ~U | ( E )
F = x | y
'''

for i in range(5):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```
![image](https://github.com/user-attachments/assets/8545f865-b7a6-4ea5-83ef-dadeeaf750f3)

