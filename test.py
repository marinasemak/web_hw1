from enum import Enum
from abc import ABC, abstractmethod
from functionality import AddressBook, Record
from commands import (
    AddContact,
    ChangeContact,
    ShowPhone,
    ShowAllContacts,
    AddBirthday,
    ShowBirthday,
    Birthdays,
)


class CommandType(Enum):
    TYPE_CLOSE = "close"
    TYPE_EXIT = "exit"
    TYPE_HELLO = "hello"
    TYPE_ADD = "add"
    TYPE_CHANGE = "change"
    TYPE_PHONE = "phone"
    TYPE_ALL = "all"
    TYPE_ADD_BIRTHDAY = "add-birthday"
    TYPE_SHOW_BIRTHDAY = "show-birthday"
    TYPE_BIRTHDAYS = "birthdays"


class Interface(ABC):

    @abstractmethod
    def get_command(self) -> str:
        pass

    @abstractmethod
    def display_command(self):
        pass


class CommandHandler:
    def __init__(self, user_input, record=None) -> None:
        self.user_input = user_input
        self.record = record

    def parse_input(self):
        cmd, *args = self.user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    def handle_command(self):
        cmd, *args = self.parse_input()
        if cmd == CommandType.TYPE_ADD.value:
            command = AddContact()
            command.execute(args, self.record)


class ConsoleInterface(Interface):

    def get_command(self) -> str:
        return input("Enter a command: ")

    def display_command(self, command_handler: CommandHandler):
        command_handler.handle_command()


class RunBot:

    def __init__(self, ui: ConsoleInterface, record: AddressBook):
        self.ui = ui
        self.record = record

    def run(self):
        # while True:
        user_input = self.ui.get_command()
        command_handler = CommandHandler(user_input, self.record)
        self.ui.display_command(command_handler)


if __name__ == "__main__":
    client = RunBot(ConsoleInterface(), AddressBook())
    client.run()
