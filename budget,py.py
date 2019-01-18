#Nana Antwi
#cs 21
#assigment 4
#budget.py
#design a program for analysing budget

#asisgn variables
spent = 0.0
expense = -1

#sentinel varaiable
sent_val = 0

#user prompt inputs
budget = float(input('Enter total budget for the month: '))


#condition loop statements
while expense != sent_val:
    expense = float(input('Enter amount spent("0" to quit):'))
    spent += expense

#output results of input
print('Budget: $', format(budget, '.2f'))
print('Spent: $', format(spent, '.2f'))

#contant variables
surplus_budget = (budget - spent)
negative_budget = (spent - budget)

#condition statement test
if spent > budget:
    print('You are $', format(negative_budget, '.2f'), 'over budget,BALANCE YOUR BUDGET')

elif spent < budget:
          print('You have $', format(surplus_budget, '.2f'), 'left of budget,BALANCED BUDGET')

else:
                print('You have a balanced working budget')
                
                
          
