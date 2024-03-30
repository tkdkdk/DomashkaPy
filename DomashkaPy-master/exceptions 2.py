class TooLongString(Exception):
    pass


def verify_short_string(string):
    if len(string) > 10:
        raise TooLongString

# These should not raise
verify_short_string("short")
verify_short_string("10   chars")

# This should raise
try:
    verify_short_string("this is long")
except TooLongString as e:
    # This is ok
    pass
else:
    # This means that there was no exception
    assert False
