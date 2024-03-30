WANTED_PEOPLE = ["John Doe", "Clint Eastwood", "Chuck Norris"]

def find_wanted_people(names):
    wanted = []
    for name in names:
        if name in WANTED_PEOPLE:
            wanted.append(name)
    return wanted
people_to_check1 = ["Donald Duck", "Clint Eastwood", "John Doe", "Barack Obama"]
wanted1 = find_wanted_people(people_to_check1)
assert len(wanted1) == 2
assert "John Doe" in wanted1
assert "Clint Eastwood" in wanted1

people_to_check2 = ["Donald Duck", "Mickey Mouse", "Zorro", "Superman", "Robin Hood"]
wanted2 = find_wanted_people(people_to_check2)
assert wanted2 == []

