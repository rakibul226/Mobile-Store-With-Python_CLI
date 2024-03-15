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
            print("b. My Orders")
            print("c. View Order Details")
            print("d. Cancel Order")
            print("e. Update Order")
            print("f. Logout")
            print()
            choice = input("Enter your choice: ")

            if choice == 'a':
                self.place_order()
            elif choice == 'b':
                self.my_orders()
            elif choice == 'c':
                self.view_order_details()
            elif choice == 'd':
                self.cancel_order()
            elif choice == 'e':
                self.update_order()
            elif choice == 'f':
                print()
                print("****YOU ARE SUCCESSFULLY LOGGED OUT****")
                return
            else:
                print("Invalid choice. Please enter a valid option.")


    def place_order(self):      #-------------------------user place order
        print("Available Products:")
        for product_id, product_info in self.products.items():
            print(f"{product_id}. {product_info['name']} - Price: ${int(product_info['price'])} - Color: {product_info['color']}")

        print()
        product_choice = input("Enter the product ID to place an order: ")
        if product_choice.isdigit():
            product_id = int(product_choice) #must change the datatype to int
            if product_id in self.products:
                quantity_ = input("Enter the Quantity :")
                if quantity_.isdigit():
                     quantity = int(quantity_)
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
                    print("Invalid input. Quantity must be a number.")
            else:
                print("Invalid product ID")
        else: print("Invalid input. Please enter a numeric product ID.")

    def my_orders(self):   #-------------------------user view placed order
        if self.user_orders:
            print("My Orders:")
            for product_id, quantity in self.user_orders.items():
                product_name = self.products[product_id]['name']
                print(f"{product_id}. {product_name} ({quantity})")
        else:
            print("You have no orders yet.")

    def view_order_details(self): #--------------------user view order details
        if self.user_orders:
            print("Available Orders:")
            for product_id in self.user_orders:
                product_name = self.products[product_id]['name']
                print(f"{product_id}. {product_name}")

            print()
            order_id = input("Enter the order ID to view details: ")
            if order_id.isdigit() and int(order_id) in self.user_orders:
                product_id = int(order_id)
                product_info = self.products[product_id]
                print(
                    f"{product_id}. Name:{product_info['name']}  Price:${product_info['price']}  Color:{product_info['color']}")
            else:
                print("Invalid order ID.")
        else:
            print("You have no orders yet.")

    def cancel_order(self):   #------------------user cancle placed order
        if self.user_orders:
            print("Available Orders:")
            for product_id in self.user_orders:
                product_name = self.products[product_id]['name']
                print(f"{product_id}. {product_name}")

            print()
            order_id = input("Enter the order ID to cancel: ")
            if order_id.isdigit() and int(order_id) in self.user_orders:
                product_id = int(order_id)
                del self.user_orders[product_id]
                print("Order canceled successfully.")
            else:
                print("Invalid order ID.")
        else:
            print("You have no orders yet.")

    def update_order(self):  #-----------------------------------user update order quantity
        if self.user_orders:
            order_id = input("Enter the order ID to update: ")
            if order_id.isdigit() and int(order_id) in self.user_orders:
                product_id = int(order_id)
                new_quantity = int(input("Enter the new quantity: "))
                if new_quantity > 0:
                    self.user_orders[product_id] = new_quantity
                    print("Order updated successfully.")
                else:
                    print("Invalid quantity.")
            else:
                print("Invalid order ID.")
        else:
            print("You have no orders yet.")


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