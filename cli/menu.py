def display_menu():
    # Displays the CLI menu and get users choice
    # Returns the choice as a string

    print("\nWelcome to the Local Farmers Produce Marketplace!")
    print("Please select an option:")
    print("1. Add a farmer")
    print("2. Add a Product")
    print("3. View all farmers")
    print("4. View all products")
    print("5. View products by farmer")
    print("6. Purchase a product (M-Pesa payment)")
    print("7. Delete a farmer")
    print("8. Delete a product")
    print("9. Add a buyer")
    print("10. Delete a buyer")
    print("11. Search products")
    print("12. View buyer transaction history")
    print("0. Exit")


    choice = input("Enter your choice: ")
    return choice
