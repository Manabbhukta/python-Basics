contacts = {}

def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print()

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts[name] = phone
    print(f"'{name}' added successfully")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts found")
    else:
        print("\nYour Contact List:")
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone:
