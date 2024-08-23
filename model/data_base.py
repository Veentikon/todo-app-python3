import sqlite3

# The returned Connection object connection represents the connection to the on-disk database.
connection = sqlite3.connect("toDoApp.db")

# In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor.
dbCursor = connection.cursor()

# Create database table for tasks
dbCursor.execute("CREATE TABLE tasks(text, compete?)")


