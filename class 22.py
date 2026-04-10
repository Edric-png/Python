# tuplex = (6,2,8,1,7,4,5)
# print(tuplex)
# tuplex + tuplex == (9,)
# tuple1 = (50,20,10,70,50)
# print(tuple1.count(50))
# tuplex = (1,5,8,2,9,7,4,6,3,0)
# _slice = tuplex[3:5]
# print(_slice)
# _slice = tuplex[:6]
# print(_slice)
# def palind(r):
#     e = len(r) -1
#     s = 0
#     while (s<e):
#         if(r[s]!=r[e]):
#             return False
#         s += 1
#         e -= 1
#     return True
# r = (1,2,3,3,2,1)
# if (palind(r)):
#     print("It is flip-flop")
# else:
#     print("It is not flip-flop")
weather=(1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for i in range(0,7):
    if weather[i]==0:
        rainy += 1
    else:
        sunny += 1
if sunny>rainy:
    print("It is good weather")
else:
    print("It is bad weather")
    