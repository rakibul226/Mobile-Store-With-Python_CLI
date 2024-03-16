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
            print("\nAdmin Panel:")
            print("a. View Product")
            print("b. Add Product")
            print("c. Update Product")
            print("d. Remove Product")
            print("e. Logout")
            print()

            choice = input("Enter your choice: ")
            print()

            if choice == 'a':
                self.view_products()
                print()
            elif choice == 'b':
                self.add_product()
            elif choice == 'c':
                self.update_product()
            elif choice == 'd':
                self.remove_product()
            elif choice == 'e':
                print("******YOU ARE SUCCESSFULLY LOGGED OUT******")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def view_products(self):
        print("Products:")
        if not self.products:  # Check if there are no products
            print("No products available.")
        else:
            for product_id, product_info in self.products.items():
                print(
                    f"ID:{product_id} Name:{product_info['name']} - Price:${int(product_info['price'])} - Color:{product_info['color']}")

    # def add_product(self):  #------------------------------admin add new product
    #     product_name = input("Enter product name: ")
    #     if product_name.isalpha():
    #         product_price = input("Enter product price: ")
    #         product_color = input("Enter product color: ")
    #         if product_price.isdigit() and product_color.isalpha():
    #               product_id = max(self.products.keys()) + 1
    #               self.products[product_id] = {"name": product_name, "price": product_price, "color": product_color}
    #               print("Product added successfully.")
    #         else:
    #               print("Invalid Price")
    #     else:
    #         print("Invalid product name")

    def add_product(self):  # ------------------------------admin add new product

            product_name = input("Enter product name(must be string): ")
            product_price = input("Enter product price(must be numeric): ")
            product_color = input("Enter product color(must be string): ")
            if product_name.isalpha() and product_price.isdigit() and product_color.isalpha():
                product_id = max(self.products.keys()) + 1
                self.products[product_id] = {"name": product_name, "price": product_price, "color": product_color}
                print("Product added successfully.")
            else:
                print("Invalid Product Information")

    def update_product(self):
        self.view_products()
        print()
        product_id = input("Enter the product ID to update: ")
        if product_id.isdigit():
            product_id = int(product_id)
            if product_id in self.products:
                product_info = self.products[product_id]
                new_price = input("Enter new product price: ")
                new_color = input("Enter new product color: ")
                if new_price.isdigit() and new_color.isalpha():
                    new_price = int(new_price)
                    product_info["price"] = new_price
                    product_info["color"] = new_color
                    print("Product updated successfully.")
                else:
                    print("Invalid update information.")
            else:
                print("Invalid product ID.")
        else:
            print("Invalid product ID.")

    def remove_product(self):   #----------------------------admin delete a product
        self.view_products()
        print()
        product_id = input("Enter the product ID to remove: ")
        if product_id.isdigit():
            product_id = int(product_id)
            if product_id in self.products:
                del self.products[product_id]
                print("Product removed successfully.")
            else:
                print("Invalid product ID.")
        else:print("Invalid product ID.")






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

    def print_available_orders(self):
        print("Available Orders:")
        for product_id in self.user_orders:
            product_name = self.products[product_id]['name']
            print(f"{product_id}. {product_name}")

    def place_order(self):      #-------------------------user place order
        print("Products:")
        if not self.products:  # Check if there are no products
            print("No products available.")
        else:
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

            self.print_available_orders()

            print()
            order_id = input("Enter the order ID to view details: ")
            if order_id.isdigit() and int(order_id) in self.user_orders:
                product_id = int(order_id)
                product_info = self.products[product_id]
                quantity = self.user_orders[product_id]
                total_price = quantity * product_info['price']
                print(
                    f"{product_id}. Name:{product_info['name']} Quantity:{quantity}  Price:${total_price}  Color:{product_info['color']}")
            else:
                print("Invalid order ID.")
        else:
            print("You have no orders yet.")

    def cancel_order(self):   #------------------user cancle placed order
        if self.user_orders:
            self.print_available_orders()

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
            self.print_available_orders()

            order_id = input("Enter the order ID to update: ")
            if order_id.isdigit() and int(order_id) in self.user_orders:
                product_id = int(order_id)
                new_quantity = input("Enter the new quantity: ")
                if new_quantity.isdigit() and new_quantity > 0:
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