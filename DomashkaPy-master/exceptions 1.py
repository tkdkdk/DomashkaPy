def sum_of_list(values):
    total_sum = 0
    for val in values:
        try:
            numeric_val = float(val)
        except (ValueError, TypeError) as e:

            continue
        total_sum += numeric_val
    return total_sum
list1 = [1, 2, 3]
list2 = ["1", 2.5, "3.0"]
list3 = ["", "1"]
list4 = []
list5 = ["John", "Doe", "was", "here"]
nasty_list = [KeyError(), [], dict()]

assert sum_of_list(list1) == 6
assert sum_of_list(list2) == 6.5
assert sum_of_list(list3) == 1
assert sum_of_list(list4) == 0
assert sum_of_list(list5) == 0
assert sum_of_list(nasty_list) == 0