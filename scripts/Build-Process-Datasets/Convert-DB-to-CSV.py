import os
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host='',
  user='',
  password='',
  port=3306,
  database=''
)

# Get data
sql = "SELECT * FROM persons;"
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()

df = pd.DataFrame()
for x in myresult:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_csv('sql-data.csv')
