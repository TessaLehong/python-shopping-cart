def display_cart(cart):
    if not cart:
        print("Your cart is empty")
    else:
        print("Shopping Cart:")
        total_price = 0
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item['name']} - R{item['price']:.2f}")
            total_price += item['price']
        print(f"Total: R{total_price:.2f}")


def main():
    cart = {

        "Laptop": {
            "price": 12000.00,
            "quantity": 1
        },
        "Headphones": {
            "price": 600.00,
            "quantity": 2
        }

    }
    while True:
        print("\nShopping Cart Application")
        print("1. View Cart")
        print("2. Add Item to Cart")
        print("3. Remove Item From Cart")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_cart(cart)

        elif choice == "2":
            item_name = input("Enter item name: ").strip().lower()
            try:
                item_price = float(input("Enter item price: "))
                item_quantity = int(input("Enter quantity: "))

                if item_price < 0 or item_quantity <= 0:
                    print("\n Price and quantity must be positive numbers.\n")
                    continue

                if item_name in cart:
                    cart[item_name]['quantity'] += item_quantity
                else:
                    cart[item_name] = {'price': item_price, 'quantity': item_quantity}
                print(" Item added to cart.")

            except ValueError:
                print(" Invalid input. Please enter a valid number.")

        elif choice == "3":
            if not cart:
                print("Your cart is empty")
            else:
                display_cart(cart)
                try:
                    item_index = int(input("Enter the item number to remove: ")) - 1
                    if 0 <= item_index < len(cart):
                        removed_item = cart.pop(item_index)
                        print(f"Removed item: {removed_item['name']}")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "4":
            if cart:
                display_cart(cart)
                confirm = input("\nDo you want to proceed to checkout? (yes/no): ").strip().lower()
                if confirm == "yes":
                    print("\nPurchase confirmed! Thank you for shopping.")
                    cart.clear()
                else:
                    print("\nCheckout canceled.")
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please select a valid option.")


if __name__ == "__main__":
    main()
