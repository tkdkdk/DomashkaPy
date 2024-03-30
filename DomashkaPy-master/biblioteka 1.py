first_name = "John"
last_name = "Doe"
favorite_hobby = "Python"
sports_hobby = "gym"
age = 82


my_dict = {
    "name": first_name + " " + last_name,
    "age": age,
    "hobbies": [favorite_hobby, sports_hobby],
}

print(my_dict)
assert my_dict == {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}