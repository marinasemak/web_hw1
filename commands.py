from abc import ABC, abstractmethod
from functionality import AddressBook, Record

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class AddContact(Command):

    def execute(self, args, book: AddressBook) -> None:
        """
        Add new or update contact in the dictionary
        """
        # if len(args) < 2:
        #     raise MissingArgumentsError("Give me name and phone please")
        name, phone, *_ = args
        record = book.find(name)
        message = "Contact updated."
        if record is None:
            record = Record(name)
            book.add_record(record)
            message = "Contact added."
        if phone:
            record.add_phone(phone)
        print(message)

class ChangeContact(Command):
    def execute(self, args, book: AddressBook) -> None:
        """
        Change phone for existed contact
        """
        # if len(args) < 3:
        #     raise MissingArgumentsError("Give me name, old phone and new phone please")
        name, old_phone, new_phone, *_ = args
        record = book.find(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            print("Contact updated")
        else:
            print("Contact not found")

class ShowPhone(Command):
    def execute(self, args, book: AddressBook) -> None:
        """
        Show phone for existed contact
        """
        # if len(args) < 1:
        #     raise MissingArgumentsError("Give me name of the contact please")
        name, *_ = args
        record = book.find(name)
        if record:
            message = f"{record.name}: {'; '.join(p.value for p in record.phones)}"
        else:
            message = "Contact not found"
        print(message)

class ShowAllContacts(Command):
    def execute(self, book: AddressBook) -> None:
        """
        Show all contacts from the dictionary
        """
        if not book:
            print("No contacts found.")
        else:
            contacts = [str(value) for key, value in book.items()]
            print("\n".join(contacts))


class AddBirthday(Command):
    def execute(self, args, book: AddressBook) -> None:

        # if len(args) < 2:
        #     raise MissingArgumentsError("Give me name and birthday please")
        name, birthday, *_ = args
        record = book.find(name)
        if not record:
            print("No contacts found.")
        else:
            record.add_birthday(birthday)
            print(f"Birthday is added for {name}")


class ShowBirthday(Command):
    def execute(self, args, book: AddressBook) -> None:

        # if len(args) < 1:
        #     raise MissingArgumentsError("Give me name of the contact please")
        name, *_ = args
        record = book.find(name)
        if not record:
            message = "Contact not found"
        elif record.birthday is None:
            message = f"No birthday for {record.name}"
        else:
            message = f"{record.name}: {record.birthday}"
        print(message)


class Birthdays:
    def execute(self, book: AddressBook) -> None:
        """
        Show upcoming birthdays within 7 days ahead
        """
        if not book:
            print("No contacts found.")
        else:
            contacts = book.get_upcoming_birthdays()
            print(contacts)
