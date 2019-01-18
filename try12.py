#Nana Antwi
#Homework 3
#question 15

#design a program that converts input from seconds to minutes to hours to days.


#declare  variable contants.
#60 seconds equals a minute
#3600 seconds equals an hour
#86400 seconds equals a day

#user input to prompts
seconds = int(input('Enter number of seconds: ')


#conditon statements
if seconds <= 60:  
    minutes = seconds // 60
    print('The amount in minutes equals: ' (minutes)) 
elif seconds <= 3600:
    hours = seconds // 3600            
    print('The amount in hours equals: ' (hours))
elif seconds <= 86400:
    days = seconds // 86400
    print('The amount in days equals: ' (day))
