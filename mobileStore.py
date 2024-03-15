class MobileStoreManagement:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin"},
            "user": {"password": "user"}
        }
        self.products = {
            1: {"name": "Xiaomi", "price": 10, "color": "Red"},
            2: {"name": "Samsung", "price": 20, "color": "Blue"},
            3: {"name": "Apple", "price": 30, "color": "Green"},
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

    # ---------------------------------------User----------------------------------------------------
    def user_panel(self):
        print()
        print("**********WELCOME AS AN USER **********")
        while True:

            print("a. Logout")
            print()
            choice = input("Enter your choice: ")

            if choice == 'a':
                print()
                print("****YOU ARE SUCCESSFULLY LOGGED OUT****")
                return
            else:
                print("Invalid choice. Please enter a valid option.")


# -------------------------------------------------------------------------------------------


if __name__ == "__main__":
    mobile_store_system = MobileStoreManagement()

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if mobile_store_system.users.get(username) and mobile_store_system.users[username]["password"] == password:
            mobile_store_system.main_menu(username)
        else:
            print("Invalid username or password.")