#Nana Antwi
#Homework 3
#question 15

#design a program that converts input from seconds to minutes to hours to days.

#general information about time.
#60 seconds equals a minute
#3600 seconds equals an hour
#86400 seconds equals a day

#assign varialbles
seconds = 0.0
minutes = 0.0
hours = 0.0
days = 0.0
sec_2 = 0.0

#declare variable constants
DAYS = 86400
HOURS = 3600
MINUTES = 60

#user prompt input
seconds = int(input('Enter the number of seconds: '))

#conditional statements
if seconds < 0:
    print('Invalid entry seconds value must be >= 0')

else:
    days = seconds // DAYS
    hours = (seconds%DAYS) // HOURS
    minutes = (seconds%HOURS) // MINUTES
    sec_2 = seconds%MINUTES

#results output
    print( seconds, 'seconds', '=', days, 'days', '=', hours, 'hours', '=', minutes, 'minutes')
