
# represents an item in a store, can increase, decrease or apply a discount to itself
class Item:

    # an item has name and price
    def __init__(self, name, price, buyingPrice):
        self.name = name
        self.price = price
        self.buyingPrice = buyingPrice# this is only used for when you are buying items but u increase/decrease/discount the price of an item so it does not change


    # increase price of an item
    def increasePrice(self, amount):
        self.price = self.price + amount
        print( str(self.name) + " price increased")



    # decrease price of an item
    def decreasePrice(self, amount):
        # make sure decreasing does not give a negative price
        if (self.price - amount < 0):
            print("\nCannot decrease price this much. Price decrease cancelled.\n")
        else:
            self.price = self.price - amount
            print( str(self.name) + "price decreased")



    # enter the percentage of discount to give
    def addDiscount(self, discount):
        discountAmount = (discount/100) * self.price
        newPrice = self.price - discountAmount
        # make sure it is a sensible discount that does not give a negative price
        if (newPrice < 0):
            print("\nCannot apply this much discount. Discount cancelled.\n")
        else:
            self.price = newPrice
            print("Discount of " + str(discount) + "% was applied to " + str(self.name))



    def __str__(self):
        return "Item: " + str(self.name) + "\t Selling Price: $" + str(format(float(self.price), '.2f')) + "\t Buying Price: $" + str(format(float(self.buyingPrice), '.2f'))















