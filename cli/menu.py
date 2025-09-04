def display_menu():
    # Displays the CLI menu and get users choice
    # Returns the choice as a string

    print("\nWelcome to the Local Farmers Produce Marketplace CLI!")
    print("Please select an option:")
    print("1. Add a farmer")
    print("2. Add a Product")
    print("3. View all Farmers")
    print("4. View all Products")
    print("5. View Products by Farmer")
    print("6. Purchase a Product (M-Pesa Payment)")
    print("0. Exit")


    choice = input("Enter your choice: ")
    return choice
