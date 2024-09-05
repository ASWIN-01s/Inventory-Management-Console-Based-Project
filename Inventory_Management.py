import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform
import Database
import View
import model.signin as signin

class InventoryManagement:
    def __init__(self):
        pass

    def clrscreen(self):
        if platform.system() == "Windows":
            print(os.system("cls"))

    def run(self):
        Database.data.create_database()
        Database.data.create_tables()

    def login(self):
        self.clrscreen()
        signin.sig.log()
        role = signin.sig.get_user_role(signin.sig.username, signin.sig.password)
        if role:
            self.run()
            self.show_inventory_management_menu(role)
        else:
            print("Login failed. Invalid username or password.")


    def show_inventory_management_menu(self, role):
        while True:
            self.clrscreen()
            print("\t\t\t Inventory Management\n")
            print("+===================================================================+")
            print("+  1. Purchase Management")
            print("+  2. Sales Management")
            print("+  3. Inventory Management")
            if role == "admin":
                print("+  4. Add Inventory Manager")
                print("+  5. Signout")

            if role in ['manager','staff']:
                print("+  4. Signout")

            print("+===================================================================+")
            choice = int(input("Enter Choice between 1 to 5 -------> : "))
            if choice == 1:
                View.menu.MenuPurchases()
            elif choice == 2:
                View.menu.MenuSales()
            elif choice == 3:
                View.menu.MenuInventory()
            elif role == "admin" and choice == 4:
                signin.sig.add_manager()
            elif choice == 5 and role == "admin":
                break
            elif choice == 4 and role in ['manager','staff']:
                break
            
           
            else:
                print("Wrong Choice.....Enter Your Choice again")
                x = input("Press any key to continue: ")

    

im = InventoryManagement()
im.login()
