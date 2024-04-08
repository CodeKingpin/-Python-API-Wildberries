
##  Python API Wildberries



# ENG

A Python script that utilizes the Wildberries API to access and retrieve data from the Wildberries online retail platform. The script allows users to programmatically interact with the Wildberries API to perform various actions such as searching for products, retrieving product details, and managing orders. It provides a convenient and efficient way to access and retrieve data from the Wildberries platform, making it easier for developers to integrate Wildberries data into their applications. The script is customizable and can be easily adapted to suit the specific needs and requirements of individual users. With the Wildberries API Python script, users can efficiently interact with the Wildberries platform and access a wide range of data and information.




## Features

This script is used to fetch advertising statistics data from Wildberries API and store it in a MySQL database using the requests and pymysql libraries. Here are some features of the script:

-    It imports the required libraries requests and pymysql to make HTTP requests to the Wildberries API and interact with the MySQL database, respectively.
-    It sets up the API and MySQL settings, including the API endpoint, API key, MySQL host, user, password, and database name.
-    It connects to the MySQL database using the pymysql library and creates a cursor object to execute SQL queries.
-    It sends a GET request to the Wildberries API using the requests library and retrieves the response in JSON format.
-    It iterates over the data received from the API and constructs an INSERT query to insert the data into the MySQL database.
-    It uses the cursor object to execute the INSERT query and passes the values to be inserted as a tuple.
-    It commits the changes to the database and closes the cursor and connection objects.

This script is useful for fetching advertising statistics data from Wildberries API and storing it in a MySQL database for further analysis or reporting. However, it is a basic script and might need to be modified to fit specific requirements, such as adding error handling, modifying the API endpoint or parameters, or adjusting the database schema.

Additionally, it is recommended to use task scheduler like cron in Linux or Task Scheduler in Windows to run this script daily or as per the requirement.


# RUS

Скрипт на Python, использующий API Wildberries для доступа и получения данных с платформы интернет-магазина Wildberries. Скрипт позволяет пользователям программно взаимодействовать с API Wildberries для выполнения различных действий, таких как поиск товаров, получение информации о товарах и управление заказами. Он обеспечивает удобный и эффективный способ доступа и получения данных с платформы Wildberries, облегчая разработчикам интеграцию данных Wildberries в свои приложения. Скрипт является настраиваемым и может быть легко адаптирован под конкретные нужды и требования отдельных пользователей. С помощью скрипта Wildberries API Python пользователи могут эффективно взаимодействовать с платформой Wildberries и получать доступ к широкому спектру данных и информации.


## Характеристики

 
Этот скрипт используется для получения данных статистики рекламы из API Wildberries и хранения их в базе данных MySQL с помощью библиотек requests и pymysql. Вот некоторые особенности скрипта:
- Импортирует необходимые библиотеки requests и pymysql для выполнения HTTP-запросов к API Wildberries и взаимодействия с базой данных MySQL, соответственно.
- Устанавливает настройки API и MySQL, включая конечную точку API, ключ API, хост MySQL, пользователя, пароль и имя базы данных.
- Он подключается к базе данных MySQL с помощью библиотеки pymysql и создает объект курсора для выполнения SQL-запросов.
- Отправляет GET-запрос к API Wildberries с помощью библиотеки requests и получает ответ в формате JSON.
- Он перебирает данные, полученные от API, и строит запрос INSERT для вставки данных в базу данных MySQL.
- Для выполнения запроса INSERT используется объект курсора, а значения для вставки передаются в виде кортежа.
- Он фиксирует изменения в базе данных и закрывает объекты курсора и соединения.
Этот сценарий полезен для получения данных статистики рекламы из API Wildberries и хранения их в базе данных MySQL для дальнейшего анализа или создания отчетов. Тем не менее, это базовый сценарий, который может потребовать доработки под конкретные требования, например, добавления обработки ошибок, изменения конечной точки или параметров API или корректировки схемы базы данных.
Кроме того, рекомендуется использовать планировщик задач, например cron в Linux или Task Scheduler в Windows, чтобы ru
