import mysql.connector

class Database:
    @staticmethod
    def create_database():
        cnx = mysql.connector.connect(user='root', password='Aswin@123', host='localhost')
        Cursor = cnx.cursor()
        Cursor.execute("CREATE DATABASE IF NOT EXISTS Inventory")
        Cursor.close()
        cnx.close()

    @staticmethod
    def create_tables():
        cnx = mysql.connector.connect(user='root', password='Aswin@123', host='localhost', database='Inventory')
        Cursor = cnx.cursor()
        Cursor.execute("CREATE TABLE IF NOT EXISTS Purchases(ProductCode int(2) Primary Key, ProductName varchar(20), PurchaseDate Date, PurchasePrice int(3), ProductStock int(2))")
        Cursor.execute("CREATE TABLE IF NOT EXISTS Sales(ProductCode int(2) Primary Key, ProductName varchar(20), SalesDate Date, SalesPrice int(3))")
        Cursor.execute("CREATE TABLE IF NOT EXISTS Inventory(ProductCode int(2) Primary Key, ProductName varchar(20), PurchaseDate Date, SalesDate Date, PurchasePrice int(3), SalesPrice int(3))")
        Cursor.execute("CREATE TABLE IF NOT EXISTS management(id int(2) Primary Key, username varchar(20), password varchar(20),role varchar(20))")
        Cursor.close()
        cnx.close()
data=Database()

