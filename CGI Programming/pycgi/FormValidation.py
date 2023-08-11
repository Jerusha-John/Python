#!C:\Users\ACER\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\r\n\r\n")

import cgi
import mysql.connector

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue("name")
email = form.getvalue("email")

# Validate and sanitize data (you should do more thorough validation)
if not name or not email:
    
    print("<html><body><p>Both name and email are required.</p></body></html>")
else:
    # Establish a connection to the database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="COLLEGEERP"
    )
    mycursor = mydb.cursor()

    # Insert data into the database
    sql = "INSERT INTO STUDENT (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql,val)   
    mydb.commit()

    # Close the database connection
    mydb.close()

    # print("Content-type: text/html\n")
    print("<html><body>")
    print("<h2>Data inserted successfully.</h2>")
    print("<p>Name: {0}</p>".format(name))
    print("<p>Email: {0}</p>".format(email))
    print("</body></html>")