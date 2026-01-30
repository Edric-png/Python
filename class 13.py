# a = int(input("Enter any number"))
# for i in range (a):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# a = int(input("Enter any number:"))
# b = 1
# for i in range (a):
#     for j in range(i+1):
#         print(b,end=" ")
#         b = b+1
#     print()
a = int(input("Enter any number:"))
if a%2==0:
    h = int(a/2)
else:
    h = int(a/2)+1
s = h-1
for i in range (1,h+1):
    for d in range(1,s+1):
        print(end=" ")
    s = s-1
    b = 1
    for j in range(2*i-1):
        print(end=str(b))
        b = b+1
    print()
s = 1
for i in range(1,h):
    for j in range(1,s+1):
        print(end=" ")
    s = s + 1
    b = 1
    for j in range(1,2*(h-i)):
        print(end=str(b))
        b = b+1
    print()