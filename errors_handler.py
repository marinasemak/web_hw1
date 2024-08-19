from functools import wraps
from entities import FieldValidationError, MissingValueError, MissingArgumentsError


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return e
        except FieldValidationError as e:
            return e
        except MissingValueError as e:
            return e
        except MissingArgumentsError as e:
            return e

    return inner
