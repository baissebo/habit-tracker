В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер
полезных привычек.

Клонировать репозиторий: <https://github.com/baissebo/habit-tracker.git>

Создать зависимости из файла requirements.txt, выполнив команду `poetry add $(cat requirements.txt)`
или `poetry install`.

Заполнить свои данные в файл <.env> согласно списке из файла <env.sample>

Запустить Redis на ПК командой <redis-server>

Для запуска проекта наберите в терминале команду <python manage.py runserver>

Чтобы начать рассылку:

    В терминале запустите celery worker командой: <celery -A config worker -l INFO> (Для Windows: <celery -A config worker -l INFO -P eventlet>)

    В другом терминале запустите celery beat командой: <celery -A config beat -l info -S django>

Для запуска файла в Docker:

    Ввести команду в терминал: <docker-compose up -d --build>