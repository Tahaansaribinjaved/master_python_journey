contacts = {}

def add_contact():
    name = input("Enter contact Name :")
    number = input("Enter contact number :")
    contacts[name.lower()] = number
    print(f"Contact {name} added succefully ! \n")
    
def view_contacts():
    if not contacts :
        print('Contact not found \n')
        return
    print('\n Contact List')
    for name,number in contacts.items():
        print(f"{name.capitalize()} : {number}")
    print()
def search_contact():
    name = input("Enter name to search: ").lower()  # Convert input to lowercase
    if name in contacts:
        print(f"{name.capitalize()} : {contacts[name]}\n")  # Capitalize name for display
    else:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print(f"Contact {name} updated successfully!\n")
    else:
        print("Contact not found.\n")
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!\n")
    else:
        print("Contact not found.\n")
        
def main(): 
    while True :
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()

    
