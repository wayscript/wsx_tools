import os
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host='lcpbq9az4jklobvq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
  user='srwmp6imz2v547os',
  password=os.environ.get('password'),
  port=3306,
  database='c9h0n4i2bk671ofb'
)

# Get data
sql = "SELECT * FROM earnings;"
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult)

df = pd.DataFrame()
for x in myresult:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_html('sql-data.html')
