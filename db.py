import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="alby1234"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Res1")