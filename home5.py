#Nana Antwi
#CS 21
#Design a program that plays the game of 21 with the user.

#import languages
import random

#definition function
def main ():

	#declare varaiables
	user_total = 0.0
	computer_total = 0.0
	limit = 21

	#user prompt to roll dice
	yes_no = str(input('Do you want to roll a dice? yes/no '))

	#condition loop statements
	while yes_no == "yes" or yes_no == "no":
	
		if yes_no == "yes": 

			#dice rolls between the computer and the user
			user_1, user_2, computer_1, computer_2 = roll()

			#computations from the dice roll
			user_total = (user_1 + user_2)
			computer_total = (computer_1 + computer_2)
		

			#users total points
			print('User Point: ', user_total)

			

			#user rolls dice again
			yes_no = str(input('Do you want to roll a dice? yes/no '))

					#revalidation of response
			while yes_no!= "yes" and yes_no!= "no":
					print("Invalid Entry")

					yes_no = str(input('Do you want to roll a dice? yes/no '))

					#if user answers yea to the prompt
					if yes_no == "yes":


						#second dice rolls between the computer and the user
						user_1, user_2, computer_1, computer_2 = roll()

						#computations from the second dice roll
						user_total = (user_1 + user_2)
						computer_total = (computer_1 + computer_2)

							#users second dice roll total points
						print('User Point: ', user_total)

					#when uses wish to end turn
					elif yes_no== "no":


						#computer points from dice roll
						print('Computers points: ', computer_total)

							#to find winner of the game
						if computer_total == user_total and user_total <= limit:

								#the game is tie

								print('Tie')

							#when both players scored under 21
						elif computer_total <= limit and user_total <= limit:

								#if both under 21 and computer score more
								if computer_total > user_total:

									#computer is decalared winner
									return print('Computer wins the game of 21')

								#user is decalared winner
								else:
									return print('User wins the game of 21')
							#when both players are over the score 21
						elif user_total > limit and computer_total > limit:
								#both over score total no one wins
								return print('There is no winner')

							#when computer score is more than score total
						elif user_total <= limit and computer_total > limit:
								#when users wins 
								print('User wins the game of 21')                                                         
							#when users score is more than score total
						elif computer_total <= limit and user_total >limit:
								#when computer wins 
								print('Computer wins the game 0f 21')
								#display computers points
								print('Computers points: ', computer_total)

				#to find winner of the game
				if computer_total == user_total and user_total == computer_total:

					#the game is tie

					print('Tie')

				#when both players scored under 21
				elif computer_total <= limit and user_total <= limit:

					#if both under 21 and computer score more
					if computer_total > user_total:

						#computer is decalared winner
						print('Computer wins the game of 21')

					#user is decalared winner
					else:
						print('User wins the game of 21')

				#when both players are over the score 21
				elif user_total > limit and computer_total > limit:

					#both over score total no one wins
					return print('There is no winner')

				#when computer score is more than score total
				elif user_total <= limit and computer_total > limit:

					#when users wins 
					return print('User wins the game of 21')               

				#when users score is more than score total
				elif computer_total <= limit and user_total >limit:

					#when computer wins 
					return print('Computer wins the game of 21')
	#all game score total                          
	else:
		#users score
		print('Users game total points: ', user_total)
		#computers score
		print('Computes game total points: ', computer_total)

		#declare time
		print('Tie!')

#dice roll function
def roll ():

	#users dice roll 1                          
	user_roll_1 = random.randint(1,6)

	#users dice roll 2
	user_roll_2 = random.randint(1,6)

	#computers dice roll 1
	computer_roll_1 = random.randint(1,6)

	#computers dice roll 2
	computer_roll_2 = random.randint(1,6)

	#display of data from rolls
	return user_roll_1, user_roll_2, computer_roll_1, computer_roll_2

#call main function
main()

