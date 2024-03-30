numbers = [1, 3, 4, 6, 81, 80, 100, 95]

my_list = []
for number in numbers:
    if number % 5 == 0 and number % 2 == 1:
        my_list.append("five odd")
    elif number % 5 == 0 and number % 2 == 0:
        my_list.append("five even")
    elif number % 2 == 1:
        my_list.append("odd")
    else:
        my_list.append("even")
print(my_list)
assert my_list == [
    "odd",
    "odd",
    "even",
    "even",
    "odd",
    "five even",
    "five even",
    "five odd",
]

