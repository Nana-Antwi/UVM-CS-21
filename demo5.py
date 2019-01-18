#Nana Antwi
#CS 021
#Assignment 5
#autombile program

#Design a program calculates monthly automobile budget

#Function
def show_expenses():
    
#variables
 total_expenses = 0.0

#input statements
 expense_loan = int(input('Enter monthly amount spent on loan: $'))
 expense_insurance = int(input('Enter monthly amount spent on insurance: $'))
 expense_gas = int(input('Enter monthly amount spent on gas: $'))
 expense_oil = int(input('Enter monthly amount spent on oil: $'))
 expense_tire = int(input('Enter monthly amount spent on tire: $'))
 expense_maintenance = int(input('Enter monthly amount spent on maintenance: $'))

#Constants
 total_monthly_expense = (expense_loan + expense_insurance + expense_gas + expense_oil + expense_oil + expense_tire + expense_maintenance)
 annual_total = (total_monthly_expense) * 12

#results
 print('Total monthly expense: $', total_monthly_expense)
 print('Annual total expense: $', annual_total)

show_expenses()
