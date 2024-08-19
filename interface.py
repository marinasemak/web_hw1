from abc import ABC, abstractmethod
from commands_handler import CommandHandler


class Interface(ABC):

    @abstractmethod
    def get_command(self) -> str:
        pass

    @abstractmethod
    def display_command(self):
        pass


class ConsoleInterface(Interface):

    def get_command(self) -> str:
        return input("Enter a command: ")

    def display_command(self, command_handler: CommandHandler):
        command_handler.handle_command()
