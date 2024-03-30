class StringManipulator:
    """Docstring of StringManipulator"""

    category = "Manipulator"

    def __init__(self, original):
        self.string = original

    def reverse_words(self):
        words = self.string.split()
        self.string = ' '.join(reversed(words))

    def make_title(self):
        self.string = self.string.title()

    def get_manipulated(self):
        return self.string


assert StringManipulator.__doc__ == "Docstring of StringManipulator"
assert StringManipulator.category == "Manipulator"

str_manip = StringManipulator("cOOL pyThON")

str_manip.reverse_words()
assert str_manip.get_manipulated() == "pyThON cOOL"

str_manip.make_title()
assert str_manip.get_manipulated() == "Python Cool"

