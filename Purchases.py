import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform
from tabulate import tabulate


class Purchases:
    def __init__(self):
        self.cnx = None
        self.cursor = None

    def connect(self):
        self.cnx = mysql.connector.connect(user='root', password='Aswin@123', host='localhost', database='Inventory')
        self.Cursor = self.cnx.cursor()

    def clrscreen(self):
        if platform.system() == "Windows":
            print(os.system("cls"))

    def insertData(self):
        try:
            self.connect()
            ProductCode = input("Enter Product Code : ")
            ProductName = input("Enter Product Name : ")
            print("Enter Date of Purchase (Date/Month and Year separately) : ")
            DD = int(input("Enter Date : "))
            MM = int(input("Enter Month : "))
            YY = int(input("Enter Year : "))
            PurchaseDate = date(YY, MM, DD)
            PurchasePrice = int(input("Enter Product Price : "))
            ProductStock = int(input("Enter Quantity purchased : "))
            Qry = ("INSERT INTO Purchases VALUES (%s, %s, %s, %s, %s)")
            data = (ProductCode, ProductName, PurchaseDate, PurchasePrice, ProductStock)
            self.Cursor.execute(Qry, data)
            print("Record Inserted.")
            #Qry1 = ("INSERT INTO Inventory(ProductCode, ProductName, PurchaseDate, PurchasePrice) VALUES(%s, %s, %s, %s)")
            #data1 = (ProductCode, ProductName, PurchaseDate, PurchasePrice)
            #self.Cursor.execute(Qry1, data1)
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

    def deleteData(self):
        try:
            self.connect()
            ProductCode = input("Enter Product Code to be deleted from the Purchases : ")
            Qry = ("""DELETE FROM Purchases WHERE ProductCode = %s""")
            del_rec = (ProductCode,)
            self.Cursor.execute(Qry, del_rec)
            print(self.Cursor.rowcount, "Record(s) Deleted Successfully.")
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
            PCode = input("Enter Product Code to be searched from the Purchases : ")
            query = ("SELECT * FROM Purchases WHERE ProductCode like '%{}%'".format(PCode))
            self.Cursor.execute(query)
            Rec_count = 0
            for (ProductCode, ProductName, PurchaseDate, PurchasePrice, ProductStock) in self.Cursor:
                Rec_count += 2
                print("=============================================================")
                print("Product Code : ", ProductCode)
                print("Product Name : ", ProductName)
                print("Purchased on : ", PurchaseDate)
                print("Price of Product : ", PurchasePrice)
                print("Product in Stock : ", ProductStock)
                print("=============================================================")
                if Rec_count % 2 == 0:
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
            self.cnx.close()
    def searchData2(self):
        try:
            self.connect()
            query = ("SELECT * FROM purchases")
            self.Cursor.execute(query)
            myresult = self.Cursor.fetchall()
            print(tabulate(myresult, headers=['ProductCode', 'ProductName', 'PurchaseDate', 'PurchasePrice', 'ProductStock'], tablefmt='psql'))
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
            self.connect()
            ProductCode = input("Enter Product Code to be updated from the Purchases : ")
            query = ("SELECT * FROM Purchases WHERE ProductCode = %s ")
            rec_srch = (ProductCode,)
            print("Enter new data")
            ProductName = input("Enter Product Name : ")
            print("Enter Date of Purchase (Date/Month and Year separately) : ")
            DD = int(input("Enter Date : "))
            MM = int(input("Enter Month : "))
            YY = int(input("Enter Year : "))
            PurchaseDate = date(YY, MM, DD)
            PurchasePrice = int(input("Enter Product Price : "))
            ProductStock = int(input("Enter Quantity purchased : "))
            Qry = ("UPDATE Purchases SET ProductName=%s, PurchaseDate=%s, PurchasePrice=%s, ProductStock=%s  WHERE ProductCode=%s")
            data = (ProductName, PurchaseDate, PurchasePrice, ProductStock, ProductCode)
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
pur=Purchases()
