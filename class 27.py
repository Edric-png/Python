# class student:
#     grade = 10
#     print("Hey, I am a student of grade",grade)
# ob = student
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
# modelX = Vehicle(240, 18)
# print("Model Max Speed:",modelX.max_speed)
# print("Model Mileage:", modelX.mileage)
class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))