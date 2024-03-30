magic_dict = dict(val1=44, val2="secret value", val3=55.0, val4=1)

sum_of_values = 0
for value in magic_dict.values():
    if isinstance(value, (int, float)):
        sum_of_values += value

print(sum_of_values)
assert sum_of_values == 100

#здесь пришлось плотно гуглить...