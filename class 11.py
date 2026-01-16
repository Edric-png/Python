# n = int(input("Enter any number"))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i + 1
#     print("Sum =",sum)
# i = 0
# while i == 0:
#     print(i)
n = int(input("Enter any number"))
sum = 0
i = n
while i > 0:
    d = i%10
    sum += d**3
    i //= 10
if n==sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")