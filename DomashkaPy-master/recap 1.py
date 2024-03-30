VOWELS = ["a", "e", "i", "o", "u"]

def super_vowels(text):

  result = ""
  for char in text:
    if char.lower() in VOWELS:
      result += char.upper()
    else:
      result += char.lower()
  return result


assert super_vowels("hi wassup!") == "hI wAssUp!"
assert super_vowels("HOw aRE You?") == "hOw ArE yOU?"

print(super_vowels("hi wassup!"))