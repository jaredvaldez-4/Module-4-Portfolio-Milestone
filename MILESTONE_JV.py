
"""
Created on Mon Jan 7 22:08:53 2026

@author: jared
"""
item_name = 0
item_price = 0
item_quanitity = 0

class ITMTWOPURCHASE:
    def __init__(self):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quanitity

    def print_item_cost(self):
        
        TOTALCOSTITEM = self.item_price * self.item_quantity
        
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${TOTALCOSTITEM}")

"""
OUTPUT OUTPUT
"""

item1 = ITMTWOPURCHASE()


print("---- Item 1 ---- ")
item1.item_name = input("Please enter the item name:\n")
item1.item_price = int(input("Now enter the item price:\n"))
item1.item_quantity = int(input("What is the item quantity:\n"))

item2 = ITMTWOPURCHASE()
print("\n----  Item 2----  ")
item2.item_name = input("Please enter the item name:\n")
item2.item_price = int(input("Now enter the item price:\n"))
item2.item_quantity = int(input("What is the item quantity:\n"))



print("\n------------- SUMMARY OF TOTAL COST ------------- ")
item1.print_item_cost()
item2.print_item_cost()

GRANDtotal = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

print(f"\nGRANDtotal: ${GRANDtotal:}")
