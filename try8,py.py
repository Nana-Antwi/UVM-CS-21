#Nana Antwi
#CS-21
#Assignment 3
#question 1

#Design a program to calculate weight

#user input prompt in mass which is converted 

#weight= mass * 9.8

#declare variables
mass = float(input('Enter objects mass in killograms: '))
weight = (mass) * (9.8)


#results output
print('Weight of object is : ', weight) 

if mass >= 1000:
    print('Object is too heavy, It weighs more than 1000 newtons')

elif mass <= 10:
    print('Object is too light, It wighs less than 10 newtons')

     
