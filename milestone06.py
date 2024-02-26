class ItemToPurchase():
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0

    def return_total(self, item_price, item_quantity):
        total = "{:.2f}".format(float(self.item_price) * float(self.item_quantity))
        return total


    def print_item_cost(self, item_name, item_price, item_quantity):
        total = "{:.2f}".format(float(self.item_price) * float(self.item_quantity))
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}')

def get_item_name():
    item_name = str(input("Enter item name: "))
    return item_name

def get_item_description():
    item_description = input("Enter item description: ")
    return item_description

def get_item_price():
    item_price = float(input("Enter item price: "))
    return item_price

def get_item_quantity():
    item_quantity = int(input("Enter item quantity: "))
    return item_quantity

class ShoppingCart():
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2001"
        self.cart_items = []
    
    def add_item(self, item):
        item.item_name = get_item_name()
        item.item_price = "{:.2f}".format(get_item_price())
        item.item_description = input("Enter item description: ")
        item.item_quantity = get_item_quantity()
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
            else:
                print("Item not found in cart. Nothing removed.")

    def modify_item(self, modify):
        modify.item_name = input("Enter item name to modify: ")
        for item in self.cart_items:
            if modify.item_name == item.item_name:
                if item.item_description == "none" or item.item_quantity == 0 or item.item_price == 0:
                    item.item_price = "{:.2f}".format(get_item_price())
                    item.item_description = input("Enter item description: ")
                    item.item_quantity = get_item_quantity()
                else:
                    return
            else:
                print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        total_quantity = 0
        for items in self.cart_items:
            total_quantity = total_quantity + items.item_quantity
        return total_quantity

    
    def get_cost_of_cart(self):
        total = 0.00
        if self.get_num_items_in_cart() > 0:
            for items in self.cart_items:
                item_total = float("{:.2f}".format(float(items.item_price) * float(items.item_quantity)))
                total = "{:.2f}".format(float(total) + item_total)
            print(f"${total}")
        else:
            print("SHOPPING CART IS EMPTY.")
        return
    
    def print_totals(self):
        print(f"{self.customer_name} - {self.current_date}")
        print(f"Number of items: {self.get_num_items_in_cart}")
        for items in self.cart_items:
            item_total = float("{:.2f}".format(float(items.item_price) * float(items.item_quantity)))
            print(f"{items.item_name} {items.item_quantity} @ ${items.item_price} = {item_total}")
        print(self.get_cost_of_cart())

    def print_descriptions(self):
        print(f"{self.customer_name} - {self.current_date}")
        print("Item Descriptions")
        for items in self.cart_items:
            print(f"{items.item_name}: {items.item_description}")

    
shoppingCart = ShoppingCart()
shoppingCart.customer_name = input("Enter Customer Name: ")
shoppingCart.current_date = input("Enter the current date: ")
item = ItemToPurchase()
shoppingCart.add_item( item)
print(len(shoppingCart.cart_items))
item_name = str(input("Enter item name to remove: "))
shoppingCart.remove_item(item_name)
print(len(shoppingCart.cart_items))
modify = ItemToPurchase()
shoppingCart.modify_item(modify)
print(shoppingCart.get_num_items_in_cart())
print(shoppingCart.get_cost_of_cart())




# def menu(shoppingCart):
#     menu = print("MENU\na - a - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit")
#     option = ""
#     while option != "q":
#         menu
#         option = input("Choose an option: ")
#         if option == "a":
#             shoppingCart.add_item(ItemToPurchase)
            
#     if option == "r":
#         print(len(shoppingCart.cart_items))
#         item_name = str(input("Item to remove: "))
#         shoppingCart.cart_items = shoppingCart.remove_item(item_name)
#         return shoppingCart.cart_items
        
# def main():
#     shoppingCart = ShoppingCart()
#     shoppingCart.customer_name = input("Enter customer name: ")
#     shoppingCart.current_date = input("Enter current date: ")
#     menu(shoppingCart)

# main()
