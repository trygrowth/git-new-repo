# Contact Book Application

# Initialize an empty dictionary to store contacts
contacts = {}

def display_menu():
    print("\n--- Contact Book ---")
    print("1. View All Contacts")
    print("2. Add New Contact")
    print("3. Search Contact by Name")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nYour Contacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print(f"Contact with name '{name}' already exists.")
    else:
        phone = input("Enter phone number: ").strip()
        if phone.isdigit():
            contacts[name] = phone
            print(f"Contact '{name}' added successfully.")
        else:
            print("Invalid phone number. Please enter digits only.")

def search_contact():
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        print(f"Found Contact - Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"No contact found with name '{name}'.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()
        if new_phone.isdigit():
            contacts[name] = new_phone
            print(f"Contact '{name}' updated successfully.")
        else:
            print("Invalid phone number. Please enter digits only.")
    else:
        print(f"No contact found with name '{name}'.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with name '{name}'.")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        view_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
 
