#Nana Antwi
#cs 21
#assignment 4
#distance.py
#write a program that calculates distance
#distance is equal to speed muliple by time

#variables
speed = 0.0
time = 0.0
distance = 0.0
var_cons = 1.0

#user input variable
speed = float(input('Enter speed: ')) #user prompts


#condition loop statements
while speed <= 0:
    print('Speed must always be greater than zero')
    speed = int(input('Enter speed: '))
    time = int(input('Enter time: '))

while time <= 0:
    print('Time must always be greater than zero')
    time = int(input('Enter time: '))

#results output
print('Hour of distance treavelled')
print('---------------------------')

for var_cons in range(1, (time + 1)):
    distance = var_cons * speed
    print(var_cons, "\t", format(distance, ',.1f'))
