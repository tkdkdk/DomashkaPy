def average_length_of_words(sentence):

    if not sentence:
        return 0
    words = sentence.split()

    total_length = sum(len(word) for word in words)

    return round(total_length / len(words), 1)

assert average_length_of_words("only four lett erwo rdss") == 4
assert average_length_of_words("one two three") == 3.7
assert average_length_of_words("one two three four") == 3.8
assert average_length_of_words("") == 0


