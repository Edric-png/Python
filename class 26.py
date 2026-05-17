# theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
#             '4': ' ' , '5': ' ' , '6': ' ' ,
#             '1': ' ' , '2': ' ' , '3': ' ' }
# board_keys = []
# for key in theBoard:
#     board_keys.append(key)
# def printBoard(board):
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])
# def game():
#     turn = 'X'
#     count = 0
#     for i in range(10):
#         printBoard(theBoard)
#         print("It's your turn," + turn + ".Move to which place?")
#         move = input()        
#         if theBoard[move] == ' ':
#             theBoard[move] = turn
#             count += 1
#         else:
#             print("That place is already filled.\nMove to which place?")
#             continue
#         # Now we will check if player X or O has won,for every move after 5 moves. 
#         if count >= 5:
#             if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")                
#                 break
#             elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break 
#             elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break 
#         if count == 9:
#             print("\nGame Over.\n")                
#             print("It's a Tie!!")
#         if turn =='X':
#             turn = 'O'
#         else:
#             turn = 'X'        
#     restart = input("Do want to play Again?(y/n)")
#     if restart == "y" or restart == "Y":  
#         for key in board_keys:
#             theBoard[key] = " "

#         game()
# if __name__ == "__main__":
#     game()
# Import necessary modules
import random 
import time

# Pick a number between 1 and 100
number=random.randint(1, 100) 

def intro():
	print("May I ask you for your name?")
	global name
	name = input()
	print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
	if(number%2==0):
		x='even'
	else:
		x='odd'
	print("\nThis is an {} number".format(x))
	time.sleep(.5)
	print("Go ahead. Guess!")
def pick():
	guessesTaken = 0
	while guessesTaken < 6:
		time.sleep(.25)
		#inserts the place to enter guess
		enter=input("Guess: ") 
		try:
			guess = int(enter)
			if guess<=100 and guess>=1:
				guessesTaken=guessesTaken+1
				if guessesTaken<6:
					if guess<number:
						print("The guess of the number that you have entered is too low")
					if guess>number:
						print("The guess of the number that you have entered is too high")
					if guess != number:
						time.sleep(.5)
						print("Try Again!")
					if guess==number:
						break
			if guess>100 or guess<1: 
				print("Silly Goose! That number isn't in the range!")
				time.sleep(.25)
				print("Please enter a number between 1 and 100")
		except: #if a number wasn't entered
			print("I don't think that "+enter+" is a number. Sorry")
	if guess == number:
		guessesTaken = str(guessesTaken)
		print('Good job, {}! You guessed my number in {} guesses!'.format(name, guessesTaken))
	if guess != number:
		print('Nope. The number I was thinking of was ' + str(number))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
	intro()
	pick()
	print("Do you want to play again?")
	playagain=input()