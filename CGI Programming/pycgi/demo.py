#!C:\Users\ACER\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\r\n\r\n")

import mysql.connector

# Establish a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="COLLEGEERP"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE COLLEGEERP")

# mycursor.execute("CREATE TABLE STUDENT(NAME VARCHAR(25),EMAIL VARCHAR(30))")
sql = "INSERT INTO STUDENT (name, email) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql,val)
mydb.commit()

# Close the database connection
mydb.close()

print('''
      <!DOCTYPE html>
<html>
<head>
    <title>Database Form Example</title>
</head>
<body>
     <form action="/pycgi/FormValidation.py" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <input type="submit" value="Submit">
     </form>
</body>
</html>
      
      ''')