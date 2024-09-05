import mysql.connector
from mysql.connector import errorcode
from datetime import date
import os
import platform
from tabulate import tabulate

class Sales:
    def __init__(self):
        self.cnx = None
        self.cursor = None
        self.PCode = None
        self.SaleDate = None
        self.SalePrice = None
        
    def connect(self):
        self.cnx = mysql.connector.connect(user='root', password='Aswin@123', host='localhost', database='Inventory')
        self.Cursor = self.cnx.cursor()

    def clrscreen(self):
        if platform.system() == "Windows":
            print(os.system("cls"))

    def insertData(self):
        try:
            self.connect()
            self.PCode = input("Enter Product Code : ")
            ProductName = input("Enter Product Name : ")
            print("Enter Date of Sales (Date/Month and Year) separately) : ")
            DD = int(input("Enter Date : "))
            MM = int(input("Enter Month : "))
            YY = int(input("Enter Year : "))
            self.SaleDate = date(YY, MM, DD)
            self.SalePrice = int(input("Enter Sales Price : "))
            Qry = ("INSERT INTO Sales VALUES(%s, %s, %s, %s)")
            data = (self.PCode, ProductName, self.SaleDate, self.SalePrice)
            self.Cursor.execute(Qry, data)
            print("Record Inserted.")
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
            self.cnx.close()

    def updateInventory(self):
        try:
            self.connect()
            Qry1 = "UPDATE Inventory SET SalesDate=%s, SalesPrice=%s WHERE ProductCode=%s"
            data1 = (self.SaleDate, self.SalePrice, self.PCode)
            self.Cursor.execute(Qry1, data1)
            print("Inventory Updated.")
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

    def deleteData(self):
        try:
            self.connect()
            self.PCode = input("Enter Product Code to be deleted from the Sales : ")
            Qry = ("DELETE FROM Sales WHERE ProductCode like '%{}%'".format(self.PCode))
            print("Record(s) Deleted Successfully.")
            self.Cursor.execute(Qry)
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
            self.cnx.close()

    def searchData1(self):
        try:
            self.connect()
            self.PCode = input("Enter Product Code to be searched from the Sales : ")
            query = ("SELECT * FROM Sales where ProductCode like '%{}%'".format(self.PCode))
            self.Cursor.execute(query)
            Rec_count = 0
            for(ProductCode, ProductName, SaleDate, SalePrice) in self.Cursor:
                Rec_count += 2
                print("=============================================================")
                print("Product Code : ", ProductCode)
                print("Product Name : ", ProductName)
                print("Date of Sale : ", SaleDate)
                print("Sale Price : ", SalePrice)
                print("=============================================================")
                if Rec_count % 2 == 0:
                    print(Rec_count, "Record(s) found")
                    input("Press any key to continue: ")
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
            self.connect()
            query = ("SELECT * FROM sales")
            self.Cursor.execute(query)
            myresult = self.Cursor.fetchall()
            print(tabulate(myresult, headers=['ProductCode', 'ProductName', ' SaleDate', 'SalePrice'], tablefmt='psql'))
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
            self.cnx.close()


    def updateData(self):
        try:
            ProductCode = input("Enter Product Code to be updated from the Sales : ")
            query = ("SELECT * FROM Sales WHERE ProductCode = %s")
            rec_srch = (ProductCode,)
            print("Enter new data")
            ProductName = input("Enter Product Name : ")
            print("Enter Date of Sales (Date/Month and Year separately) : ")
            DD = int(input("Enter Date : "))
            MM = int(input("Enter Month : "))
            YY = int(input("Enter Year : "))
            SaleDate = date(YY, MM, DD)
            SalePrice = input("Enter Sales Price : ")
            Qry = ("UPDATE Sales SET ProductName=%s, SaleDate=%s, SalePrice=%s WHERE ProductCode=%s")
            data = (ProductName, SaleDate, SalePrice, ProductCode)
            print(self.Cursor.rowcount, "Record(s) Updated Successfully.")
            self.Cursor.execute(Qry, data)
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
            self.cnx.close()
sal=Sales()

