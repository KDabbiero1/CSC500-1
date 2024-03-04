from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart

def print_menu(shoppingCart):
    option = input("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\nChoose an option: ")
    if option == "q":
        return
    while option != "q":
        if option == "a":
            item = ItemToPurchase()
            shoppingCart.add_item(item)
            option = input("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\nChoose an option: ")
        elif option == "r":
            item_name = str(input("Enter item name to remove: "))
            shoppingCart.remove_item(item_name)
            option = input("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\nChoose an option: ")
        elif option == "c":
            modify = ItemToPurchase()
            shoppingCart.modify_item(modify)
            option = input("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\nChoose an option: ")
        elif option == "i":
            shoppingCart.print_descriptions()
            option = input("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\nChoose an option: ")
        elif option == "o":
            shoppingCart.print_totals()
            option = input("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\nChoose an option: ")
    return

def main():
    shoppingCart = ShoppingCart()
    shoppingCart.customer_name = input("Enter Customer Name: ")
    shoppingCart.current_date = input("Enter the current date: ")

    print_menu(shoppingCart)

if __name__ == "__main__":
    main()