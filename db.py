import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='eivind',
    password='eivind123',
    database='MiniSOC'
)

cursor = db.cursor(dictionary=True)