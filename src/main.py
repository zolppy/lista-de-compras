import os
import pickle # file handling
from enum import IntEnum

# enumerations make the code more readable
class Menu(IntEnum):
    ADD_ITEM    = 1
    SHOW_ITEMS  = 2
    UPDATE_ITEM = 3
    REMOVE_ITEM = 4
    EXIT        = 5

def clear_console():
    if os.name == 'nt':  # windows
        os.system('cls')
    else:  # unix/linux/mac
        os.system('clear')

# loads shopping list from file
def load_list():
    if os.path.exists('../data/data.pkl'):
        with open('../data/data.pkl', 'rb') as file:
            return pickle.load(file)
    else:
        return []

# saves the shopping list in the file
def save_list(list):
    with open('../data/data.pkl', 'wb') as file:
        pickle.dump(list, file)

shopping_list = load_list()

def add_item():
    item = input('Enter the name of the item to be added: ')
    shopping_list.append(item)
    save_list(shopping_list)
    print(f"Item '{item}' added to shopping list.")

def show_items():
    print('Shopping list:')
    if shopping_list:
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print('The shopping list is empty.')

def update_item():
    show_items()
    if shopping_list:
        index = int(input('Enter the number of the item to be updated: '))
        if 1 <= index <= len(shopping_list):
            novo_item = input('Enter the new item name: ')
            shopping_list[index - 1] = novo_item
            save_list(shopping_list)
            print('Item updated successfully.')
        else:
            print('Invalid index.')
    else:
        print('The shopping list is empty.')

def remove_item():
    show_items()
    if shopping_list:
        index = int(input('Enter the number of the item to be removed: '))
        if 1 <= index <= len(shopping_list):
            target = shopping_list.pop(index - 1)
            save_list(shopping_list)
            print(f"Item '{target}' removed from shopping list.")
        else:
            print('Invalid index.')
    else:
        print('The shopping list is empty.')

def show_menu():
    print('Menu:')
    print('1. Add item')
    print('2. Show items')
    print('3. Update item')
    print('4. Remove item')
    print('5. Exit')

while True:
    show_menu()
    option = int(input('Enter the number of the desired option: '))

    if option == Menu.ADD_ITEM:
        clear_console()
        add_item()
    elif option == Menu.SHOW_ITEMS:
        clear_console()
        show_items()
    elif option == Menu.UPDATE_ITEM:
        clear_console()
        update_item()
    elif option == Menu.REMOVE_ITEM:
        clear_console()
        remove_item()
    elif option == Menu.EXIT:
        clear_console()
        print('Goodbye.')
        break
    else:
        print('Invalid option. Try again.')
