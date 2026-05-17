n = int(input("Choose any number:"))
odd = [i for i in range(n) if i%2==1]
print(odd)
fruits = ["apple", "banana", "cherry"]
new = [f.capitalize() for f in fruits]
print(new)