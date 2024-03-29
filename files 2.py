#Файлы здесь также хранятся в папке проекта на моём компьютере
def find_first_words(input_file):
    first_words = []
    with open(input_file) as file:
        for line in file:
            if line.strip():
                first_word = line.split()[0]
                first_words.append(first_word)
            else:
                first_words.append("")
    return first_words

in_file1 = "simple_file.txt"
in_file2 = "simple_file_with_empty_lines.txt"

expected_file_1 = ["First", "Second", "Third", "And"]
assert find_first_words(in_file1) == expected_file_1

expected_file_2 = ["The", "", "First", "nonsense", "", "Then"]
assert find_first_words(in_file2) == expected_file_2
print(expected_file_2)