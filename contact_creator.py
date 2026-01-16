# ContactBook: A normal, Python program
contacts = []

def add_contact(name, phone):
    """Add a new contact to the list."""
    contacts.append({"name": name, "phone": phone})
    print(f"Added contact: {name} - {phone}")

def list_contacts():
    """List all contacts."""
    print("\nAll Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def remove_contact(index):
    """Remove a contact by its number (1-based)."""
    if 0 <= index < len(contacts):
        removed = contacts.pop(index)
        print(f"Removed contact: {removed['name']}")
    else:
        print("Invalid contact number.")

# Example usage
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
add_contact("Charlie", "555-555-5555")

list_contacts()

remove_contact(1)  # removes Bob
list_contacts()