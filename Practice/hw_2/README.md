## Задание №2
![2+](https://github.com/user-attachments/assets/ed61ced6-dfeb-4ac9-9b0b-ae3287e43c39)

## Требования

- **Python 3.6+**
- **Git**, установленный и доступный в `PATH`.
- **Graphviz**, установленный и доступный в `PATH`.
- **pytest** для запуска тестов (опционально).

## Установка

1. **Клонируйте репозиторий или скопируйте файлы проекта**:

   ```bash
   git clone https://github.com/Yusi-21/Project.git
   ```

2. **Перейдите в директорию проекта**:

   ```bash
   cd Project
   ```

3. **Установите необходимые зависимости** (если они не установлены):

   - **Установка Graphviz**:
     - **Windows**:

       - Скачайте и установите Graphviz с [официального сайта](https://graphviz.org/download/).
       - Добавьте путь к `dot.exe` в переменную окружения `PATH`.

   - **Установка `pytest`** (для запуска тестов):

     ```bash
     pip install pytest
     ```

## Использование

откройте `cmd` и запустите:

```bash
python C:\Users\user\PycharmProjects\pythonProject\hw_2\dependency_visualizer.py -p C:\Users\user\Graphviz\bin\dot -n curl -o curl_dependencies.dot -u http://archive.ubuntu.com/ubuntu/dists/focal/main/binary-amd64/
```

После успешного выполнения вы увидите `.dot` файл в папке, в которой вы работаете:

![image](https://github.com/user-attachments/assets/d036148e-0a57-45b1-9db0-4571494e5096)

## Результаты:

![2,1](https://github.com/user-attachments/assets/16d5967c-8ce6-4e94-9bd9-28612094a7b0)

![2,4](https://github.com/user-attachments/assets/24b784f8-4eab-4bb2-ab21-a75ef46c4921)

![2,5](https://github.com/user-attachments/assets/4f664fc3-3b08-42f4-bf52-26d3b59b2157)

## Тестирование

Чтобы запустить тесты и убедиться в корректной работе скрипта, выполните:

```bash
pytest -v test_dependency_visualizer.py
```

Вы должны увидеть вывод, подтверждающий успешное прохождение всех тестов.

![test](https://github.com/user-attachments/assets/477a5dce-01f7-424b-aa74-7bb296641f3b)

## Структура проекта

- **dependency_visualizer.py**: Основной скрипт для визуализации графа зависимостей.
- **test_dependency_visualizer.py**: Набор тестов для проверки корректности работы функций.
- **README.md**: Документация проекта.
