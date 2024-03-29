my_list = []

my_list.append("Python")
my_list.append("is ok")
my_list.append("sometimes")

my_list.remove("sometimes")

my_list[1] = "is neat"


print(my_list)
assert my_list == ["Python", "is neat"]
