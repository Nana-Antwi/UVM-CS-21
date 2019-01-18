#Nana Antwi
#CS 21
#Assignment 6
#future.py


#design a program calculate total amount of money a user own in their bank account.

#variables
future_val = 0.0
present_val = 0.0
time_months = 0.0
interest_rate = 0.0

#user prompt statements and conditon loop statements
present_val = int(input('Enter the present value in your account: $'))
while present_val <= 0:
                    print('Invalid Entry')
                    present_val = int(input('Enter the present value in your account: $'))

interest_rate = float(input('Enter the monthly interest rate: %'))
while (interest_rate > 100) or (interest_rate < 0):
                    print('Invalid Entry')
                    interest_rate = float(input('Enter the monthly interest rate: %'))

time_months = int(input('Enter number of months: '))
while time_months <= 0:
                    print('Invalid Entry')
                    time_months = int(input('Enter number of months: '))




#declare constants
FUTURE_VAL = ((present_val) * ((1 + ((interest_rate) *.01))** (time_months)))


#display results
print("Accumlated amount after", time_months, "months in your account will be: $ ", (format(FUTURE_VAL, '.2f')))  
    
