# import random
# playing = True
# num = str(random.randint(0,9))
# while playing:
#     guess = input("Give me your guess:")
#     if num==guess:
#         print("You win!")
#         break
#     else:
#         print("Try again")
# import random
# while True:
#     user_action = input("Rock Paper Scissors:")
#     a = ["Rock","Paper","Scissors"]
#     computer_action = random.choice(a)
#     if user_action==computer_action:
#         print("Its a tie!")
#     elif user_action=="Rock":
#         if computer_action=="Scissors":
#             print("Rock beats Scissors, You win!")
#         else:
#             print("Paper beats Rock, You lose")
#     elif user_action=="Paper":
#         if computer_action=="Rock":
#             print("Paper beats Rock, You win!")
#         else:
#             print("Scissors beats Paper, You lose")
#     elif user_action=="Scissors":
#         if computer_action=="Paper":
#             print("Scissors beat Paper, You win")
#         else:
#             print("Rock beats Scissors, You lose")
#     b = input("Want to play again, Y for Yes N for No:")
#     if b=="N":
#         break
import math
print(math.ceil(25.32))
print(math.floor(25.32))
x=10
y=-15
print(math.copysign(x,y))
print(math.fabs(-24))
print(math.gcd(17,34))