class MobileStoreManagement:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin"},
            "user": {"password": "user"}
        }
        self.products = {
            1: {"name": "Apple", "price": 10, "color": "Red"},
            2: {"name": "Xiaomi", "price": 30, "color": "Green"},
            3: {"name": "Samsung", "price": 20, "color": "Blue"},
            # Add more products as needed
        }
        self.user_orders = {}

    def main_menu(self, username):
        if username == 'admin':
            self.admin_panel()
        else:
            self.user_panel()
        print()

    # -------------------------------------Admin------------------------------------------------------
    def admin_panel(self):
        print()
        print("**********WELCOME TO ADMIN PANEL**********")

        while True:

            print("a. Logout")
            print()

            choice = input("Enter your choice: ")
            if choice == 'a':
                print("******YOU ARE SUCCESSFULLY LOGGED OUT******")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    # ---------------------------------------User Start----------------------------------------------------
    def user_panel(self):
        print()
        print("**********WELCOME AS AN USER **********")
        while True:

            print("\nUser Panel:")
            print("a. Place Order")
            print("b. Logout")
            print()
            choice = input("Enter your choice: ")

            if choice == 'a':
                self.place_order()
            elif choice == 'b':
                print()
                print("****YOU ARE SUCCESSFULLY LOGGED OUT****")
                return
            else:
                print("Invalid choice. Please enter a valid option.")


    def place_order(self):
        print("Available Products:")
        for product_id, product_info in self.products.items():
            print(f"{product_id}. {product_info['name']} - Price: ${int(product_info['price'])} - Color: {product_info['color']}")

        print()
        product_choice = input("Enter the product ID to place an order: ")
        if product_choice.isdigit():
            product_id = int(product_choice) #must change the datatype to int
            if product_id in self.products:
                quantity = int(input("Enter the Quantity :"))
                if quantity > 0:
                    if product_id in self.user_orders:
                        self.user_orders[product_id] += quantity
                        print("Quantity Updated")
                    else:
                        self.user_orders[product_id] = quantity
                        print(f"Order placed: {quantity} {self.products[product_id]['name']}")
                else:
                    print("Invalid quantity. Quantity must be greater than 0.")
            else:
                print("Invalid product ID")
        else: print("Invalid input. Please enter a numeric product ID.")

# -----------------------------------------User End--------------------------------------------------


if __name__ == "__main__":
    mobile_store_system = MobileStoreManagement()

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if mobile_store_system.users.get(username) and mobile_store_system.users[username]["password"] == password:
            mobile_store_system.main_menu(username)
        else:
            print("Invalid username or password.")