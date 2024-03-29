words = ["PYTHON", "JOHN", "chEEse", "hAm", "DOE", "123"]
upper_case_words = []

for word in words:
    if word.isupper():
        upper_case_words.append(word)

print(upper_case_words)
assert upper_case_words == ["PYTHON", "JOHN", "DOE"]



