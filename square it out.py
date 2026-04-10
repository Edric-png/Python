a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
list1 = []
for i in range(a,b+1):
    list1.append(i*i)
print(list1)
even = [c for c in list1 if c%2==0]
print(even)
odd = [c for c in list1 if c%2!=0]
print(odd)