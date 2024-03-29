original = ["I", "am", "learning", "hacking", "in"]

modified = original[:3]

modified.extend(["Lists" , "in" , "Python"])


print(modified)
assert original == ["I", "am", "learning", "hacking", "in"]
assert modified == ["I", "am", "learning", "Lists", "in", "Python"]
