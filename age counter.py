try:
    age = int(input("Enter your age:"))
    if(age<18):
        raise ValueError
    else:
        print("Your age is valid")
except ValueError as ex:
    print(ex)
if age%2==0:
    print("It is even")
else:
    print("It is odd")