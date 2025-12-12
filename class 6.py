# a = 7
# b = ""
# if a or b:
#     print("a and b is boolean")
# else:
#     print("a and b is not boolean")
# a = 6
# b = 2
# c = 2
# print(a != b)
# print(b != c)
# a = 8
# if a%2!=0:
#     print("Odd")
# else:
#     print("Even")
weight = float(input("Enter your weight"))
height = float(input("Enter your height"))
bmi = (weight/height**2)
print("your bmi is",bmi)
if bmi<18:
    print("you are underweight")
elif bmi<24:
    print("you are fit")
else:
    print("you are overweight")