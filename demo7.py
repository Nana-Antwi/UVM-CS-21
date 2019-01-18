#Nana Antwi
#CS 021
#Assignment 5
#paint job estimator

#design a program to calculate labor hours and materials needed for a paint job

#function
def show_cost_estimate():


#Variables
 total_paintjob_cost = 0.0
 area_to_paint = 0.0
 gallons_needed = 0.0
 hours_labor = 0.0

#constant variables
 HOURS_OF_LABOR = 8

#user prompt inputs statements
 area_to_paint = float(input('Enter wall space in square feet to be painted: '))
 gallons_needed = float(input('Enter the cost per a gallon of paint: '))

#calculations of constants
 number_gal = (area_to_paint) / 115
 hours_labor = (HOURS_OF_LABOR) * number_gal
 total_gal_cost = (number_gal) * (gallons_needed)
 total_labor_cost = (number_gal) * 8 * 20
 total_paintjob_cost = (total_labor_cost) + (total_gal_cost)


#display results
 print('Gallons of paint to be used: ', number_gal)
 print('Hours of Labor: ', hours_labor)
 print('Total paint charges: ', total_gal_cost)
 print('Total labor cost: ', total_labor_cost)
 print('Total cost for a paint job: ', total_paintjob_cost)

#recall of function
show_cost_estimate()
            
