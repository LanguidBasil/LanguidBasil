# Hi there ✨ I'm ...

![ascii art](./assets/ascii.gif)

## about me

> Under construction

## technologies

<img width="16px" src="./assets/python.svg" alt="python logo" /> Python <img width="16px" src="./assets/fastapi.svg" alt="fastapi logo" /> FastAPI <img width="16px" src="./assets/django.svg" alt="django logo" /> Django <img width="16px" src="./assets/sqlalchemy.svg" alt="sqlalchemy logo" /> SQLAlchemy <img width="16px" src="./assets/pandas.svg" alt="sqlalchemy logo" /> Pandas

<img width="16px" src="./assets/html.svg" alt="html logo" /> html <img width="16px" src="./assets/css.svg" alt="css logo" /> css <img width="16px" src="./assets/javascript.svg" alt="javascript logo" /> Javascript <img width="16px" src="./assets/react.svg" alt="react logo" /> React

<img width="16px" src="./assets/postgres.svg" alt="postgres logo" /> Postgres <img width="16px" src="./assets/redis.svg" alt="redis logo" /> Redis <img width="16px" src="./assets/mongodb.svg" alt="mongodb logo" /> MongoDB <img width="16px" src="./assets/sqlite.svg" alt="sqlite logo" /> SQLite

<img width="16px" src="./assets/docker.svg" alt="docker logo" /> Docker <img width="16px" src="./assets/gitlab.svg" alt="gitlab logo" /> Gitlab CI <img width="16px" src="./assets/github.svg" alt="github logo" /> Github CI

## contacts

<img width="16px" src="./assets/telegram.svg" alt="telegram logo" /> [telegram](https://t.me/emakunev)

<img width="16px" src="./assets/linkedin.svg" alt="linkedin logo" /> [LinkedIn](https://www.linkedin.com/in/eugene-makunev-b9682b233/)

<img width="16px" src="./assets/mail.svg" alt="mail logo" /> [Mail](mailto:e.makunev@gmail.com)

## achivements

```mermaid
flowchart TD
    classDef parent fill:#AA7DCE, stroke:#D2D0BA, color:#ffffff, font-size:12pt
    classDef child fill:#F4A5AE, stroke:#D2D0BA, color:#ffffff, font-size:8pt
    classDef graphstyle fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

    main(my life):::parent
    university(university 2020 / 2024):::parent
    university_graduate_work(graduate_work):::parent
    university_naruto(naruto):::parent
    paper_plane(paper_plane):::parent
    tomoru(tomoru):::parent
    softorium(softorium):::parent


    main --> university
    subgraph university_graph
        style university_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

        university --> university_1{{"Муравьиный алгоритм. Pascal"}}:::child
        university_1 --> university_2{{"Змейка на самописном ассемблере. Logisim"}}:::child
        university_2 --> university_3{{"Моделирование системы по обработке деталей и улучшение исопльзования ресурсов путем оптимизации различных факторов: вместимость стола, скорость обработки, количество рабочих и тп. C# + WinForms"}}:::child
        university_3 --> university_4{{"Реализация различных алгоритмов сортировки и их сравнение. C# + WinForms"}}:::child
        university_4 --> university_5{{"Моделирование сети предприятия. Cisco Packet Tracer"}}:::child
        university_5 --> university_6{{"API Limiter. Python + FastAPI + Redis"}}:::child
        university_6 --> university_7{{"Интернет магазин. OpenCart"}}:::child
    end

    university --> university_graduate_work
    subgraph university_graduate_work_graph
        style university_graduate_work_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

        university_graduate_work --> university_graduate_work_1{{"Проектирование и разработка human resource management system"}}:::child
        university_graduate_work_1 --> university_graduate_work_2{{"React + React Router (client side rendering and routing), Typescript, NPM, eslint"}}:::child
        university_graduate_work_2 --> university_graduate_work_3{{"Python + FastAPI + Postgres + Docker"}}:::child
    end

    university --> university_naruto
    subgraph university_naruto_graph
        style university_naruto_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

        university_naruto --> university_naruto_1{{"Телеграм бот для записи расходов с QR кода на чеке в гугл таблицу, с Machine Learning алгоритмом для определения категории товаров (еда, еда вкусная, одежда, транспорт и прочие)"}}:::child
        university_naruto_1 --> university_naruto_2{{"Включение файлов конфигурации и доступов в `.dockerignore` для избежания их попадания в docker image"}}:::child
        university_naruto_2 --> university_naruto_3{{"Python + FastAPI + sklearn (naive bayes classifier)"}}:::child
    end

    main --> paper_plane
    subgraph paper_plane_graph
        style paper_plane_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

        paper_plane --> paper_plane_1{{"Контроллер персонажей с детальной настройкой (двойной прыжок, время койота, время на набор и сброс максимальной скорости))"}}:::child
        paper_plane_1 --> paper_plane_2{{"Рандомная генерация уровней с пресетами объектов"}}:::child
        paper_plane_2 --> paper_plane_3{{"Создание уровней и импорт ассетов в Unity"}}:::child
        paper_plane_3 --> paper_plane_4{{"Шейдеры для подсвечивания зон интереса"}}:::child
        paper_plane_4 --> paper_plane_5{{"Искусственный Интеллект с системами патрулирования и боя по ролям"}}:::child
        paper_plane_5 --> paper_plane_6{{"Создание систем сохранений, диалогов, инвентаря, состояний"}}:::child
    end

    main --> tomoru
    subgraph tomoru_graph
        style tomoru_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt
        
        tomoru --> tomoru_graph_2023_04_1("tomoru 2022-06 / 2023-04"):::parent
        tomoru --> tomoru_graph_2023_05_1("tomoru 2023-04 / 2023-05"):::parent
        tomoru --> tomoru_graph_2023_06_1("tomoru 2023-05 / 2023-06"):::parent
        tomoru --> tomoru_graph_2023_07_1("tomoru 2023-06 / 2023-07"):::parent
        tomoru --> tomoru_graph_2023_08_1("tomoru 2023-07 / 2023-08"):::parent
        tomoru --> tomoru_graph_2023_09_1("tomoru 2023-08 / 2023-09"):::parent
        
        subgraph tomoru_graph_2023_04
            style tomoru_graph_2023_04 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_04_1 --> tomoru_graph_2023_04_2{{"Получение данных по API из сторонних сервисов, их обработка и запись в PostgreSQL, Google Spreadsheets и BigQuery"}}:::child
            tomoru_graph_2023_04_1 --> tomoru_graph_2023_04_2{{"Ускорение загрузки 5 гигабайт данных из AmoCRM API в 4 раза распределив ее на 4 celery worker'а"}}:::child
            tomoru_graph_2023_04_2 --> tomoru_graph_2023_04_3{{"Макрос для создания бекапов Google Spreadsheets"}}:::child
            tomoru_graph_2023_04_3 --> tomoru_graph_2023_04_4{{"Форма для добавления и обновления данных на платформе компании"}}:::child
            tomoru_graph_2023_04_4 --> tomoru_graph_2023_04_5{{"Чистка данных и улучшение их надежности"}}:::child
            tomoru_graph_2023_04_5 --> tomoru_graph_2023_04_6{{"Кеширование данных по вебхуку (Huntflow)"}}:::child
            tomoru_graph_2023_04_6 --> tomoru_graph_2023_04_7{{"Настройка интеграции между нашим сервисом, телеграмм ботом и CRM"}}:::child
            tomoru_graph_2023_04_7 --> tomoru_graph_2023_04_8{{"Телеграмм бот для генерации видео"}}:::child
            tomoru_graph_2023_04_8 --> tomoru_graph_2023_04_9{{"HR tinder"}}:::child
            tomoru_graph_2023_04_9 --> tomoru_graph_2023_04_10{{"Менторство Никиты"}}:::child
            tomoru_graph_2023_04_10 --> tomoru_graph_2023_04_11{{"Введение требований на оформление задач"}}:::child
            tomoru_graph_2023_04_11 --> tomoru_graph_2023_04_12{{"Введение code review"}}:::child
        end
        
        subgraph tomoru_graph_2023_05
            style tomoru_graph_2023_05 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_05_1 --> tomoru_graph_2023_05_2{{"Верификация телефона по СМС, аналитика HR"}}:::child
            tomoru_graph_2023_05_2 --> tomoru_graph_2023_05_3{{"Переделал схему данных с использованием Json схемы, для гибкости добавления новых этапов в воронке найма"}}:::child
            tomoru_graph_2023_05_3 --> tomoru_graph_2023_05_4{{"Создал конфиг файл для гугл таблиц для задания порядка и места выгрузки данных из бд"}}:::child
            tomoru_graph_2023_05_4 --> tomoru_graph_2023_05_5{{"Исправил данные которые испортились из за инцидента со временем перемещения кандидатов по воронке. Все кандидаты передвинулись на этап “Отправлено SMS” из за не правильной настройки шкедулера"}}:::child
        end
        
        subgraph tomoru_graph_2023_06
            style tomoru_graph_2023_06 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_06_1 --> tomoru_graph_2023_06_2{{"Новая система логов с помощью logging модуля"}}:::child
            tomoru_graph_2023_06_2 --> tomoru_graph_2023_06_3{{"Создание бекапов postgres"}}:::child
            tomoru_graph_2023_06_3 --> tomoru_graph_2023_06_4{{"Документация и оптимизация гугл таблиц"}}:::child
            tomoru_graph_2023_06_4 --> tomoru_graph_2023_06_5{{"Оптимизация Dockerfile на запуск с 10 минут до 30 секунд за счет кеширования установки зависимостей"}}:::child
        end
        
        subgraph tomoru_graph_2023_07
            style tomoru_graph_2023_07 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_07_1 --> tomoru_graph_2023_07_2{{"Общение с внешними подрядчиками"}}:::child
            tomoru_graph_2023_07_2 --> tomoru_graph_2023_07_3{{"Рефакторинг скрипта генерации видео и ускорение ее в 2 раза. Написание телеграмм бота для интеракции с ним"}}:::child
            tomoru_graph_2023_07_3 --> tomoru_graph_2023_07_4{{"Бот сбора обратной связи"}}:::child
            tomoru_graph_2023_07_4 --> tomoru_graph_2023_07_5{{"Новые инструменты: FastTrack, Albato"}}:::child
        end
        
        subgraph tomoru_graph_2023_08
            style tomoru_graph_2023_08 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_08_1 --> tomoru_graph_2023_08_2{{"Написание openapi документации"}}:::child
            tomoru_graph_2023_08_2 --> tomoru_graph_2023_08_3{{"Написание технических гайдов 'Как пользоваться Postman', 'Как сделать бекап бд', 'Как мы пишем код' и тд"}}:::child
            tomoru_graph_2023_08_3 --> tomoru_graph_2023_08_4{{"Написание CI&CD пайплайна в Github Actions"}}:::child
            tomoru_graph_2023_08_4 --> tomoru_graph_2023_08_5{{"Тесты с pytest (каждый ендпоинт и большинство ютилок) и их внедрение в cd"}}:::child
            tomoru_graph_2023_08_5 --> tomoru_graph_2023_08_6{{"Google Cloud Platform"}}:::child
            tomoru_graph_2023_08_6 --> tomoru_graph_2023_08_7{{"Введение debug конфига для упрощения разработки"}}:::child
            tomoru_graph_2023_08_7 --> tomoru_graph_2023_08_8{{"Новая машинка падает, и перед этим есть рост cpu активности в 100%. а) Убрал 15 минутные downtim'ы сервиса превратив синхронный код в асинхронный (получение данных из amocrm). б) Вынес процесс форматирования данных для аналитики в другой процесс (multiprocessing), и параллельно готовил таблицы к записи"}}:::child
        end
        
        subgraph tomoru_graph_2023_09
            style tomoru_graph_2023_09 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_09_1 --> tomoru_graph_2023_09_2{{"Распределение работы сервера по времени, для экономии ресурсов машины. До фикса во время обновления данных продаж процессор прыгал на 20 минут до 80-90%, а после прыгает на 30 минут до 10% и на пару минут до 20%. Вся сложность была в приведении данных в нужный вид для аналитики. Все данные доставались по апи, и раньше сервер сначала доставал все данные, а потом их обрабатывал. Сейчас же он обрабатывает их сразу при получении каждого запроса, что размазало нагрузку по времени"}}:::child
        end

    end

    main --> softorium
    subgraph softorium_graph
        style softorium_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt
        
        softorium --> softorium_graph_2023_10_1("softorium 2023-10 / 2023-11"):::parent
        softorium --> softorium_graph_2023_11_1("softorium 2023-11 / 2023-12"):::parent
        softorium --> softorium_graph_2023_12_1("softorium 2023-12 / 2024-01"):::parent
        softorium --> softorium_graph_2024_01_1("softorium 2024-01 / 2024-02"):::parent
        softorium --> softorium_graph_2024_02_1("softorium 2024-02 / 2024-03"):::parent
        softorium --> softorium_graph_2024_03_1("softorium 2024-03 / 2024-04"):::parent
        softorium --> softorium_graph_2024_04_1("softorium 2024-04 / 2024-05"):::parent
        softorium --> softorium_graph_2024_05_1("softorium 2024-05 / 2024-06"):::parent
        softorium --> softorium_graph_2024_06_1("softorium 2024-06 / 2024-07"):::parent
        softorium --> softorium_graph_2024_07_1("softorium 2024-07 / 2024-08"):::parent
        softorium --> softorium_graph_2024_08_1("softorium 2024-08 / 2024-09"):::parent
        softorium --> softorium_graph_2024_09_1("softorium 2024-09 / 2024-10"):::parent

        subgraph softorium_graph_2023_10
            style softorium_graph_2023_10 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2023_10_1 --> softorium_graph_2023_10_2{{"Оптимизация Dockerfile. Вынес установку зависимостей в отдельный шаг, чтобы позволить кешировать результат, благодаря чему билд проекта ускорился с 6 минут до 30 секунд"}}:::child
            softorium_graph_2023_10_2 --> softorium_graph_2023_10_3{{"Оптимизировал Dockerfile на использование hot reload у fastapi и dash. Поставил mount с директории кода, на директорию приложения докера, благодаря чему оно видело изменения и перезагружалось. В последствии обновил на `docker compose watch`"}}:::child
            softorium_graph_2023_10_3 --> softorium_graph_2023_10_4{{"Работал с Dash, Flask, Alembic"}}:::child
            softorium_graph_2023_10_4 --> softorium_graph_2023_10_5{{"Повышение качества данных. Повышение нормальной формы базы данных, индексация вторичных ключей и дат, "}}:::child
            softorium_graph_2023_10_5 --> softorium_graph_2023_10_6{{"Написание миграций для превращения String поля в ForeignKey"}}:::child
            softorium_graph_2023_10_6 --> softorium_graph_2023_10_7{{"Создание интерактивного отчета с пользовательскими группировкой, фильтрацией, и показателями, который генерирует sql запрос и отображает в таблицу из конфига на бекенде"}}:::child
        end

        subgraph softorium_graph_2023_11
            style softorium_graph_2023_11 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2023_11_1 --> softorium_graph_2023_11_2{{"Удаление дублирования логики путем выносаа общих компонентов и callback'ов"}}:::child
            softorium_graph_2023_11_2 --> softorium_graph_2023_11_3{{"Кеширование запросов к базе данных (lru_cache)"}}:::child
            softorium_graph_2023_11_3 --> softorium_graph_2023_11_4{{"Оптимизация загрузки страницы с 8 до 2 секунд. Кеширование, упрощение потока выполнения программы, оптимизация записи в Storage (чтение только по открытии страницы, запись только при генерации отчета, а не на каждом изменении) "}}:::child
            softorium_graph_2023_11_4 --> softorium_graph_2023_11_5{{"Функционал для сохранения и отображения "даты последнего изменения""}}:::child
            softorium_graph_2023_11_5 --> softorium_graph_2023_11_6{{"Встраивание форматтера в ci cd"}}:::child
            softorium_graph_2023_11_6 --> softorium_graph_2023_11_7{{"Составление релиз плана с заказчиком"}}:::child
            softorium_graph_2023_11_7 --> softorium_graph_2023_11_8{{"Генерация excel файлов по шаблону (jinja)"}}:::child
            softorium_graph_2023_11_8 --> softorium_graph_2023_11_9{{"Добавление админ панели вместо множества формочек (на самом деле не было, но звучит супер круто)"}}:::child
            softorium_graph_2023_11_9 --> softorium_graph_2023_11_10{{"Создание кастомного logging.handler для логирования в базу данных"}}:::child
            softorium_graph_2023_11_10 --> softorium_graph_2023_11_11{{"Создание и применение конфигураций отчета (система сохранения настроек)"}}:::child
            softorium_graph_2023_11_11 --> softorium_graph_2023_11_12{{"Фронтенд разработка клиентской части на bootstrap (+горизонтальный скролл среди вкладок)"}}:::child
            softorium_graph_2023_11_12 --> softorium_graph_2023_11_13{{"Генератор SQL запросов (включая клиентскую часть). Сохранение конфигураций. Множество группировок и показателей, в том числе сворачивание в bin'ы. Фильтры по полям группировок, показателей и дат. Группировка по периодам (месяц, квартал, год, все время). Сортировка и ограничение выводимых строк (необходимо так как таблица на фронте ограничена в 100к строк). Поддержка вложенных запросов. Сокращение имен столбцов при sql запросе"}}:::child
            softorium_graph_2023_11_13 --> softorium_graph_2023_11_14{{"Улучшение процесса код ревью. Обсуждения “как экологично давать обратную связь”. Процесс обязательный, за исключением пулл реквестов на изменение конфигов. Мерж только если ревьювер сказал 'все ок'. Даже если на проекте ты единственный, проси команду ревьювить чтобы снизить bus factor. Обязательное обозначение какой задачи касается пулл реквест: особенно актуально с большими задачи которые необходимо декомпозировать, так как нужно указывать на какой функционал ожидать при код ревью и не просить больше / меньше"}}:::child
        end

        subgraph softorium_graph_2023_12
            style softorium_graph_2023_12 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2023_12_1 --> softorium_graph_2023_12_2{{"[Отзыв от заказчика](https://softorium.pro/post/Otzyv_Titbit_screen)"}}:::child
            softorium_graph_2023_12_2 --> softorium_graph_2023_12_3{{"Большая работа по рефакторингу. Обновление форматирования с ruff. Добавление аннотаций типов. Удаление лишнего функционала Миграция для добавления полей в JSON поля"}}:::child
            softorium_graph_2023_12_3 --> softorium_graph_2023_12_4{{"Валидация порядка сортировок среди несколько таблиц (сортировки по этой строке может не быть, нужно понимать из какой таблицы строка и по какому индексу, нужно обновить все сортировки в нужном порядке)"}}:::child
            softorium_graph_2023_12_4 --> softorium_graph_2023_12_5{{"Изменение логики расчета метрик 'средние' на 'среднемесячные'"}}:::child
            softorium_graph_2023_12_5 --> softorium_graph_2023_12_6{{"Обновление логики API - отсутствие необязательных параметров больше не вызывает ошибки"}}:::child
        end

        subgraph softorium_graph_2024_01
            style softorium_graph_2024_01 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_01_1 --> softorium_graph_2024_01_2{{"Синхронизация кеша между потоками, смена `lru_cache` на `Redis`. `lru_cache` не синхронизируется между потоками, и для каждого потока создается свой кеш, что вызывало заметные для пользователя промахи кеша "}}:::child
            softorium_graph_2024_01_2 --> softorium_graph_2024_01_3{{"Синхронизация требований к структуре приложения и инфраструктуры между `docker-compose-local` и `docker-compose-dev` файлами - отличались команды запуска и требуемые папки. Возникла ситуация когда требуемая для dev версии папка была удалена, а локально это ошибки не вызвало из за чего слияние тех изменений привело к падению dev версии"}}:::child
            softorium_graph_2024_01_3 --> softorium_graph_2024_01_4{{"Конфигурация ip доступов к postgresql базе данных"}}:::child
            softorium_graph_2024_01_4 --> softorium_graph_2024_01_5{{"Указание временной зоны в строке подключения к базе данных. Ошибка возникала из-за отсутствия, и как следствие не верного определения часовых поясов. Дата в таблице хранилась без указания временной зоны и postgres по умолчанию присваивал значение UTC. При запросе в базу данных временные зоны также не указывались и система выставляла им локальное. Из за этого на клиенте не отображались данные, так как столбцы дат идентифицировались началом периода, а данные содержат значения на 3 часа назад (московское время), то есть прошлый день"}}:::child
            softorium_graph_2024_01_5 --> softorium_graph_2024_01_6{{"Написал скрипт сохранения rtsp потока в 1ч видео файлы"}}:::child
            softorium_graph_2024_01_6 --> softorium_graph_2024_01_7{{"Передача фото по API и их запись в файл"}}:::child
            softorium_graph_2024_01_7 --> softorium_graph_2024_01_8{{"Обновление production сервера с dev, устранение ошибок с базой данных связанных с изменениями появившимися без миграций"}}:::child
            softorium_graph_2024_01_8 --> softorium_graph_2024_01_9{{"Разрешение ошибок при применении миграций, в том числе изменение ORM кода на SQL для сохранения исторической целостности. ORM использовал текущее описание модели которое содержало поля, которые были созданы сильно после создания этой миграции и вызывали ошибку при выборке"}}:::child
            softorium_graph_2024_01_9 --> softorium_graph_2024_01_10{{"linux. Процесс менеджмент (получение PID, чтение по нему stdout и sterr). Перенаправление выходов (piping)"}}:::child
            softorium_graph_2024_01_10 --> softorium_graph_2024_01_11{{"Фильтрация данных на клиенте для снижения загрузки с сервера. Данных было немного и клиент загружал все разом и фильтры на странице обращались не к серверу, а к этому хранилищу"}}:::child
            softorium_graph_2024_01_11 --> softorium_graph_2024_01_12{{"Интерфейс для редактирования данных (корректировка статуса номенклатуры). Каждое действие пользователя сохранялось и его можно было отменить. Паттерн 'Command'. Диалоговое окно подтверждения с отображением изменений"}}:::child
        end

        subgraph softorium_graph_2024_02
            style softorium_graph_2024_02 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_02_1 --> softorium_graph_2024_02_2{{"Разрешил ошибку с сравнением строк путем анализа их байт кода (различались символы новой строки)"}}:::child
            softorium_graph_2024_02_2 --> softorium_graph_2024_02_3{{"Использование window функций в SQL для нахождения даты с максимальным значением (сортировка по этому полю, нумерация postgres функцией rank, и фильтрация по значению 1)"}}:::child
            softorium_graph_2024_02_3 --> softorium_graph_2024_02_4{{"Повышение качества базы данных, а не обход аномалий (метод 'падать быстро') - статусы внутри одной сети дублировались среди разных магазинов, хотя такого не должно было быть. Заказчик предложил обходить это в отчете, беря первый статус"}}:::child
            softorium_graph_2024_02_4 --> softorium_graph_2024_02_5{{"Фильтрация групп номенклатуры если какая либо из записей содержит значение статуса (HAVING + sum(case when status in () then 1 else 0))"}}:::child
            softorium_graph_2024_02_5 --> softorium_graph_2024_02_6{{"Создал миграцию которая исправляла аномалию в данных. При заполнении статусов в таблице sales создалось много записей которые принадлежат одной сети и клиенту, но имеют разные статусы за одну дату"}}:::child
            softorium_graph_2024_02_6 --> softorium_graph_2024_02_7{{"Регистрация программы как `systemd` сервиса для автозапуска на старте системы и создание `bash install` скрипта для автоматической настройки"}}:::child
            softorium_graph_2024_02_7 --> softorium_graph_2024_02_8{{"Создание docker изображения программы для упрощения ее запуска (+ поддержка автоперезагрузки программы при изменении конфигов)"}}:::child
            softorium_graph_2024_02_8 --> softorium_graph_2024_02_9{{"Доработка Dash.Datatable компонента на возможность отключения сортировки у конкретных столбцов"}}:::child
        end

        subgraph softorium_graph_2024_03
            style softorium_graph_2024_03 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_03_1 --> softorium_graph_2024_03_2{{"Предложение ввода тест кейсов и их написание"}}:::child
            softorium_graph_2024_03_2 --> softorium_graph_2024_03_3{{"Удаление из pd.DataFrame столбцов которые не отображаются на клиенте для удаления дублируемых строк"}}:::child
            softorium_graph_2024_03_3 --> softorium_graph_2024_03_4{{"Оптимизация загрузки страницы с 5 секунд до меньше чем 0.5: удаление лишних вызовов к базе данных и получение данных 1 раз в 1 месте"}}:::child
            softorium_graph_2024_03_4 --> softorium_graph_2024_03_5{{"Упрощение кодовой базы, удаление мертвого кода и лишних утилит (принципы DRY + KISS). Сокращение объема utils директорий и callback функций как минимум в 2 раза"}}:::child
            softorium_graph_2024_03_5 --> softorium_graph_2024_03_6{{"Использование jupiter notebook расширения для своей IDE для быстрого тестирования теорий (без запуска всего приложения). Скорость каждой итераций выросла с 5-10 минут до 1 минуты"}}:::child
            softorium_graph_2024_03_6 --> softorium_graph_2024_03_7{{"Вынос повторяющихся стилей компонентов в общее пространство"}}:::child
            softorium_graph_2024_03_7 --> softorium_graph_2024_03_8{{"Подключение swagger документации к Flask API и описание путей с запросами, ответами и примерами"}}:::child
            softorium_graph_2024_03_8 --> softorium_graph_2024_03_9{{"Составление кейса проекта. Описание проблемы заказчика, предложенных решений, процессе и технологиях разработки, реализованных решений"}}:::child
            softorium_graph_2024_03_9 --> softorium_graph_2024_03_10{{"Перенос функций по фильтрации и выборке и данных из backend стороны в сторону базы данных, тем самым улучшив производительность и разграничение обязанностей между слоями сервиса"}}:::child
        end

        subgraph softorium_graph_2024_04
            style softorium_graph_2024_04 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_04_1 --> softorium_graph_2024_04_2{{"Написание кейса проекта"}}:::child
            softorium_graph_2024_04_2 --> softorium_graph_2024_04_3{{"Предложение решений по предзагрузке данных для фильтров (экран загрузки / фоновая загрузка данных)"}}:::child
            softorium_graph_2024_04_3 --> softorium_graph_2024_04_4{{"Создание Celery задачи для прогрева кеша"}}:::child
            softorium_graph_2024_04_4 --> softorium_graph_2024_04_5{{"Оптимизация структуры базы данных - сохранение статуса номенклатуры не в таблице продаж sales, а в отдельной где указываются у какой номенклатуры с какого периода какой статус"}}:::child
            softorium_graph_2024_04_5 --> softorium_graph_2024_04_6{{"Оборачивание сервиса с приложением, очередью, базой данных и кэшем в docker контейнеры"}}:::child
            softorium_graph_2024_04_6 --> softorium_graph_2024_04_7{{"Изменение текста popup подсказки React компонента из библиотеки, исключительно средствами CSS. Скрытие текста с помощью `visible: hidden`. Добавление `:before` псевдокласса с установленными `visible: visible; content: ''; margin-bottom: -20px`"}}:::child
            softorium_graph_2024_04_7 --> softorium_graph_2024_04_8{{"Рефакторинг системы сохранения настроек. Все настройки были юнифицированы в одну таблицу с JSON столбцом для единого механизма работы, и простоты сохранения этих настроек на клиенте. Все JSON поля перед получением проверялись на существование, так как при изменении их структуры старые сохраненные настройки ломались "}}:::child
            softorium_graph_2024_04_8 --> softorium_graph_2024_04_9{{"Общение с заказчиком по поводу сроков, их задержки и причин "}}:::child
            softorium_graph_2024_04_9 --> softorium_graph_2024_04_10{{"Рефакторинг. Смена компонентов страницы с dash.DataTable на html таблицу с стандартными Input компонентами"}}:::child
            softorium_graph_2024_04_10 --> softorium_graph_2024_04_11{{"Анализ выполнения SQL запросов, изучение cost каждого шага"}}:::child
            softorium_graph_2024_04_11 --> softorium_graph_2024_04_12{{"Ускорение выполнения сложных аналитических запросов в 3 раза за счет построения индексов в базе данных и устранения ненужных join условий"}}:::child
        end

        subgraph softorium_graph_2024_05
            style softorium_graph_2024_05 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_05_1 --> softorium_graph_2024_05_2{{"Оптимизация потока выполнения celery задач, использование chain и group вместо рекурсивного создания AsyncResult по countdown. Итогом стало создание 1 celery задачи на 5 минутный таск вместо 30, благодаря чему скорость выполнения запроса выросла на 10% а использование памяти из O(n) времени стало O(1)"}}:::child
            softorium_graph_2024_05_2 --> softorium_graph_2024_05_3{{"Изменил процесс работы с кодом заказчика. В аутсорс компании было правило что вся работа с кодом ведется в репозитории компании, и если у заказчика есть свой репозиторий то он обновляется из него. При работе с одним заказчиком который был погружен в техническую часть я вместе с проджект менеджером настояли на изменении процесса чтобы заказчик наглядно видел всю работу, мерж реквесты и код ревью. Это не только помогло повысить доверие к нам, но и сэкономило позже деньги так как я был повышен до лида прокта и стал единственным разработчиком после неэффективных с точки зрения заказчика код ревью"}}:::child
            softorium_graph_2024_05_3 --> softorium_graph_2024_05_4{{"Ссылка celery worker контейнера на изображение которое использует приложение, для избежания повторного билда"}}:::child
            softorium_graph_2024_05_4 --> softorium_graph_2024_05_5{{"Создание CI/CD процесса для деплоя docker-compose файла в gitlab"}}:::child
            softorium_graph_2024_05_5 --> softorium_graph_2024_05_6{{"Разрешение ошибок в gitlab ci при работе с git репозиторием. Gitlab ci был скопирован с другого проекта и gitlab runner переходил из своего окружения в локальную папку и пытался взаимодействовать с git репозиторием к которому у него не было доступа"}}:::child
            softorium_graph_2024_05_6 --> softorium_graph_2024_05_7{{"Добавление 192.168.0.0/16 и 172.16.0.0/12 сетей в pg_hba.conf для процесса ci/cd"}}:::child
        end

        subgraph softorium_graph_2024_06
            style softorium_graph_2024_06 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_06_1 --> softorium_graph_2024_06_2{{"Использование null значения вместо значений по умолчанию"}}:::child
            softorium_graph_2024_06_2 --> softorium_graph_2024_06_3{{"Создание миграций для обновления данных вместо создания дополнительной логики в сервисе. После занесения в базу данных дат '0001-01-01' из апи, не предусматривать такую возможность в сервисе, а исправить данные"}}:::child
            softorium_graph_2024_06_3 --> softorium_graph_2024_06_4{{"Объединение 3 таблиц с логами в одну и обновление логики их фильтрации на использование регулярных выражений. Необходимо чтобы не терялась информация и не было лишней логики в сервисе на взаимодействие с несколькими таблицами"}}:::child
            softorium_graph_2024_06_4 --> softorium_graph_2024_06_5{{"Повышение качества данных и оптимизация базы данных - удаление дублирующихся индексов, что ускорило операции по записи в 2 раза"}}:::child
            softorium_graph_2024_06_5 --> softorium_graph_2024_06_6{{"Создание документации с требованиями к данным для аналитических отчётов"}}:::child
            softorium_graph_2024_06_6 --> softorium_graph_2024_06_7{{"Стандартизация создания отчета, четкое разделение на этапы: очищение данных, загрузка данных, валидация, расчет, сохранение, логирование промежуточных этапов и определение этих операций в наследуемых классах"}}:::child
            softorium_graph_2024_06_7 --> softorium_graph_2024_06_8{{"Оптимизация запросов в базу данных - превращение 2 запросов в for цикле из 3000+ записей в 2 на всю функцию, и оптимизация работы с 1.5 часа до 2 минут"}}:::child
        end

        subgraph softorium_graph_2024_07
            style softorium_graph_2024_07 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_07_1 --> softorium_graph_2024_07_2{{"Динамическая загрузка `APIRouter` объектов из модулей в пакете `routers` и включение их в `FastAPI` объект"}}:::child
            softorium_graph_2024_07_2 --> softorium_graph_2024_07_3{{"Синхронизация collation базы данных между dev и prod стендами чтобы операции фильтрации и поиска давали консистентные результаты"}}:::child
            softorium_graph_2024_07_3 --> softorium_graph_2024_07_4{{"Rebuild инвалидированных индексов при изменении collation"}}:::child
            softorium_graph_2024_07_4 --> softorium_graph_2024_07_5{{"Изолирование тестов друг от друга, тестирование upgrade и downgrade миграций, предотвращение появления сайд эффектов после выполнения теста"}}:::child
            softorium_graph_2024_07_5 --> softorium_graph_2024_07_6{{"Создание скрипта и ci/cd задачи по увеличению версии при принятии мерж реквеста в development или master ветку"}}:::child
            softorium_graph_2024_07_6 --> softorium_graph_2024_07_7{{"git checkout в прошлые коммиты для определения после каких изменений появился баг"}}:::child
            softorium_graph_2024_07_7 --> softorium_graph_2024_07_8{{"Объединил все операции с базой данных в рамках одного API ендпоинта в транзакцию чтобы обеспечить атомарность операции"}}:::child
            softorium_graph_2024_07_8 --> softorium_graph_2024_07_9{{"Использование Explain Analyze для ускорения SQL запросов. Построение индексов на часто используемые столбцы. Удаление лишних join условий. Замена Inline выражений на константные"}}:::child
        end

        subgraph softorium_graph_2024_08
            style softorium_graph_2024_08 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_08_1 --> softorium_graph_2024_08_2{{"Создание cron задачи для автоматического бекапа базы данных (pd_dump + pg_restore)"}}:::child
            softorium_graph_2024_08_2 --> softorium_graph_2024_08_3{{"Откат изменений с помощью git reset и сохранение изменений в stash"}}:::child
            softorium_graph_2024_08_3 --> softorium_graph_2024_08_4{{"Сохранение git stash'а в отдельный файл, перенос на флешку и применение на другом пк"}}:::child
        end

        subgraph softorium_graph_2024_09
            style softorium_graph_2024_09 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_09_1 --> softorium_graph_2024_09_2{{"Код ревью и оценка грейда кандидатов на вакансии"}}:::child
            softorium_graph_2024_09_2 --> softorium_graph_2024_09_3{{"Ускорение запроса с фильтрацией по uuid в 112 раз путем изменения индекса базы данных с btree на hash"}}:::child
            softorium_graph_2024_09_3 --> softorium_graph_2024_09_4{{"Создание plotly отчетов - pie chart'ы, гистограммы, динамика выручки, доля полки по поставщикам"}}:::child
        end
    end
```
