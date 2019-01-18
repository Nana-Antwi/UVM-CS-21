#Nana Antwi
#CS-21
#Assignment 3
#Question 4

#Assign Variables
month = 0
day = 0
year = 0
magic_date = 0.0

#Declare Variables
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
year = int(input('Enter a year: '))
magic_date = ((day) * (month) == (year))

if (day) * (month) == (year):
    print('Date is magic.')

else:
    print('Date is not magic.')
