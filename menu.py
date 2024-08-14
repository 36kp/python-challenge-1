# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42

# Create an empty list that store customer's order in dictionary format
order = []

# Initialize place order 
place_order = False

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to view different sections of the menu, so let's create a 
# continuous loop
while True:
    # Ask the customer which menu category they want to view
    print("Which menu would you like to view? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}

    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_category_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Initialize a menu item counter
            item_counter = 1
            # Clear menu items to display sub menu
            menu_items = {}
            # Print out the menu options from the menu_category_name
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        # Add item to current sub-menu on display
                        menu_items[item_counter] = {f"{key} - {key2}": value2}
                        # Add 1 to the item_counter
                        item_counter += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    # Add item to current sub-menu on display
                    menu_items[item_counter] = {key: value}
                    # Add 1 to the item_counter
                    item_counter += 1
            
            print(menu_dashes)
            # Ask user for order or return to the main menu
            menu_selection = input("Enter the Item # to order.:")
            if menu_selection.isdigit():
                menu_selection_int = int(menu_selection)
                # Check if input is in the sub menu on display
                if menu_selection_int in menu_items.keys():
                    for key, value in menu_items[menu_selection_int].items():
                        selected_item = key
                        # Ask user for quantity
                        quantity = input(f"Enter quantity for {selected_item}. Quantity will default to 1 for invalid entry. : ")
                        quantity_int = 1
                        if quantity.isdigit():
                            quantity_int = int(quantity)
                        order.append({"Item name": selected_item, 
                                        "Price": value, 
                                        "Quantity": quantity_int})
                else:
                    print(f"{menu_selection} is not a valid input.")
            else :
                print(f"{menu_selection} is not a valid input.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
    
    # Ask user if they would like to continue ordering
    while True:
        keep_ordering = input("Would you like to keep ordering? Select (y)es or (n)o. :")
        match keep_ordering.lower():
            case 'y':
                place_order = True
                break
            case 'n':
                place_order = False
                print("Thank you for your order")
                break
            case _:
                print("Invalid input")
    
    # Check if customer has finished placing order
    if place_order == False:
        # print receipt
        receipt_dashes = "-" * 45
        print(receipt_dashes)
        print("Item name                 | Price  | Quantity")
        print("--------------------------|--------|---------")
        for item in order:
            # Extract Item name, Price and Quantity from Order list
            item_name = item['Item name']
            price = f"${item['Price']:,.2f}"
            quantity = f"{item['Quantity']}"
            # Calculate and store extra spaces for each attribute
            item_name_spaces = " " * (26 - len(item_name))
            price_spaces = " " * (6 - len(price))
            quantity_spaces = " " * (9 - len(quantity))
            # Print order item
            print(f"{item_name}{item_name_spaces}|" + 
                  f" {price}{price_spaces} |" + 
                  f" {quantity}{quantity_spaces}")
        print(receipt_dashes)
        # Calculate total price for the order
        total_price = sum([item['Price'] * item['Quantity'] for item in order])
        # Print total price for the order
        print(f"Your total price for the order is ${total_price:,.2f}")
        print(receipt_dashes)
        # clear order for next customer. This is only if we do not want the 
        # program to start over for new customer
        order = []
        # Complete order and exit. Remove this break to keep program running
        # for multiple customers
        break 

