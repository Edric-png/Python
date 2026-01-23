# a = input("Enter anything:")
# b = input("Enter any letter:")
# i = 0
# count = 0
# while (i < len(a)):
#     if (a[i]==b):
#         count = count + 1
#     i = i + 1
# print(count)
a = int(input("upperlimit"))
b = int(input("lowerlimit"))
for i in range(b,a+1):
    if i > 1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)