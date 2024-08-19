from functools import wraps


class FieldValidationError(Exception):
    pass


class MissingValueError(Exception):
    pass


class MissingArgumentsError(Exception):
    pass


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
            return e
        except FieldValidationError as e:
            print(e)
            return e
        except MissingValueError as e:
            print(e)
            return e
        except MissingArgumentsError as e:
            print(e)
            return e

    return inner
