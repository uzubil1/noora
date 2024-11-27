class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_contact(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
      


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                contact.display_contact()



contact1 = Contact("Arina Balazitov", "arina@mail.com", "+971 123 4567")
contact2 = Contact("MEHTAB Kurshid", "mckad@mail.com", "+971 987 6543")


manager = ContactManager()


manager.add_contact(contact1)
manager.add_contact(contact2)


manager.list_contacts()
