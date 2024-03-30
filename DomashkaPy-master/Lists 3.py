list1 = [6, 12, 5]
list2 = [6.2, 0, 14, 1]
list3 = [0.9]

my_list = list1 + list2 + list3

my_list.sort(reverse=True)

print(my_list)

assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]
