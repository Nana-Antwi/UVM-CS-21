#lab 3
#Exercise 6
#Get user input about a data and assess validity

#Assign Variables
month = 0
day = 0
year = 0
magic = 0.0 
#User Input Day
day = int(input("enter the day of the month:"))

#User Input Month
month = int(input("enter the month:"))

#User Input Year
year = int(input("enter the year:"))

magic = day*month

#Check if the day is greater than/equal to 1 and less than/equal to 31
if(day < 1 and day > 31) :
   print("Error: Day is not valid.")

#Check if the month is >= 1 <=12
elif(month < 1 or month > 12 ) :
     print("ERROR: Month is not valid.")

#Check if the year >=0 but less than or equal to 99
elif(year <0 or year > 99):
     print("ERROR: Year is not valid.")

else:
    print("The date is ", month, '/', day, '/', year)

#Calculate day multiplied month -- in if statement

#Print Message
