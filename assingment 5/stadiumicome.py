#Nana Antwi
#CS 021
#assignment 5
#program 2
#stadiumincome.py

#design a program allow users calculate the total amount of tickets sold and the number sold at each class.

#Define function
def show_income():
 
#variables
 total_amount_sold = 0.0
 total_class_a = 0.0
 total_class_b = 0.0
 total_class_c = 0.0

#user prompt input statements
 class_a = int(input('Enter the number of class A tickets sold: '))
 class_b = int(input('Enter the number of class B tickets sold: '))
 class_c = int(input('Enter the number of class C tickets sold: '))

#Variable constants
 CLASS_A = 15
 CLASS_B = 12
 CLASS_C = 9

#calculations of totals in the function
 total_class_a = (CLASS_A) * (class_a)
 total_class_b = (CLASS_B) * (class_b)
 total_class_c = (CLASS_C) * (class_c)
 total_amount_sold = (total_class_a) + (total_class_b) + (total_class_c)

#display results
 print('Total amount of class A tickets sold: $ ', total_class_a)
 print('Total amount of class B tickets sold: $ ', total_class_b)
 print('Total amount of class C tickets sold: $ ', total_class_c)
 print('Total amount of tickets sold: $ ', total_amount_sold)

#function call
show_income()
