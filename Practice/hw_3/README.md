## Задача №3

![hw3+](https://github.com/user-attachments/assets/d122441e-444a-409f-839c-d5b0a896edff)

### Установка

Убедитесь, что у вас установлена версия Python 3.7 или выше.

1. Клонируйте этот репозиторий:

    ```bash
    git clone https://github.com/Yusi-21/Project
    cd Project
    ```
    
#### Пример

Для `JSON` файла следующего вида:

```json
[
    {
        "var": {
            "Pi": 3.14159,
            "Radius": 5
        }
    },
    {
        "Circle": {
            "Area": {
                "expr": "Pi * Radius * Radius"
            },
            "Circumference": {
                "expr": "2 * Pi * Radius"
            }
        }
    },
    {
        "Calculations": [
            {
                "Description": "Absolute value of -10",
                "Result": {
                    "expr": "abs(-10)"
                }
            },
            {
                "Description": "Modulo of 10 % 3",
                "Result": {
                    "expr": "mod(10, 3)"
                }
            }
        ]
    }
]

```

Запуск команды:

```bash
python C:\Users\user\PycharmProjects\pythonProject\hw_3\config_transformer.py -o output.conf < C:\Users\user\PycharmProjects\pythonProject\hw_3\examples\math_constants.json
```

Вернет результат:

```plaintext
var Pi := 3.14159;
var Radius := 5;
{
    Circle => {
        Area => 78.53975,
        Circumference => 31.4159
    }
}
{
    Calculations => '( {
        Description => "Absolute value of -10",
        Result => 10
    } {
        Description => "Modulo of 10 % 3",
        Result => 1
    } )
}

```
![output-math](https://github.com/user-attachments/assets/2acd30c5-de89-44c0-84df-e8eb05042a72)

## Тестирование

Этот проект использует `pytest` для тестирования. Чтобы запустить тесты:

1. Установите `pytest`, если у вас его еще нет:

    ```bash
    pip install pytest
    ```

2. Запустите тесты:

    ```bash
    pytest test_config_transformer.py
    ```

Вывод:
![test3](https://github.com/user-attachments/assets/637dbeaf-7779-477a-a336-d038f59ae47e)

## Примеры конфигураций

Ниже приведены примеры конфигураций JSON из разных предметных областей, которые можно использовать с этим инструментом.

### Конфигурация веб-сервера

**Входной JSON:**

```json
[
    {
        "var": {
            "DefaultPort": 8080
        }
    },
    {
        "Server": {
            "Port": {
                "expr": "DefaultPort + 1"
            },
            "Host": "localhost",
            "SSL": {
                "Enabled": false,
                "Certificate": null
            },
            "Endpoints": [
                {
                    "Path": "/api",
                    "Methods": ["GET", "POST"],
                    "AuthRequired": true
                },
                {
                    "Path": "/health",
                    "Methods": ["GET"],
                    "AuthRequired": false
                }
            ]
        }
    }
]

```

**Конвертированный вывод:**

```plaintext
var DefaultPort := 8080;
{
    Server => {
        Port => 8081,
        Host => localhost,
        SSL => {
            Enabled => False,
            Certificate => None
        },
        Endpoints => '( {
            Path => "/api",
            Methods => '( GET POST ),
            AuthRequired => True
        } {
            Path => "/health",
            Methods => '( GET ),
            AuthRequired => False
        } )
    }
}
```
![output-web](https://github.com/user-attachments/assets/3c5ab985-8595-4be5-b1f7-6abba423decd)

