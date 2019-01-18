#Nana Antwi
#CS 21
#design a program that collect rainfall data and calculates it average

#assign variables
w = 0.0
z = 0.0
rain = 0.0
months = 0.0
monthly_rainfall = 0.0
total_rainfall = 0.0

#declare variable constants
MONTHS = 12

#user prompt inputs
years = int(input('Enter number of years: '))
months = MONTHS*years

#condition loop statements
for w in range(1, (years + 1)):
    print('for year', z, ": ")
    for z in range (1,13):
        rain = (float(input('Enter amount of rainfall for the month: ' +str(z) + ": ")))
        total_rainfall = rain + total_rainfall
    monthly_rainfall = (total_rainfall)/(months)

#results output
print('For', months, 'months')
print('Total rainfall: ', format(total_rainfall, ',.2f'), 'inches')
print('Avreage monthly rainfall: ', format(monthly_rainfall, ',.2f'), 'inches')

    
