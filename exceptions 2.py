class TooLongString(Exception):

    def __init__(self, message="String is too long!"):
        super().__init__(message)

def verify_short_string(string):

    if len(string) > 10:
        raise TooLongString("String length exceeds 10 characters.")


verify_short_string("short")
verify_short_string("10   chars")


try:
    verify_short_string("this is long")
except TooLongString as e:

    pass
else:

    assert False