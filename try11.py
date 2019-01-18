#Nana Antwi
#CS-21
#Assignment
#question 2

#Design a program to calculate BMI

#Declare Variables 
weight = float(input('Enter boby weight in pounds: '))
height = float(input('Enter height in inches: '))
bmi = (weight) * ((703) / (height) ** (2))

#results
print('Your BMI is: ', bmi)

#statements
if bmi <= 18.5:
    print('You are underweight')
if height < 48 and weight < 50:
    print('ERROR, invalid height or weight')
else:
    print('Your are overweight')

                     
