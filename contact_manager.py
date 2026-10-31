# The address book
address_book = {}

def display_menu():
    print("\n=== CONTACT MANAGER ===")
    print("1. Add new contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Search contact")
    print("6. Quit")

def add_contact():
    name = input("Contact name: ").strip()
    if name in address_book:
        print("Contact already exists")
        return
    phone = input("Phone: ").strip()
    email = input("E-mail: ").strip()
    address_book[name] = {"Phone":phone,"E-mail": email}
    print(f"Contact '{name}' added")

def search_contact():
    name = input("Contact name to search: ").strip()
    if name in address_book:
        print(f"\nContact {name}")
        print(f"\nPhone: {address_book[name]['Phone']}")
        print(f"\nE-mail: {address_book[name]['E-mail']}")
    else:
        print(f"\nContact {name} not found")

def update_contact():
    name = input("Contact name to update: ").strip()
    if name in address_book:
        print(f"\nContact {name}")
        print(f"\nPhone: {address_book[name]['Phone']}")
        print(f"\nE-mail: {address_book[name]['E-mail']}")

        print("\nLaisse vide pour conserver la valeur actuelle.")
        new_phone = input("New phone: ").strip()
        new_email = input("New e-mail: ").strip()

        if new_phone:
            address_book[name]['Phone'] = new_phone
        if new_email:
            address_book[name]['E-mail'] = new_email

        print(f"\nContact '{name}' updated successfully.")
    else:
        print(f"\nContact '{name}' not found.")

def delete_contact():
    name = input("Contact name to delete: ").strip()
    if name in address_book:
        del address_book[name]
        print(f"\nContact '{name}' deleted successfully.")
    else:
        print(f"\nContact '{name}' not found.")

def view_all_contacts():
    if len(address_book)==0:
        print("The address book is empty.")
    else:
        print(f"\n{len(address_book)} contact(s) saved.")
        for name, info in address_book.items():
            print(f"Name : {name} | Phone : {info['Phone']} | E-mail : {info['E-mail']}")


# Main program loop
while True:
    display_menu()
    choice = input("\nYour choice: ").strip()
    if choice == "1":
        add_contact()
    elif choice == "2":
        update_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        view_all_contacts()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")