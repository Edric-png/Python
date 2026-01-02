# num = 89
# ml = "N"
# if num <= 75:
#     if ml == "Y":
#         print("Eligible")
#     else:
#         print("Doesn't meet conditions")
# else:
#     print("Eligible")
# num = 165
# if num <= 50:
#     amount = num*8
#     print(amount)
# elif num <= 100:
#     amount = num*5
#     print(amount)
# elif num <= 200:
#     amount = num*3
#     print(amount)
# else:
#     amount = num*2
#     print(amount)
print("Select your vehicle")
print("1.Bike")
print("2.Car")
a = int(input("Press 1 or 2:"))
if a == 1:
    print("Scooty or Scooter")
    b = int(input("Select your bike:"))
    if b == 1:
        print("You have chosen Scooty")
    elif b == 2:
        print("You have chosen Scooter")
elif a == 2:
    print("Sedan or SUV")
    c = int(input("Select your Car:"))
    if c == 1:
        print("You have chosen Sedan")
    elif c == 2:
        print("You have chosen SUV")