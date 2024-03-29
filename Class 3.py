class Dog:

    def __init__(self):
        self.energy = 10

    def sleep(self):
        self.energy += 2

    def bark(self):
        if self.energy > 0:
            self.energy -= 1

    def get_energy(self):
        return self.energy


doge = Dog()
assert doge.get_energy() == 10

doge.bark()
doge.bark()
doge.bark()
assert doge.get_energy() == 7

doge.sleep()
assert doge.get_energy() == 9

another_doge = Dog()
assert another_doge.get_energy() == 10

