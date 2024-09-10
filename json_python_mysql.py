import json
import mysql.connector
from mysql.connector import Error

taxables = []

with open('taxables.json', 'r') as jsonFile:
    jsonDict = json.load(jsonFile)
    for record in jsonDict:
        taxable = (record["index"], record["item"], record["cost"], record["tax"], record["total"])
        taxables.append(taxable)

host = '*********.us-east-1.rds.amazonaws.com'
database = 'training'
user = #'username here'
password = #'password here'

try:
    connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
    if connection.is_connected():
        cursor = connection.cursor()

        sql =   """
                INSERT INTO TAXABLES (Id, Item, Cost, Tax, Total)
                VALUES (%s, %s, %s, %s, %s);
                """

        result = cursor.executemany(sql, taxables)
        connection.commit()
        cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection to MySQL db closed")



