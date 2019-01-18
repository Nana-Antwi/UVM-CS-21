#Nana Antwi
#CS 021
#Assignment 5
#program 1
#autombile.py

#Design a program that calculates monthly automobile budget and annual expenditure for user.

#Define Function
def show_expenses():
    
#variables
 total_expenses = 0.0

#user prompt input statements
 expense_loan = int(input('Enter monthly amount spent on loan: $'))
 expense_insurance = int(input('Enter monthly amount spent on insurance: $'))
 expense_gas = int(input('Enter monthly amount spent on gas: $'))
 expense_oil = int(input('Enter monthly amount spent on oil: $'))
 expense_tire = int(input('Enter monthly amount spent on tire: $'))
 expense_maintenance = int(input('Enter monthly amount spent on maintenance: $'))

#calculations of Constants 
 total_monthly_expense = (expense_loan + expense_insurance + expense_gas + expense_oil + expense_oil + expense_tire + expense_maintenance)
 annual_total = (total_monthly_expense) * 12

#display results 
 print('Total monthly expense: $', format(total_monthly_expense, '.2f'))
 print('Annual total expense: $', format(annual_total, '.2f'))

#calling of the function
show_expenses()
