dict1 = dict(key1="This is not that hard", key2="Python is still cool")
dict2 = {"key1": 123, "special_key": "secret"}
# This is also a away to initialize a dict (list of tuples)
dict3 = dict([("key2", 456), ("keyX", "X")])

my_dict = dict1.copy()
my_dict.update(dict2)
my_dict.update(dict3)

special_value = my_dict.pop("special_key")

print(my_dict)

assert my_dict == {"key1": 123, "key2": 456, "keyX": "X"}
assert special_value == "secret"
assert dict1 is not my_dict
assert dict2 is not my_dict
assert dict3 is not my_dict


