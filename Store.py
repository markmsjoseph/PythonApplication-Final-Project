from Item import *


# represents a store with a bank account, and abailty to sell and buy items
class Store():

    # a store will have a name, it will show if there is a profit or a loss, and it will keep track of records made of sales and purchases
    def __init__(self, name, startCash):
        self.bankAccount = startCash
        self.name = name
        self.totalEarnings =0
        self.totalSpendings =0
        self.recordsOfTransactions = ""
        self.inventory =[]


    def buyItems(self, item, number):
        cash = 0
        for i in range(number):
            self.inventory.append(item)
            cash = cash + item.buyingPrice
        self.bankAccount = self.bankAccount - cash
        self.recordsOfTransactions = self.recordsOfTransactions + "\nPurchased " + str(number) + " " + str(item.name)
        print("Purchased " + str(number) + " items")


    def sellItems(self, item, number):
        if item not in self.inventory:
           print("\nYou do not have that many items to tell. Sale cancelled\n")
        else:
            num = self.inventory.count(item)
            if(number > num):
                print("\nYou do not have that many items to tell. Sale cancelled\n")
            else:
                cash = 0
                for i in range(number):
                    self.inventory.remove(item)
                    cash = cash + item.price
                self.bankAccount = self.bankAccount + cash
                self.recordsOfTransactions = self.recordsOfTransactions + "\nSold " + str(number) + " " + str(item.name)
                print("Sold " + str(number)  + " items")


    def checkStock(self):
        print("stock is " + str(len(self.inventory)) + " items")
        for i in range(len(self.inventory)):
            print(self.inventory[i])


    def checkTotalEarnings(self):
        print("Total income is " + str(self.totalEarnings))


    def checkTotalSpendings(self):
        print("Total spendings is " + str(self.totalSpendings))


    def checkBankAccount(self):
        if(self.bankAccount < 0):
            print( "Available Balance: " + str(self.bankAccount) + "\nAccount Overdrawn\n")
        else:
            print( "Available Balance: " + str(self.bankAccount))


    def checkTransactions(self):
        print( self.recordsOfTransactions)


    def __str__(self):
        return "\nStore's name is " + str(self.name) + "\nBank Balance: " + str(self.bankAccount) + \
               "\nMoney Earned: " + str(self.totalEarnings) + "\nMoney Spent: " + str(self.totalSpendings)\
                + "\nCurrent Inventory : " + str(len(self.inventory)) + " items" + "\n\n====Record Of Transactions==== " + str(self.recordsOfTransactions)






running = True
###################### make a store
response = input("Enter the store name\n")
store = Store(response, 2000)
print("You Have $2000 in the bank\n")

##############set up items


shoes = Item("shoes",100, 100)
store.buyItems(shoes, 3)

pants = Item("pants",50, 50)
store.buyItems(pants, 10)

shirts = Item("shirts",25, 25)
store.buyItems(shirts, 10)

while running:
    print("\nWhat do you want to do?\nCommands are:\n check bank/tran/spending/earnings/stock\n sell/buy shoes/pants/shirts\n discount shoes/pants/shirts\n increase/decrease shoe/shirt/pants price\n")

    reply = input("")

    if reply == "check bank":
        store.checkBankAccount()
    elif reply == "check tran":
        store.checkTransactions()
    elif reply == "check spending":
        store.checkTotalSpendings()
    elif reply == "check earnings":
        store.checkTotalEarnings()
    elif reply == "check stock":
        store.checkStock()

    elif reply == "buy shoes":
        amtshoes = input("How many shoes do u want\n")
        store.buyItems(shoes, int(amtshoes))
    elif reply == "buy pants":
        amtshoes = input("How many pants do u want\n")
        store.buyItems(pants, int(amtshoes))
    elif reply == "buy shirts":
        amtshoes = input("How many shirts do u want\n")
        store.buyItems(shirts, int(amtshoes))

    elif reply == "sell shoes":
        amtshoes = input("How many shoes \n")
        store.sellItems(shoes, int(amtshoes))
    elif reply == "sell pants":
        amtshoes = input("How many pants \n")
        store.sellItems(pants, int(amtshoes))
    elif reply == "sell shirts":
        amtshoes = input("How many shirts \n")
        store.sellItems(shirts, int(amtshoes))

    elif reply == "discount shoes":
        amtshoes = input("Enter discount amount eg. 10 \n")
        shoes.addDiscount(int(amtshoes))
    elif reply == "discount shirts":
        amtshoes = input("Enter discount amount eg. 10 \n")
        shirts.addDiscount(int(amtshoes))
    elif reply == "discount pants":
        amtshoes = input("Enter discount amount eg. 10 \n")
        pants.addDiscount(int(amtshoes))

    elif reply == "increase shoe price":
        amtshoes = input("Enter amount to increase price by eg. 10 \n")
        shoes.increasePrice(int(amtshoes))
    elif reply == "increase shirt price":
        amtshoes = input("Enter amount to increase price by eg. 10 \n")
        shirts.increasePrice(int(amtshoes))
    elif reply == "increase pants price":
        amtshoes = input("Enter amount to increase price by eg. 10 \n")
        pants.increasePrice(int(amtshoes))

    elif reply == "decrease shoe price":
        amtshoes = input("Enter amount to decrease price by eg. 10 \n")
        shoes.decreasePrice(int(amtshoes))
    elif reply == "decrease shirt price":
        amtshoes = input("Enter amount to decrease price by eg. 10 \n")
        shoes.decreasePrice(int(amtshoes))
    elif reply == "decrease pants price":
        amtshoes = input("Enter amount to decrease price by eg. 10 \n")
        shoes.decreasePrice(int(amtshoes))



    elif reply == "quit":
        running = False


print('DONE')

