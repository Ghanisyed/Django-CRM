#install mysql on your computer
#https://dev.mysql.com/downlosds/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ghani@000'
)


#prepare a cursor object

cursorObj = dataBase.cursor()

#create a databse'
cursorObj.execute("CREATE DATABASE elderco")

print("All Done!")