from cli.menu import display_menu
from cli.actions import (add_farmer, add_product, view_farmers, view_products, view_products_by_farmer, process_payment)

# Main CLI loop. Displays menu and calls functions based on user choice
def main():
    while True:
        choice = display_menu()

        if choice == "1":
            add_farmer()
        elif choice == "2":
            add_product()
        elif choice == "3":
            view_farmers()
        elif choice == "4":
            view_products()
        elif choice == "5":
            view_products_by_farmer()
        elif choice == "6":
            process_payment()
        elif choice == "0":
            print("Exiting the App. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

