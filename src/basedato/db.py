from peewee import MySQLDatabase

#local
db = MySQLDatabase(
    "crud-db",
    user="root",
    password="",
    host="localhost",
    port=3306
)
