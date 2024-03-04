class ShoppingCart():
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2001"
        self.cart_items = []
    
    def add_item(self, item):
        item.item_name = str(input("Enter item name: "))
        item.item_price = "{:.2f}".format(float(input("Enter item price: ")))
        item.item_description = input("Enter item description: ")
        item.item_quantity = int(input("Enter item quantity: "))
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for items in self.cart_items:
            if items.item_name == item_name:
                self.cart_items.remove(items)
                return
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modify):
        modify.item_name = str(input("Enter item name to modify: "))
        for item in self.cart_items:
            if modify.item_name == item.item_name:
                item.item_quantity = int(input("Enter new item quantity: "))
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
        print(f"Number of items: {self.get_num_items_in_cart()}")
        for items in self.cart_items:
            item_total = "{:.2f}".format(float(items.item_price) * float(items.item_quantity))
            print(f"{items.item_name} {items.item_quantity} @ ${items.item_price} = ${item_total}")
        print(self.get_cost_of_cart())

    def print_descriptions(self):
        print(f"{self.customer_name} - {self.current_date}")
        print("Item Descriptions")
        for items in self.cart_items:
            print(f"{items.item_name}: {items.item_description}")

