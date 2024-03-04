class ItemToPurchase():
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self, item_name, item_price, item_quantity):
        total = "{:.2f}".format(float(self.item_price) * float(self.item_quantity))
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}')
