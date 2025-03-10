class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name: ")
item1.item_price = int(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

print("\nItem 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name: ")
item2.item_price = int(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))


print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${total_cost}")
