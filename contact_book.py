contacts = []  # List to store contacts


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    # Creates a dictionary to store contact details
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print(f"Contact '{name}' added successfully!\n")


def view_contacts():
    if not contacts:  # Check if the contacts list is empty
        print("No contacts found.\n")
        return

    print("Your Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()  # Prints a new line for better readability


def search_contact():
    search_name = input("Enter the name of the contact you want to search for: ")

    found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]
    if found_contacts:
        print("Search Results:")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()
    else:
        print(f"No contacts found with the name '{search_name}'.\n")


def delete_contact():
    view_contacts()  # Displays all contacts to the user

    if not contacts:  # If no contacts exist, exit the function
        return

    try:
        contact_number = int(input("Enter the number of the contact you want to delete: "))
        if 1 <= contact_number <= len(contacts):
            removed_contact = contacts.pop(contact_number - 1)
            print(f"Contact '{removed_contact['name']}' deleted successfully.\n")
        else:
            print("Invalid input. Please enter a valid number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def update_contact():
    view_contacts()  # Displays all contacts to the user

    if not contacts:  # If no contacts exist, exit the function
        return

    try:
        contact_number = int(input("Enter the number of the contact you want to update: "))
        if 1 <= contact_number <= len(contacts):
            contact = contacts[contact_number - 1]

            print("Updating contact:")
            print(f"1. Name: {contact['name']}")
            print(f"2. Phone: {contact['phone']}")
            print(f"3. Email: {contact['email']}")

            choice = input("Enter the number of the field you want to update (1/2/3): ")

            if choice == '1':
                new_name = input("Enter the new name: ")
                contact['name'] = new_name
                print("Name updated successfully.\n")
            elif choice == '2':
                new_phone = input("Enter the new phone number: ")
                contact['phone'] = new_phone
                print("Phone number updated successfully.\n")
            elif choice == '3':
                new_email = input("Enter the new email address: ")
                contact['email'] = new_email
                print("Email address updated successfully.\n")
            else:
                print("Invalid choice. No updates made.\n")
        else:
            print("Invalid input. Please enter a valid number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def save_contacts():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")
    print("Contacts saved successfully.")


def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
        print("Contacts loaded successfully.\n")
    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty list.\n")


def main():
    load_contacts()  # Load contacts from file when the program starts

    while True:
        print("Simple Contact Book")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Search for a Contact")
        print("4. Delete a Contact")
        print("5. Update a Contact")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            save_contacts()
            print("Contacts saved. Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

