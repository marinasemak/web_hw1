from errors_handler import input_error
from functionality import AddressBook, Record
from entities import MissingArgumentsError


@input_error
def add_contact(args, book: AddressBook):
    """
    Add new or update contact in the dictionary
    """
    if len(args) < 2:
        raise MissingArgumentsError("Give me name and phone please")
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    """
    Change phone for existed contact
    """
    if len(args) < 3:
        raise MissingArgumentsError("Give me name, old phone and new phone please")
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated"
    else:
        return "Contact not found"


@input_error
def show_phone(args, book: AddressBook):
    """
    Show phone for existed contact
    """
    if len(args) < 1:
        raise MissingArgumentsError("Give me name of the contact please")
    name, *_ = args
    record = book.find(name)
    if record:
        message = f"{record.name}: {"; ".join(p.value for p in record.phones)}"
    else:
        message = "Contact not found"
    return message


@input_error
def show_all(book: AddressBook):
    """
    Show all contacts from the dictionary
    """
    if not book:
        return "No contacts found."
    else:
        contacts = [str(value) for key, value in book.items()]
        return "\n".join(contacts)


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise MissingArgumentsError("Give me name and birthday please")
    name, birthday, *_ = args
    record = book.find(name)
    if not record:
        return "No contacts found."
    else:
        record.add_birthday(birthday)
        return f"Birthday is added for {name}"

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        raise MissingArgumentsError("Give me name of the contact please")
    name, *_ = args
    record = book.find(name)
    if not record:
        message = "Contact not found"
    elif record.birthday is None:
        message = f"No birthday for {record.name}" 
    else: message = f"{record.name}: {record.birthday}"
    return message

@input_error
def birthdays(book: AddressBook):
    """
    Show upcoming birthdays within 7 days ahead
    """
    if not book:
        return "No contacts found."
    else:
        contacts = book.get_upcoming_birthdays()
        return contacts
