import requests
from pymysql import connect,cursors

# API settings
api_url = "https://api.wildberries.ru/api/v1/statistics/advertising"
api_key = "your_api_key"
headers = {"X-Api-Key": api_key}

# MySQL settings
mysql_config = {
    "host": "localhost",
    "user": "your_user",
    "password": "your_password",
    "database": "your_database"
}

# Connect to MySQL
connection = connect(**mysql_config)
cursor = connection.cursor()

# Get data from Wildberries API
response = requests.get(api_url, headers=headers)
data = response.json()

# Insert data into MySQL
table_name = "your_table_name"
for item in data:
    columns = ", ".join(item.keys())
    values = ", ".join(["%s"] * len(item))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    cursor.execute(insert_query, tuple(item.values()))

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()