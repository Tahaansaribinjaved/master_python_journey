contacts = {}

def add_contact():
    name = input("Enter contact Name :")
    number = input("Enter contact number :")
    contacts[name.lower()] = number
    print(f"Contact {name} added succefully ! \n")
    
def veiw_contacts():
    if not contacts :
        print('Contact not found \n')
        return
    print('\n Contact List')
    for name,number in contacts.items():
        print(f"{name.capitalize()} : {number}")
    print()
def search_contact():
    name = input("Enter conatact name to search")
    if name.lower() in contacts :
        print(f"{name.capitalize} : {contacts[name.lower()]} \n")
    else:
        print("Contact not found.\n")
