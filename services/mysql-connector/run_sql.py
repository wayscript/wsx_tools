# .secrets file should contain:
# DB_USERNAME and DB_PASSWORD

import os
import mysql.connector

mydb = mysql.connector.connect(
  host='',
  user=os.getenv('DB_USERNAME'),
  password=os.getenv('DB_PASSWORD'),
  port=3306,
  database=''
)

with open('query.sql', 'r') as f:
    mycursor = mydb.cursor()
    mycursor.execute(f.read())
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
