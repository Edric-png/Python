# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# a=b
# print(a is b)
# a = 26
# print(a>>3)
# b = 15
# print(b<<3)
Science=79
English=75
IndSST=68
UaeSST=73
Math=76
avg=(Science+English+IndSST+UaeSST+Math)/5
print(avg)
if avg>=91 and avg<=100:
    print("Your grade is A1")
elif avg>=81 and avg<91:
    print("Your grade is A2")
elif avg>=71 and avg<81:
    print("Your grade is B1")
else:
    print("Your grade is B2")