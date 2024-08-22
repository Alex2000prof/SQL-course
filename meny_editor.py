from HW_WEEK4_DAY4 import MenuItem
from MenuManager import MenuManager

def show_user_menu():
    print("Menu:")
    print("V - View an item")
    print("A - Add an item")
    print("D - Delete an item")
    print("U - Update an item")
    print("S - Show restaurant menu")
    print("Q - Quit")

def add_item_to_menu():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    name = input("Enter item name to delete: ")
    item = MenuManager.get_by_name(name)
    if item:
        item_to_delete = MenuItem(name=name, item_id=item['item_id'])
        item_to_delete.delete()
        print("Item was deleted successfully.")
    else:
        print("Item not found.")

def update_item_from_menu():
    name = input("Enter item name to update: ")
    item = MenuManager.get_by_name(name)
    if item:
        new_name = input("Enter new item name: ")
        new_price = int(input("Enter new item price: "))
        item_to_update = MenuItem(name=new_name, item_price=new_price, item_id=item['item_id'])
        item_to_update.save()
        print("Item was updated successfully.")
    else:
        print("Item not found.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    for item in items:
        print(f"ID: {item['item_id']}, Name: {item['name_id']}, Price: {item['item_price']}")

if __name__ == '__main__':
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()
        if choice == 'V':
            name = input("Enter item name to view: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"ID: {item['item_id']}, Name: {item['name_id']}, Price: {item['item_price']}")
            else:
                print("Item not found.")
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'Q':
            show_restaurant_menu()
            break
        else:
            print("Invalid choice, please try again.")
