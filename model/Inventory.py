import mysql.connector
from mysql.connector import errorcode
import os
from tabulate import tabulate

class Inventory:
    
    def __init__(self):
        self.cnx = None
        self.cursor = None

    def connect(self):
        self.cnx = mysql.connector.connect(user='root', password='Aswin@123', host='localhost', database='Inventory')
        self.Cursor = self.cnx.cursor()

    def clrscreen(self):
        print('\n' * 5)

    def searchData1(self):
        try:
            os.system('cls')
            self.connect()
            ProductCode = input("Enter Product Code to be searched from the Inventory : ")
            query = ("SELECT * FROM Inventory where ProductCode = %s")
            rec_srch = (ProductCode,)
            self.Cursor.execute(query, rec_srch)
            Rec_count = 0
            for (ProductCode, ProductName, PurchaseDate, SalesDate, PurchasePrice, SalesPrice) in self.Cursor:
                Rec_count += 2
                print("=============================================================")
                print("1.Product Code : ", ProductCode)
                print("2.Product Name : ", ProductName)
                print("3.Purchase Date : ", PurchaseDate)
                print("4.Sales Date : ", SalesDate)
                print("5.Purchase Price : ", PurchaseDate)
                print("6.Sales Price : ", SalesPrice)
                print("=============================================================")
                if Rec_count%2 == 0:
                    input("Press any key continue")
                    print(Rec_count, "Record(s) found")
                    self.clrscreen()
            self.cnx.commit()
            self.Cursor.close()
            self.cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            self.cnx.close()
    def searchData2(self):
        try:
            os.system('cls')
            self.connect()
            query = ("SELECT * FROM Inventory")
            self.Cursor.execute(query)
            myresult = self.Cursor.fetchall()
            print(tabulate(myresult, headers=['ProductCode','ProductName','PurchaseDate','SalesDate','PurchasePrice','SalesPrice'], tablefmt='psql'))
            print("Record(s) found")
            input("Press any key continue")
            self.clrscreen()
            self.cnx.commit()
            self.Cursor.close()
            self.cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.cnx.close()

inv=Inventory()
