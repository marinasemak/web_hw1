from pathlib import Path
import pickle
from collections import UserDict
from entities import Name, Phone, Birthday
from errors_handler import MissingValueError
from datetime import date, datetime, timedelta

DATA_FILE_PATH = Path("addressbook.pickle")


class Record:
    """
    Save contact info including name, phones and birthday
    """

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self) -> str:
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise MissingValueError(
            f"Phone number '{old_phone}' does not exist for contact"
        )

    def remove_phone(self, phone_str: str):
        for i, phone in enumerate(self.phones):
            if phone.value == phone_str:
                del self.phones[i]
                return
        raise MissingValueError(
            f"Phone number '{phone_str}' does not exist for contact"
        )

    def find_phone(self, phone_str: str):
        for phone in self.phones:
            if phone.value == phone_str:
                return phone.value
        return None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)


class AddressBook(UserDict):
    """
    Save and manage records
    """

    def add_record(self, record: Record):
        """
        Add record to self.data
        """
        self.data[record.name.value] = record
        return record

    def find(self, value: str):
        """
        Find record by name
        """
        return self.data.get(value, None)

    def delete(self, value: str):
        """
        Delete record by name
        """
        if value in self.data:
            del self.data[value]

    @staticmethod
    def date_to_string(date: datetime) -> str:
        return date.strftime("%d.%m.%Y")

    @staticmethod
    def find_next_weekday(start_date: datetime, weekday: int) -> datetime:
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def get_upcoming_birthdays(self, days=7) -> list:
        """
        Method defines contatcs whose birthday is 7 days ahead of the current day
        """
        upcoming_birthdays = []
        today = date.today()

        for record in self.data.values():
            if record.birthday is None:
                raise MissingValueError(
                    "There is no birthday in contacts. Add birthday first"
                )
            birthday_this_year = record.birthday.value.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = record.birthday.value.replace(year=today.year + 1)
            if 0 <= (birthday_this_year - today).days <= days:
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year = self.find_next_weekday(birthday_this_year, 0)

                congratulation_date_str = self.date_to_string(birthday_this_year)
                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "birthday": congratulation_date_str,
                    }
                )

        return upcoming_birthdays


def save_data(book, filename=DATA_FILE_PATH):
    """
    Save address book to file
    """
    with open(DATA_FILE_PATH, "wb") as data_file:
        pickle.dump(book, data_file)


def load_records():
    """
    Load saved address book
    """
    book = AddressBook()
    if DATA_FILE_PATH.exists():
        with open(DATA_FILE_PATH, "rb") as data_file:
            book = pickle.load(data_file)
    return book
