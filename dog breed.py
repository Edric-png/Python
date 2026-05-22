class Dog:
    species = "Canine"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
d1 = Dog("Buddy", "Labrador")
d2 = Dog("Rocky", "German Shepherd")
print(d1.name, d1.breed, Dog.species)
print(d2.name, d2.breed, Dog.species)