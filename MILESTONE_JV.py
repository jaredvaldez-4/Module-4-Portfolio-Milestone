# -*- coding: utf-8 -*-
"""
Created on Mon Jan 7 22:08:53 2026

@author: jared
"""

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

"""
OUTPUT OUTPUT
"""

item1 = ItemToPurchase()


print("---- Item 1 ---- ")
item1.item_name = input("Please enter the item name:\n")
item1.item_price = int(input("Now enter the item price:\n"))
item1.item_quantity = int(input("What is the item quantity:\n"))

item2 = ItemToPurchase()
print("\n----  Item 2----  ")
item2.item_name = input("Please enter the item name:\n")
item2.item_price = int(input("Now enter the item price:\n"))
item2.item_quantity = int(input("What is the item quantity:\n"))



print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${total}")
