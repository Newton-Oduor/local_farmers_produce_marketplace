# debug.py
from cli.actions import (
    add_farmer, add_product, view_farmers, view_products, view_products_by_farmer,
    delete_farmer, delete_product, purchase_product, add_buyer, delete_buyer,
    search_products, view_buyer_transactions, view_farmer_sales
)
from cli.menu import display_menu

def main():
    print("=== LFPM App Debug CLI ===\n")
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
            purchase_product()
        elif choice == "7":
            delete_farmer()
        elif choice == "8":
            delete_product()
        elif choice == "9":
            add_buyer()
        elif choice == "10":
            delete_buyer()
        elif choice == "11":
            search_products()
        elif choice == "12":
            view_buyer_transactions()
        elif choice == "13":
            view_farmer_sales()
        elif choice == "0":
            print("Exiting LFPM Debug CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()


