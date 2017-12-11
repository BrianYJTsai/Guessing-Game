#  File: GuessingGame.py

#  Description: Program uses binary search to locate a user defined number. User inputs a number to look for and the program
# determines what number it is in 7 steps if possible. 

#  Student Name: Brian Tsai

#  Student UT EID: byt76

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 4/10/17

#  Date Last Modified: 4/10/17

def main():
	print("Guessing Game")
	print()
	print("Think of a number between 1 and 100 inclusive.")
	print("And I will guess what it is in 7 tries or less.")
	print()
	prompt_valid = False
	
	# Wait for user to press 'y' or 'no' to start the game
	while(not prompt_valid):
		
		# Prompt the user
		prompt = str(input("Are you ready? (y/n): "))
		
		# Continue if the answer is 'y'
		if (prompt == 'y'):
			prompt_valid = True
		
		# End if the answer is 'no'	
		elif(prompt == 'n'):
			print()
			print("Bye")
			return
		
		# Make sure the user inputs a valid answer	
		else:
			continue
	
	# Initialize boundaries
	tries = 1
	low = 1
	hi = 100
	correct_input = False
	print()

	# Program does 7 guesses before it finishes
	while(tries <= 7):

		# The guess is in the middle of the low and hi limits
		mid = (low + hi)//2
		print("Guess", tries, ": The number you thought was", mid)
		
		# Prompt the user until they input a valid answer
		while (not correct_input):
			guess_prompt = (input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
			if (guess_prompt == "1" or guess_prompt == "-1" or guess_prompt == "0"):
				correct_input = True
		
		# Reset correct_input flag
		print()
		correct_input = False
		
		# Search lower half if the guess is too high
		if (guess_prompt == "1"):
			hi = mid - 1

		# Search upper half if the guess is too low 	
		elif (guess_prompt == "-1"):
			low = mid + 1
		
		# The answer has been found	
		else:
			print("Thank you for playing the Guessing Game.")
			break
		
		# Increment the number of tries	
		tries+=1	
	
	# Condition if the answer has not been found in the number of tries allowed
	if (tries > 7):
		print("Either you guessed a number out of range or you had an incorrect entry")		
main()
			


