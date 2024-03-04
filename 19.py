# 19) Write program for building restaurant menu using class in Python.


class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, name, description, price):
        self.menu_items[name] = {'description': description, 'price': price}

    def display_menu(self):
        print("Restaurant Menu:")
        for name, details in self.menu_items.items():
            print(f"{name} - {details['description']} - ${details['price']:.2f}")

menu = Menu()

menu.add_item("Porotta & Beef Curry", "Soft porotta with spicy beef curry", 200)
menu.add_item("Fried-Rice & Chicken-Chilli", "Fried rice with flavoured chicken-chilli", 400)
menu.add_item("Pizza", "Delicious pakistani pizza", 300)

menu.display_menu()
