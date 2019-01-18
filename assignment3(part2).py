r#Nana Antwi
#CS-21
#Assignment
#question 2

#Design a program to calculate BMI
#when a user input weight and height


#assign variables
#(weight, height, bmi)


#declare variables constants 
weight = float(input('Enter boby weight in pounds: '))
height = float(input('Enter height in inches: '))
bmi = (weight) * ((703) / (height) ** (2))


#results output
print('Your BMI is: ', bmi)

#condition statements
if height < 48 and weight < 50:
    print('ERROR, invalid height or weight')

elif bmi <= 18.5:
    print('You are underweight')

else:
    print('You are overweight')
