import json  
import csv
contacts = {}

def export_to_csv():
    if not contacts:
        print("No contacts to export.\n")
        return
    
    with open('contacts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Phone Number"])
        for name, number in contacts.items():
            writer.writerow([name.capitalize(), number])
    
    print("Contacts exported successfully to contacts.csv!\n")

def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as json_file:
            contacts = json.load(json_file)
    except FileNotFoundError:
        contacts = {}
    # print("Contacts loaded successfully!\n")

def save_contacts():
    with open('contacts.json', 'w') as json_file:
        json.dump(contacts, json_file)
    # print("Contacts saved successfully!\n")



def add_contact():
    name = input("Enter contact Name: ")
    # number = input("Enter contact number: ")


    # Check if contact already exists
    if name.lower() in contacts:
        print(f"Contact {name} already exists!\n")
        return
    while True:
        phone = input("Enter  phone number (or type 'cancel' to exit): ")
                
        if phone.lower() == "cancel":
            print("Added canceled.\n")
            return
                
        if not phone.isdigit():
            print("Invalid phone number. Only digits are allowed.")
            continue  # Ask again
                
        if len(phone) != 11:
            print("Invalid phone number. It must be exactly 11 digits long.")
            continue  # Ask again
        # Save contact
        contacts[name.lower()] = phone
        save_contacts()
        print(f"Contact {name} added successfully!\n")
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List")
    for name in sorted(contacts):  # Sort alphabetically
        print(f"{name.capitalize()} : {contacts[name]}")
    print()

def search_contact():
    query = input("Enter name or number to search: ").lower()
    found_contacts = {name: number for name, number in contacts.items() if query in name or query in number}
    
    if found_contacts:
        print("\nMatching Contacts:")
        for name, number in found_contacts.items():
            print(f"{name.capitalize()} : {number}")
        print()
    else:
        print("No matching contacts found.\n")
def update_contact():
    name = input("Enter name to update: ").lower()

    if name in contacts:
        while True:
            phone = input("Enter new phone number (or type 'cancel' to exit): ")
            
            if phone.lower() == "cancel":
                print("Update canceled.\n")
                return
            
            if not phone.isdigit():
                print("Invalid phone number. Only digits are allowed.")
                continue  # Ask again
            
            if len(phone) != 11:
                print("Invalid phone number. It must be exactly 11 digits long.")
                continue  # Ask again

            contacts[name] = phone
            save_contacts()
            print(f"Contact {name.capitalize()} updated successfully!\n")
            return  # Exit function after successful update

    else:
        print("Contact not found.\n")
def delete_contact():
    name = input("Enter name to delete: ").lower()  # Convert to lowercase
    if name in contacts:
        del contacts[name]
        print(f"Contact {name.capitalize()} deleted successfully!\n")
        save_contacts()
    else:
        print("Contact not found.\n")

def main(): 
    # global contacts
    load_contacts()
    while True :
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts")
        print("7. Exit")
        
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
            export_to_csv()
            
        elif choice == "7":
            print("Goodbye!")
            break
       
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()

    
