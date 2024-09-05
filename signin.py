import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
class signin: 
    def __init__(self):
        self.username=None
        self.password=None
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='Aswin@123', host='localhost', database='Inventory')
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    def log(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        role = self.get_user_role(self.username,self.password)

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.cnx:
            self.cnx.close()

    def get_user_role(self, username, password):
        try:
            self.connect()
            query = "SELECT role FROM management WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            role = self.cursor.fetchone()
            if role:
                return role[0]
        except mysql.connector.Error as err:
            print("An error occurred:", err)
        finally:
            self.disconnect()
        return None
    
    def add_manager(self):
        if input("Are you sure you want to add a manager? (y/n)").lower() == "y":
            manager_name = input("Enter manager's username: ")
            manager_password = input("Enter manager's password name: ")
            role = input("Enter role : ")
            try:
                self.connect()
                query = "INSERT INTO management (username,password,role) VALUES (%s, %s, %s)"
                self.cursor.execute(query, (manager_name,manager_password,role))
                self.cnx.commit()
                print("Manager added successfully.")
            except mysql.connector.Error as err:
                print("An error occurred:", err)
            finally:
                self.disconnect()
sig=signin()