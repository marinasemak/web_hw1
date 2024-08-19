from interface import ConsoleInterface
from functionality import AddressBook
from commands_handler import CommandHandler, CommandType


class RunBot:

    def __init__(self, ui: ConsoleInterface, record: AddressBook):
        self.ui = ui
        self.record = record

    def run(self):
        while True:
            user_input = self.ui.get_command()
            command_handler = CommandHandler(user_input, self.record)
            self.ui.display_command(command_handler)
            if (
                user_input == CommandType.TYPE_EXIT.value
                or user_input == CommandType.TYPE_CLOSE.value
            ):
                break


if __name__ == "__main__":
    client = RunBot(ConsoleInterface(), AddressBook())
    client.run()
