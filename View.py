import model.Purchases as Purchases
import model.Sales as Sales
import model.Inventory as Inventory
import model.signin as signin
class MenuLib:
    @staticmethod
    def MenuPurchases():
        role= signin.sig.get_user_role(signin.sig.username, signin.sig.password)
        while True:
            Purchases.pur.clrscreen()
            print("\t\t\t Purchase Record Management\n")
            print("=================================================================")
            print("1. Add Purchase Record")
            print("2. Search Purchase Record")
            if role in ['admin', 'manager']:
                print("3. Delete Purchase Record")
                print("4. Update Purchase Record")
                print("5. Return to Main Menu")
            else:
                print("3. Return to Main Menu")
            print("=================================================================")
            choice = int(input("Enter Choice between 1 to 5 -------> : "))
            if choice == 1:
                Purchases.pur.insertData()
            elif choice == 2:
                print("1. Search Specific Purchase Record")
                print("2. Show All Purchase Record")
                w = int(input("Enter Option 1 or 2  :"))
                if w == 1:
                    Purchases.pur.searchData1()
                elif w == 2:
                    Purchases.pur.searchData2()
            elif choice == 3 and role in ['admin', 'manager']:
                Purchases.pur.deleteData()
            elif choice == 4 and role in ['admin', 'manager']:
                Purchases.pur.updateData()
            elif choice == 5 and role in ['admin', 'manager']:
                return
            elif choice ==3 and role in ['staff']:
                return

            
            else:
                print("Wrong Choice.....Enter Your Choice again")
                x = input("Enter any key to continue")
    @staticmethod
    def MenuSales():
        role= signin.sig.get_user_role(signin.sig.username, signin.sig.password)
        while True:
            Purchases.pur.clrscreen()
            print("\t\t\t Sales Record Management\n")
            print("=================================================================")
            print("1. Add Sales Record")
            print("2. Search Sales Record")
            if role in ['admin', 'manager']:
                print("3. Delete Sales Record")
                print("4. Update Sales Record")
                print("5. Return to Main Menu")
            else:
                print("3. Return to MainMenu")
            print("=================================================================")
            choice = int(input("Enter Choice between 1 to 5 ------> : "))
            if choice == 1:
                Sales.sal.insertData()
                Sales.sal.updateInventory()
            elif choice == 2:
                print("1. Search Specific Purchase Record")
                print("2. Show All Purchase Record")
                w=int(input("Enter Option 1 or 2  :"))
                if w==1:
                    Sales.sal.searchData1()
                elif w==2:
                    Sales.sal.searchData2()
            elif choice == 3 and role in ['admin', 'manager']:
                Sales.sal.deleteData()
            elif choice == 4 and role in ['admin', 'manager']:
                Sales.sal.updateData()
            elif choice == 5 and role in ['admin', 'manager']:
                return
            elif choice ==3 and role in ['staff']:
                return
            
            else:
                print("Wrong Choice.....Enter Your Choice again")
                x = input("Enter any key to continue")

    @staticmethod
    def MenuInventory():
        while True:
            Purchases.pur.clrscreen()
            print("\t\t\t Inventory Record Management\n")
            print("=================================================================")
            print("1. Search Specific Data From Inventory")
            print("2. Show All The Data From Inventory")
            print("3. Return to Main Menu")
            print("=================================================================")
            choice = int(input("Enter Choice between 1 to 3 ------> : "))
            if choice == 1:
                Inventory.inv.searchData1()
            elif choice == 2:
                Inventory.inv.searchData2()
            elif choice == 3:
                return
            else:
                print("Wrong Choice.....Enter Your Choice again")
                x = input("Enter any key to continue")
menu=MenuLib()