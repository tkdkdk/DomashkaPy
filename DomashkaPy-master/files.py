#Я все файлы просто скопировал в папку проекта
def sum_numbers_in_file(input_file):
    total = 0
    with open(input_file, "r") as file:
        for line in file:
            number_str = line.strip()
            total += float(number_str)
    return total

in_file = "numbers.txt"
assert sum_numbers_in_file(in_file) == 189.5

print(sum_numbers_in_file(in_file))
