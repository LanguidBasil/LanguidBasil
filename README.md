# Hi there ✨ I'm ...

![ascii art](./assets/ascii.gif)

## about me

[Short CV here](https://drive.google.com/file/d/1uLDzea3lqNvleykk8VX-VC3cBDDupUKY/view)

TODO: write my story

<!-- I started learning to code at my school when was 16. I was introduced to Turbo Pascal at computer science class. It amazed me how you can tell computer simple instructions and it will execute it. I've immideatly applied this knoweledge and wrote a programm that finds roots of the discriminant and flashed through my math homework. I wanted more so I took home textbook and finished every given exercise over next 3 weeks.

After this experience I knew what career path I will take. I've started preparing for final exams at school and was aiming for computer science programs. Daily nerding out questions and solving tests from past years I managed to score 252 out of 300 points and got myself into university I dreamed about - Far Eastern Federal University in Vladivostok.

![fefu](./assets/fefu.jpg)

I enrolled for 'Applied Computer Science in Business'. I loved campus, nothing compared with view of the sea from my cozy dorm. Classmates were awesome, many played guitar, organized events and of course all of them were geeks. Program was much fun too. Math classes combined with economics and sprinlked with OOP and Algorithms on top is a cake for a great career.

Quite a sudden realization came when I was sitting in the evening with my homework - "This theory is good and all, but I want something more practical". I tried making simple websites and programs, but nothing felt interesting enough. Until I came upon a post in my news feed about an upcoming game jam. That's it I thought, a chance to do something great. I've signed up for a gamejam, found a team and we've made 🐱‍🐉🔧 Dinofication ⚡🏠. Cute little game about a Dino who was fixing home electronics while tenants were gone

https://gr3yknigh1.itch.io/dinofication

...

Why gamedev sucked for me

How I found Tomoru

My plans -->

## technologies

<img width="16px" src="./assets/python.svg" alt="python logo" /> Python <img width="16px" src="./assets/fastapi.svg" alt="fastapi logo" /> FastAPI <img width="16px" src="./assets/django.svg" alt="django logo" /> Django <img width="16px" src="./assets/sqlalchemy.svg" alt="sqlalchemy logo" /> SQLAlchemy <img width="16px" src="./assets/pandas.svg" alt="sqlalchemy logo" /> Pandas

<img width="16px" src="./assets/html.svg" alt="html logo" /> html <img width="16px" src="./assets/css.svg" alt="css logo" /> css <img width="16px" src="./assets/javascript.svg" alt="javascript logo" /> Javascript <img width="16px" src="./assets/react.svg" alt="react logo" /> React

<img width="16px" src="./assets/postgres.svg" alt="postgres logo" /> Postgres <img width="16px" src="./assets/redis.svg" alt="redis logo" /> Redis <img width="16px" src="./assets/mongodb.svg" alt="mongodb logo" /> MongoDB <img width="16px" src="./assets/sqlite.svg" alt="sqlite logo" /> SQLite

<img width="16px" src="./assets/docker.svg" alt="docker logo" /> Docker <img width="16px" src="./assets/gitlab.svg" alt="gitlab logo" /> Gitlab CI <img width="16px" src="./assets/github.svg" alt="github logo" /> Github CI

## contacts

<!-- TODO: maybe change to badges? Example: https://github.com/fastapi/fastapi -->

<img width="16px" src="./assets/telegram.svg" alt="telegram logo" /> [telegram](https://t.me/emakunev)

<img width="16px" src="./assets/linkedin.svg" alt="linkedin logo" /> [LinkedIn](https://www.linkedin.com/in/eugene-makunev-b9682b233/)

<img width="16px" src="./assets/mail.svg" alt="mail logo" /> [Mail](mailto:e.makunev@gmail.com)

## achievements

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

        university --> university_1{{"Ant algorithm in Pascal"}}:::child
        university_1 --> university_2{{"Snake game in self-written assembler. Logisim"}}:::child
        university_2 --> university_3{{"Modeling a system for processing details and improving resource utilization by optimizing various factors: table capacity, processing speed, number of workers, etc. C# + WinForms"}}:::child
        university_3 --> university_4{{"Implementation of different sorting algorithms and their comparison. C# + WinForms"}}:::child
        university_4 --> university_5{{"Enterprise Network Modeling. Cisco Packet Tracer"}}:::child
        university_5 --> university_6{{"API Limiter. Python + FastAPI + Redis"}}:::child
        university_6 --> university_7{{"Online store in OpenCart"}}:::child
    end

    university --> university_graduate_work
    subgraph university_graduate_work_graph
        style university_graduate_work_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

        university_graduate_work --> university_graduate_work_1{{"Design and development of human resource management system"}}:::child
        university_graduate_work_1 --> university_graduate_work_2{{"React + React Router (client side rendering and routing), Typescript, NPM, eslint"}}:::child
        university_graduate_work_2 --> university_graduate_work_3{{"Python + FastAPI + Postgres + Docker"}}:::child
    end

    university --> university_naruto
    subgraph university_naruto_graph
        style university_naruto_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

        university_naruto --> university_naruto_1{{"Telegram bot for writing expenses from a QR code on a receipt into a Google spreadsheet, with a Machine Learning algorithm for determining the category of goods (food, tasty food, clothing, transport, etc.)"}}:::child
        university_naruto_1 --> university_naruto_2{{"Including configuration and permissions files in `.dockerignore` to avoid them being included in the docker image"}}:::child
        university_naruto_2 --> university_naruto_3{{"Python + FastAPI + sklearn (naive bayes classifier)"}}:::child
    end

    main --> paper_plane
    subgraph paper_plane_graph
        style paper_plane_graph fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

        paper_plane --> paper_plane_1{{"Character controller with detailed settings - double jump, coyote time, time to gain and reset maximum speed"}}:::child
        paper_plane_1 --> paper_plane_2{{"Random level generation with object presets"}}:::child
        paper_plane_2 --> paper_plane_3{{"Creating Levels and Importing Assets in Unity"}}:::child
        paper_plane_3 --> paper_plane_4{{"Shaders for highlighting areas of interest"}}:::child
        paper_plane_4 --> paper_plane_5{{"Artificial Intelligence with patrol and role-based combat systems"}}:::child
        paper_plane_5 --> paper_plane_6{{"Creating systems of saving, dialogues, inventory, states"}}:::child
        paper_plane_6 --> paper_plane_7{{"Reverse Engioneering Unity build to get myself an avatar for telegram"}}:::child
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

            tomoru_graph_2023_04_1 --> tomoru_graph_2023_04_2{{"Receiving data via API from third-party services, processing it and writing it to PostgreSQL, Google Spreadsheets and BigQuery"}}:::child
            tomoru_graph_2023_04_1 --> tomoru_graph_2023_04_2{{"Acceleration of loading 5 gigabytes of data from AmoCRM API by 4 times by distributing it to 4 celery workers"}}:::child
            tomoru_graph_2023_04_2 --> tomoru_graph_2023_04_3{{"Macro for creating Google Spreadsheets backups"}}:::child
            tomoru_graph_2023_04_3 --> tomoru_graph_2023_04_4{{"Form for adding and updating data on the company platform"}}:::child
            tomoru_graph_2023_04_4 --> tomoru_graph_2023_04_5{{"Cleaning data and improving its reliability"}}:::child
            tomoru_graph_2023_04_5 --> tomoru_graph_2023_04_6{{"Caching data via webhook (Huntflow)"}}:::child
            tomoru_graph_2023_04_6 --> tomoru_graph_2023_04_7{{"Setting up integration between our service, telegram bot and CRM"}}:::child
            tomoru_graph_2023_04_7 --> tomoru_graph_2023_04_8{{"Telegram bot for video generation"}}:::child
            tomoru_graph_2023_04_8 --> tomoru_graph_2023_04_9{{"HR tinder"}}:::child
            tomoru_graph_2023_04_9 --> tomoru_graph_2023_04_10{{"Mentoring Nikita"}}:::child
            tomoru_graph_2023_04_10 --> tomoru_graph_2023_04_11{{"Adoption of code reviews"}}:::child
        end

        subgraph tomoru_graph_2023_05
            style tomoru_graph_2023_05 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_05_1 --> tomoru_graph_2023_05_2{{"Phone verification via SMS, HR analytics"}}:::child
            tomoru_graph_2023_05_2 --> tomoru_graph_2023_05_3{{"Reworked the data schema using Json for flexibility in adding new stages in the hiring funnel"}}:::child
            tomoru_graph_2023_05_3 --> tomoru_graph_2023_05_4{{"Created a config file for Google Sheets to specify the order and location of data unloading from the database"}}:::child
            tomoru_graph_2023_05_4 --> tomoru_graph_2023_05_5{{"Corrected data that was corrupted due to an incident with the time of candidates moving through the funnel. All candidates moved to the stage 'SMS sent' due to incorrect settings of the scheduler"}}:::child
        end

        subgraph tomoru_graph_2023_06
            style tomoru_graph_2023_06 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_06_1 --> tomoru_graph_2023_06_2{{"New logging system using logging module"}}:::child
            tomoru_graph_2023_06_2 --> tomoru_graph_2023_06_3{{"Setting up schedulled postgres backups"}}:::child
            tomoru_graph_2023_06_3 --> tomoru_graph_2023_06_4{{"Google Sheets documentation and optimization"}}:::child
            tomoru_graph_2023_06_4 --> tomoru_graph_2023_06_5{{"Optimized Dockerfile startup time from 10 minutes to 30 seconds by caching dependency installation"}}:::child
        end

        subgraph tomoru_graph_2023_07
            style tomoru_graph_2023_07 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_07_1 --> tomoru_graph_2023_07_2{{"Communication with counterparties"}}:::child
            tomoru_graph_2023_07_2 --> tomoru_graph_2023_07_3{{"Refactoring the video generation script and speeding it up by 2 times. Writing a telegram bot to interact with it"}}:::child
            tomoru_graph_2023_07_3 --> tomoru_graph_2023_07_4{{"Feedback collection bot"}}:::child
            tomoru_graph_2023_07_4 --> tomoru_graph_2023_07_5{{"New tools: FastTrack, Albato"}}:::child
        end

        subgraph tomoru_graph_2023_08
            style tomoru_graph_2023_08 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_08_1 --> tomoru_graph_2023_08_2{{"Writing openapi documentation"}}:::child
            tomoru_graph_2023_08_2 --> tomoru_graph_2023_08_3{{"Writing technical guides 'How to use Postman', 'How to make a database backup', 'How we write code', etc."}}:::child
            tomoru_graph_2023_08_3 --> tomoru_graph_2023_08_4{{"Writing a CI&CD Pipeline in Github Actions"}}:::child
            tomoru_graph_2023_08_4 --> tomoru_graph_2023_08_5{{"Tests with pytest (each endpoint and most utilities, 82% test coverage) and their implementation in cd"}}:::child
            tomoru_graph_2023_08_5 --> tomoru_graph_2023_08_6{{"Creation of virtual machine in Google Cloud Platform and setting up firewall rules"}}:::child
            tomoru_graph_2023_08_6 --> tomoru_graph_2023_08_7{{"Introducing debug config to simplify development"}}:::child
            tomoru_graph_2023_08_7 --> tomoru_graph_2023_08_8{{"The new machine crashes, and before that there is a 100% increase in CPU activity. a) Removed 15-minute service downtims by converting synchronous code into asynchronous (receiving data from amocrm). b) Moved the data formatting process for analytics to another process (multiprocessing), and simultaneously prepared tables for recording"}}:::child
        end

        subgraph tomoru_graph_2023_09
            style tomoru_graph_2023_09 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            tomoru_graph_2023_09_1 --> tomoru_graph_2023_09_2{{"Distribution of server work on timeline, to save machine resources. Before the fix, during the update of sales data, the processor jumped for 20 minutes to 80-90%, and then jumped for 30 minutes to 10%. The whole difficulty was in bringing the data into the required form for analytics. All data was retrieved via API, and then server processed it. Now it processes it immediately upon receiving each request, which spread the load over time"}}:::child
            tomoru_graph_2023_09_2 --> tomoru_graph_2023_09_3{{"Adding an admin panel instead of a bunch of forms"}}:::child
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

            softorium_graph_2023_10_1 --> softorium_graph_2023_10_2{{"Dockerfile optimization. Moved dependency installation to a separate step to allow caching the result, which speed up the project build from 6 minutes to 30 seconds"}}:::child
            softorium_graph_2023_10_2 --> softorium_graph_2023_10_3{{"Optimized Dockerfile to use hot reload in fastapi and dash. Set mount from code directory to docker application directory, so it saw changes and rebooted. Later updated to use `docker compose watch`"}}:::child
            softorium_graph_2023_10_3 --> softorium_graph_2023_10_4{{"Worked with Dash, Flask, Alembic"}}:::child
            softorium_graph_2023_10_4 --> softorium_graph_2023_10_5{{"Improving data quality. Improving the normal form of the database, indexing foreign keys and dates"}}:::child
            softorium_graph_2023_10_5 --> softorium_graph_2023_10_6{{"Writing Migrations to Convert a String Field to a ForeignKey"}}:::child
            softorium_graph_2023_10_6 --> softorium_graph_2023_10_7{{"Creating an interactive report with custom grouping, filtering, and metrics that generates a SQL query and displays it in a table from the config on the backend"}}:::child
        end

        subgraph softorium_graph_2023_11
            style softorium_graph_2023_11 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2023_11_1 --> softorium_graph_2023_11_2{{"Removing duplicate logic by moving common components and callbacks"}}:::child
            softorium_graph_2023_11_2 --> softorium_graph_2023_11_3{{"Database query caching (lru_cache)"}}:::child
            softorium_graph_2023_11_3 --> softorium_graph_2023_11_4{{"Optimization of page loading from 8 to 2 seconds. Caching, simplifying the program execution flow, optimizing writing to Storage (reading only when the page is opened, writing only when generating a report, not on each change) "}}:::child
            softorium_graph_2023_11_4 --> softorium_graph_2023_11_5{{"Functionality for saving and displaying 'last modified date'"}}:::child
            softorium_graph_2023_11_5 --> softorium_graph_2023_11_6{{"Embedding Ruff formatter in ci cd"}}:::child
            softorium_graph_2023_11_6 --> softorium_graph_2023_11_7{{"Drawing up a release plan with business analyst"}}:::child
            softorium_graph_2023_11_7 --> softorium_graph_2023_11_8{{"Generating excel files using a jinja templating engine"}}:::child
            softorium_graph_2023_11_8 --> softorium_graph_2023_11_9{{"Creating a custom logging.handler for logging to the database"}}:::child
            softorium_graph_2023_11_9 --> softorium_graph_2023_11_10{{"Creating and applying report configurations (system for saving settings)"}}:::child
            softorium_graph_2023_11_10 --> softorium_graph_2023_11_11{{"Frontend development of the client part on bootstrap (+ horizontal scrolling among tabs"}}:::child
            softorium_graph_2023_11_11 --> softorium_graph_2023_11_12{{"SQL query generator (including the client side). Saving configurations. Many groupings and metrics, including collapsing into bins. Filters by grouping fields, indicators and dates. Grouping by periods (month, quarter, year, all time). Sorting and limiting output lines (necessary since the table on the front is limited to 100k lines). Support for nested queries. Abbreviation of column names in SQL queries"}}:::child
            softorium_graph_2023_11_12 --> softorium_graph_2023_11_13{{"Improving the code review process. Discussions on “how to give feedback in friendly way”. The process is mandatory, with the exception of pull requests for config change. Merge only if the reviewer says 'everything is ok'. Even if you are the only one on the project, ask the other team to review to reduce the bus factor. Mandatory designation of what task the pull request concerns: especially relevant for large tasks that need to be decomposed, since you need to indicate what functionality to expect during code review and not ask for more or less"}}:::child
        end

        subgraph softorium_graph_2023_12
            style softorium_graph_2023_12 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2023_12_1 --> softorium_graph_2023_12_2{{"[Feedback from a client](https://softorium.pro/post/Otzyv_Titbit_screen)"}}:::child
            softorium_graph_2023_12_2 --> softorium_graph_2023_12_3{{"Lots of refactoring work. Updating formatting with ruff. Adding type annotations. Removing unnecessary functionality. Migration to add fields to JSON fields"}}:::child
            softorium_graph_2023_12_3 --> softorium_graph_2023_12_4{{"Validation of sorting order among several tables. Sorting by some rows is not possible, you need to understand from which table the row is and by which index, you need to update all sorting in the required order"}}:::child
            softorium_graph_2023_12_4 --> softorium_graph_2023_12_5{{"Changed the logic for calculating metrics from 'average' to 'monthly average'"}}:::child
            softorium_graph_2023_12_5 --> softorium_graph_2023_12_6{{"API logic update - missing optional parameters no longer causes an error"}}:::child
        end

        subgraph softorium_graph_2024_01
            style softorium_graph_2024_01 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_01_1 --> softorium_graph_2024_01_2{{"Synchronize cache between threads, change `lru_cache` to `Redis`. `lru_cache` is not synchronized between threads, and each thread creates its own cache, which caused cache misses that were noticeable to the user"}}:::child
            softorium_graph_2024_01_2 --> softorium_graph_2024_01_3{{"Synchronization of application and infrastructure structure requirements between `docker-compose-local` and `docker-compose-dev` files - startup commands and required folders were different. A situation arose when a folder required for the dev version was deleted, but locally this did not cause an error, which is why merging those changes led to a crash of the dev version"}}:::child
            softorium_graph_2024_01_3 --> softorium_graph_2024_01_4{{"Configuration of IP access to postgresql database"}}:::child
            softorium_graph_2024_01_4 --> softorium_graph_2024_01_5{{"Specifying the time zone in the database connection string. The error occurred due to the absence and, as a result, incorrect definition of time zones. The date in the table was stored without specifying the time zone and postgres assigned the UTC value by default. When querying the database, time zones were also not specified and the system set the local one. Because of this, the data was not displayed on the client, since the date columns were identified by the beginning of the period, and the data contains values ​​​​for 3 hours ago (Moscow time), that is, the previous day"}}:::child
            softorium_graph_2024_01_5 --> softorium_graph_2024_01_6{{"Wrote a script to save rtsp stream into 1h video files"}}:::child
            softorium_graph_2024_01_6 --> softorium_graph_2024_01_7{{"Transferring photos via API and writing them to a media storage"}}:::child
            softorium_graph_2024_01_7 --> softorium_graph_2024_01_8{{"Updating production server from dev, fixing database errors related to changes that appeared without migrations"}}:::child
            softorium_graph_2024_01_8 --> softorium_graph_2024_01_9{{"Resolving errors when applying migrations, including changing ORM code to SQL to preserve historical integrity. The ORM used the current model definition that contained fields that were created long after the creation of this migration and caused an error when fetching"}}:::child
            softorium_graph_2024_01_9 --> softorium_graph_2024_01_10{{"linux. Process management (getting PID, reading stdout and sterr from source). Output redirection (piping)"}}:::child
            softorium_graph_2024_01_10 --> softorium_graph_2024_01_11{{"Filtering data on the client to reduce the load from the server. There was little data and the client loaded everything at once and the filters on the page did not access the server, but this storage"}}:::child
            softorium_graph_2024_01_11 --> softorium_graph_2024_01_12{{"Interface for editing data (correcting item status). Each user action was saved and could be undone. 'Command' pattern. Confirmation dialog box with display of changes"}}:::child
        end

        subgraph softorium_graph_2024_02
            style softorium_graph_2024_02 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_02_1 --> softorium_graph_2024_02_2{{"Resolved a bug with string comparison by analyzing their byte code (newline characters were different)"}}:::child
            softorium_graph_2024_02_2 --> softorium_graph_2024_02_3{{"Using window functions in SQL to find the date with the maximum value (sort by this field, number by postgres rank function, and filter by value 1)"}}:::child
            softorium_graph_2024_02_3 --> softorium_graph_2024_02_4{{"Improving the quality of the database, not bypassing anomalies (the 'fail fast' method). Statuses within one network were duplicated among different stores, although this should not have happened. The customer suggested bypassing this in the report by taking the first status instead of adding additional checks to database"}}:::child
            softorium_graph_2024_02_4 --> softorium_graph_2024_02_5{{"Filtering item groups if any of the records contains a status value `HAVING + sum(case when status in () then 1 else 0)`"}}:::child
            softorium_graph_2024_02_5 --> softorium_graph_2024_02_6{{"Created a migration that corrected an anomaly in the data. When filling in the statuses in the sales table, many records were created that belong to the same network and client, but have different statuses for the same date"}}:::child
            softorium_graph_2024_02_6 --> softorium_graph_2024_02_7{{"Registering the program as a `systemd` service for autostart at system startup and creating a `bash install` script for automatic configuration"}}:::child
            softorium_graph_2024_02_7 --> softorium_graph_2024_02_8{{"Creating a docker image of a program to simplify its launch (+ support for auto-restarting the program when changing configs)"}}:::child
            softorium_graph_2024_02_8 --> softorium_graph_2024_02_9{{"Improvement of Dash.Datatable component to enable disabling sorting for specific columns"}}:::child
        end

        subgraph softorium_graph_2024_03
            style softorium_graph_2024_03 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_03_1 --> softorium_graph_2024_03_2{{"Introducing test cases and writing them"}}:::child
            softorium_graph_2024_03_2 --> softorium_graph_2024_03_3{{"Remove columns from pd.DataFrame that are not displayed on the client to remove duplicate rows"}}:::child
            softorium_graph_2024_03_3 --> softorium_graph_2024_03_4{{"Optimize page load from 5 seconds to less than 0.5: remove unnecessary database calls and retrieve data once in one place"}}:::child
            softorium_graph_2024_03_4 --> softorium_graph_2024_03_5{{"Simplifying the code base, removing dead code and unnecessary utilities (DRY + KISS principles). Reducing the size of utils directories and callback functions by at least 2 times"}}:::child
            softorium_graph_2024_03_5 --> softorium_graph_2024_03_6{{"Using the jupiter notebook extension for my IDE to quickly test theories (without running the entire application). The speed of each iteration increased from 5-10 minutes to 1 minute"}}:::child
            softorium_graph_2024_03_6 --> softorium_graph_2024_03_7{{"Bringing out repeating component styles into a common space"}}:::child
            softorium_graph_2024_03_7 --> softorium_graph_2024_03_8{{"Connecting swagger documentation to Flask API and describing paths with requests, responses and examples"}}:::child
            softorium_graph_2024_03_8 --> softorium_graph_2024_03_9{{"Compilation of a project case. Description of the customer's problem, proposed solutions, development process and technologies, implemented solutions"}}:::child
            softorium_graph_2024_03_9 --> softorium_graph_2024_03_10{{"Transferring filtering and data retrieval functions from the backend to the database, thereby improving performance and separating responsibilities between service layers"}}:::child
        end

        subgraph softorium_graph_2024_04
            style softorium_graph_2024_04 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_04_1 --> softorium_graph_2024_04_2{{"Writing a project case"}}:::child
            softorium_graph_2024_04_2 --> softorium_graph_2024_04_3{{"Preloading data for filters (loading screen/background data loading)"}}:::child
            softorium_graph_2024_04_3 --> softorium_graph_2024_04_4{{"Create a Celery task to warm up the cache"}}:::child
            softorium_graph_2024_04_4 --> softorium_graph_2024_04_5{{"Optimization of the database structure - saving the item status not in the sales table, but in a separate one, where the status of every item is indicated 'from some period'. Reducing size of stored info by 350%"}}:::child
            softorium_graph_2024_04_5 --> softorium_graph_2024_04_6{{"Wrapping a service with an application, message queue, database and cache in docker containers"}}:::child
            softorium_graph_2024_04_6 --> softorium_graph_2024_04_7{{"Changing the text of a React component popup tooltip from a library, purely using CSS. Hiding the text with `visible: hidden`. Adding a `:before` pseudo-class with `visible: visible; content: ''; margin-bottom: -20px"}}:::child
            softorium_graph_2024_04_7 --> softorium_graph_2024_04_8{{"Refactoring of the settings saving system. All settings were unified into one table with a JSON column for a unified interface, and simplicity of saving these settings on the client. All JSON fields were checked for existence before receiving, since when changing their structure, old saved settings might be broken"}}:::child
            softorium_graph_2024_04_8 --> softorium_graph_2024_04_9{{"Communication with the customer regarding deadlines, their delays and reasons "}}:::child
            softorium_graph_2024_04_9 --> softorium_graph_2024_04_10{{"Refactoring. Changing page components from dash.DataTable to html table with standard Input components"}}:::child
            softorium_graph_2024_04_10 --> softorium_graph_2024_04_11{{"Analysis of SQL query execution plan, study of `cost` for each step"}}:::child
            softorium_graph_2024_04_11 --> softorium_graph_2024_04_12{{"Accelerate complex analytical queries by 3 times by building indexes in the database and eliminating unnecessary join conditions"}}:::child
        end

        subgraph softorium_graph_2024_05
            style softorium_graph_2024_05 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_05_1 --> softorium_graph_2024_05_2{{"Optimization of the execution flow of celery tasks, using `chain` and `group` instead of recursive creation of `AsyncResult` by countdown. The result was the creation of 1 celery task for a 5-minute task instead of 30, due to which the speed of query execution increased by 10% and memory usage from O(n) time became O(1)"}}:::child
            softorium_graph_2024_05_2 --> softorium_graph_2024_05_3{{"Changed the process of working with the customer's code. In the outsourcing company there was a rule that all work with the code is carried out in the company's repository, and if the customer has his own repository, it is updated from it. When working with one customer who was immersed in the technical part, I, together with the project manager, insisted on changing the process so that the customer could clearly see all the work, merge requests and code reviews. This not only helped to increase trust in us, but also saved money later since I was promoted to project lead and became the only developer after code reviews that were ineffective from the customer's point of view"}}:::child
            softorium_graph_2024_05_3 --> softorium_graph_2024_05_4{{"Link celery worker container to the image that the application uses, to avoid re-build"}}:::child
            softorium_graph_2024_05_4 --> softorium_graph_2024_05_5{{"Creating a CI/CD process to deploy a docker-compose file to gitlab"}}:::child
            softorium_graph_2024_05_5 --> softorium_graph_2024_05_6{{"Resolving errors in gitlab ci when working with a git repository. Gitlab ci was copied from another project and gitlab runner moved from its environment to a local folder and tried to interact with a git repository to which it did not have access"}}:::child
            softorium_graph_2024_05_6 --> softorium_graph_2024_05_7{{"Adding 192.168.0.0/16 and 172.16.0.0/12 networks to pg_hba.conf for ci/cd process"}}:::child
        end

        subgraph softorium_graph_2024_06
            style softorium_graph_2024_06 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_06_1 --> softorium_graph_2024_06_2{{"Using null values ​​instead of default values"}}:::child
            softorium_graph_2024_06_2 --> softorium_graph_2024_06_3{{"Create migrations to update data instead of creating additional logic in the service. After entering dates '0001-01-01' from the API into the database, do not provide such an option in the service, but correct the data"}}:::child
            softorium_graph_2024_06_3 --> softorium_graph_2024_06_4{{"Merging 3 tables with logs into one and updating their filtering logic to use regular expressions. It is necessary that information is not lost and there is no unnecessary logic in the service for interaction with several tables"}}:::child
            softorium_graph_2024_06_4 --> softorium_graph_2024_06_5{{"Improving data quality and optimizing the database - removing duplicate indexes, which accelerated write operations by 40%"}}:::child
            softorium_graph_2024_06_5 --> softorium_graph_2024_06_6{{"Creating documentation with data requirements for analytical reports"}}:::child
            softorium_graph_2024_06_6 --> softorium_graph_2024_06_7{{"Standardization of report creation, clear division into stages: data truncating, data loading, validation, calculation, saving, logging of intermediate stages and definition of these operations in inherited classes"}}:::child
            softorium_graph_2024_06_7 --> softorium_graph_2024_06_8{{"Optimization of database queries - turning 2 queries in a for loop of 3000+ records into 2 for the entire function, and optimization of work from 40 minutes to 2 minutes"}}:::child
        end

        subgraph softorium_graph_2024_07
            style softorium_graph_2024_07 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_07_1 --> softorium_graph_2024_07_2{{"Dynamically loading `APIRouter` objects from modules in the `routers` package and including them in the `FastAPI` object"}}:::child
            softorium_graph_2024_07_2 --> softorium_graph_2024_07_3{{"Synchronize `collation` of databases between dev and prod environments so that filtering and searching operations give consistent results"}}:::child
            softorium_graph_2024_07_3 --> softorium_graph_2024_07_4{{"Rebuild invalidated indexes when collation changes"}}:::child
            softorium_graph_2024_07_4 --> softorium_graph_2024_07_5{{"Isolating tests from each other, testing upgrade and downgrade migrations, preventing side effects after test execution"}}:::child
            softorium_graph_2024_07_5 --> softorium_graph_2024_07_6{{"Create a script and ci/cd task to increase the version in `version.json` when accepting a merge request to the development or master branch"}}:::child
            softorium_graph_2024_07_6 --> softorium_graph_2024_07_7{{"git checkout into past commits to determine which changes caused the bug"}}:::child
            softorium_graph_2024_07_7 --> softorium_graph_2024_07_8{{"Combined all database operations within a single API endpoint into a transaction to ensure operation atomicity"}}:::child
            softorium_graph_2024_07_8 --> softorium_graph_2024_07_9{{"Using Explain Analyze to speed up SQL queries. Building indexes on frequently used unique columns. Removing unnecessary join conditions. Replacing Inline expressions with constant ones"}}:::child
            softorium_graph_2024_07_9 --> softorium_graph_2024_07_10{{"Refactored business logic to use DataRepository interfaces to simplify testing by mocking interface's implementation"}}:::child
        end

        subgraph softorium_graph_2024_08
            style softorium_graph_2024_08 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_08_1 --> softorium_graph_2024_08_2{{"Created a cron task for automatic database backup (pd_dump + pg_restore)"}}:::child
            softorium_graph_2024_08_2 --> softorium_graph_2024_08_3{{"Revert changes with `git reset` and save changes to `stash`"}}:::child
            softorium_graph_2024_08_3 --> softorium_graph_2024_08_4{{"Saving `git stash` to a separate file, transferring to a flash drive and using on another PC"}}:::child
        end

        subgraph softorium_graph_2024_09
            style softorium_graph_2024_09 fill:#F5D7E3, stroke:#D2D0BA, color:#ffffff, font-size:8pt

            softorium_graph_2024_09_1 --> softorium_graph_2024_09_2{{"Code review and assessment of the grade of candidates for vacancies"}}:::child
            softorium_graph_2024_09_2 --> softorium_graph_2024_09_3{{"Speed ​​up query with filtering by uuid by 20% by changing database index from btree to hash"}}:::child
            softorium_graph_2024_09_3 --> softorium_graph_2024_09_4{{"Creating plotly reports - pie charts, histograms, revenue dynamics, shelf share by suppliers"}}:::child
            softorium_graph_2024_09_4 --> softorium_graph_2024_09_5{{"Concealed the company's client data to create a service show case"}}:::child
        end
    end
```
