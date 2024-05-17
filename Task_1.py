import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contact information

    def add_contact(self, name, address):
        self.contacts[name] = address  # Add a new contact to the address book

    def get_contact(self, name):
        return self.contacts.get(name, None)  # Retrieve contact information by name

    def __repr__(self):
        return str(self.contacts)  # Return string representation of the address book

def save_data(book, filename="addressbook.pkl"):
    # Open the file in write-binary mode and save the address book using pickle
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        # Open the file in read-binary mode and load the address book using pickle
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        # Return a new AddressBook if the file is not found
        return AddressBook()

def main():
    # Load the address book from the file (or create a new one if the file doesn't exist)
    book = load_data()

    # Main program loop (for example purposes, we add and display contacts here)
    while True:
        action = input("Would you like to (a)dd a contact, (v)iew a contact, or (q)uit? ")
        if action == 'a':
            name = input("Enter contact name: ")
            address = input("Enter contact address: ")
            book.add_contact(name, address)
        elif action == 'v':
            name = input("Enter contact name: ")
            contact = book.get_contact(name)
            if contact:
                print(f"Address for {name}: {contact}")
            else:
                print(f"No contact found for {name}.")
        elif action == 'q':
            # Save the address book to the file before exiting
            save_data(book)
            print("Address book saved. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
