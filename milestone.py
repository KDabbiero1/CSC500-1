class ItemToPurchase():
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def return_total(self, item_price, item_quantity):
        total = "{:.2f}".format(float(self.item_price) * float(self.item_quantity))
        return total


    def print_item_cost(self, item_name, item_price, item_quantity):
        total = "{:.2f}".format(float(self.item_price) * float(self.item_quantity))
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}')

def get_item_name():
   item_name = input("Enter item name: ")
   return item_name

def get_item_price():
    item_price = float(input("Enter item price: "))
    return item_price

def get_item_quantity():
    item_quantity = int(input("Enter item quantity: "))
    return item_quantity

def get_items():
    first_item = ItemToPurchase()
    first_item.item_name = get_item_name()
    first_item.item_price = "{:.2f}".format(get_item_price())
    first_item.item_quantity = get_item_quantity()

    second_item = ItemToPurchase()
    second_item.item_name = get_item_name()
    second_item.item_price = "{:.2f}".format(get_item_price())
    second_item.item_quantity = get_item_quantity()

    return first_item, second_item
    

first_item, second_item = get_items()
first_item.print_item_cost(first_item.item_name, first_item.item_price, first_item.item_quantity)
first_item_total = float(first_item.return_total(first_item.item_price, first_item.item_quantity))
second_item.print_item_cost(second_item.item_name, second_item.item_price, second_item.item_quantity)
second_item_total = float(second_item.return_total(second_item.item_price, second_item.item_quantity))
total = "{:.2f}".format(float(first_item_total) + float(second_item_total))
print(f"Total: ${total}")