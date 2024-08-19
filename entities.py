from abc import ABC, abstractmethod
from datetime import datetime
from errors_handler import FieldValidationError


class Field(ABC):
    """
    Basic class for records fields
    """

    def __init__(self, value: str):
        self.value = value
        self.validate_field()

    def __str__(self):
        return str(self.value)

    @abstractmethod
    def validate_field(self):
        pass


class Name(Field):
    """
    Class for saving and validating contact names
    """

    def validate_field(self):
        if len(self.value) < 1:
            raise FieldValidationError("Name can't be empty")


class Phone(Field):
    """
    Class for saving and validating contact phones
    """

    def validate_field(self):
        if len(self.value) != 10:
            raise FieldValidationError("Phone number must be 10 digits long")


class Birthday(Field):
    """
    Class for saving and validating contact birthday
    """

    def validate_field(self):
        """
        convert input value to 'datetime' and validate format
        """
        try:
            self.value = datetime.strptime(self.value, "%d.%m.%Y").date()
        except ValueError:
            raise FieldValidationError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
