#Nana Antwi
#CS21
#Design a program that plays the game of 21 with the user.

#import python library nlanguages
import random

#main function
def main():

    #decalare varaibles
    user_total= 0.0
    computer_total= 0.0
    limit=21

    #user prompt to roll
    yes_no =str(input('Do you want to roll? yes/no'))

    #condition loop statement
    while yes_no!='yes' and yes_no!='no':

        #response to no 
        print("Invalid")

        #prompt user for input
        yes_no=str(input('Do you want to roll? yes/no'))

    #if the response is correct
    if yes_no=='yes':

        #dice roll between computer and user
        user_1, user_2, computer_1, computer_2=roll()

        #dice roll computation
        user_total+=(user_1+user_2)
        computer_total+=(computer_1+computer_2)

        #display computation
        print('Points:', user_total)

        #while loop when is yes and the user total is under 21
        while yes_no=='yes' and limit>=user_total:

            #ask user to roll again
            yes_no=str(input('Do you want to roll? yes/no '))

            #validation of condition
            while yes_no!='yes' and yes_no!='no':

                #response to input
                print('Invalid response')

                #prompt user for agin
                yes_no=str(input('Do you want to roll? yes/no '))

            #if response is yes game contiues
            if yes_no=='yes':

                #dice roll between user and computer
                user_1, user_2, computer_1, computer_2 =roll()

                #dice computation
                user_total+=(user_1+user_2)
                computer_total+=(computer_1+computer_2)

                #display of score
                print('Points:', user_total)

                #if user wishes to end turn
            elif yes_no=='no':

                #print the computers score
                print("Computer's points", computer_total)

                
                #condition to determine a tie game
                if computer_total==user_total and user_total<=limit:

                    #tie
                    return print('Tie!')

                #condition to determine winner
                elif computer_total<=limit and user_total<=limit:

                    #when computer points is greater
                    if computer_total>user_total:

                        #game results
                        return print('Computer wins!')

                    #else condition statements
                    else:

                        #game results
                        return print('User wins!')

                #condition loop revalidation
                elif user_total>limit and computer_total>limit:

                    #print no one wins
                    return print('No winner!')

                #condition to test loop statements
                elif user_total<=limit and computer_total>limit:

                    #game results
                    return print('User wins!')

                #if the cp is under the limit and the user is over the limit
                elif computer_total<=limit and user_total>limit:

                    #game results
                    return print('Computer wins!')
        
        #score points from game
        print("Computer's points", ctotal)

        #condition loop
        if computer_total==user_total and user_total<=limit:

            #game results
            return print('Tie!')

        #condition loop
        elif computer_total<=limit and user_total<=limit:

            #test of condition loops
            if computer_total>user_total:

                #game results
                return print('Computer wins!')
            #loop statement validation
            else:

                #game results
                return print('User wins!')

        #condition loop
        elif user_total>limit and computer_total>limit:

            #game results
            return print('Nobody wins!')

        #loop statement validation
        elif user_total<=limit and computer_total>limit:

            #game results
            return print('User wins!')

        #condition statements
        elif computer_total<=limit and user_total>limit:

            #game results
            return print('Computer wins!')

    #final condition test
    else:
        # user total
        print("Total User points:",user_total)

        # computer total
        print("Total Computer points:",computer_total)

        #game results if tie
        print('Tie Game')
 
#roll function
def roll():

    #user roll 1
    user_roll_1=random.randint(1,6)

    #user roll 2
    user_roll_2=random.randint(1,6)

    #cp roll 1
    computer_roll_1=random.randint(1,6)

    #cp roll 2
    computer_roll_2=random.randint(1,6)

    #reutrn data
    return user_roll_1, user_roll_2, computer_roll_1, computer_roll_2

#call main
main()
