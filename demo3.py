#Nana Antwi
#CS 21
#assignment 4
#design a program for analysing budget

#asisgn variables
budget = 0.0
spent = 0.0
total = 0.0
surplus_budget = 0.0
negatve_budget = 0.0
SENTINEL = 0.0

#user prompt inputs
budget = float(input('Enter total budget for the month: '))
spent = float(input('Enter an amount spent:(' +str(SENTINEL)))

#condition loop statements
while spent != SENTINEL:
    total = spent + total
    spent = (float(input('Enter an amount spent:(' +str(SENTINEL)))

if total > budget:
    print('Money Budgeted: $', format(budget, ',.2f'), sep=" ")
    print('Money Spent: $', format(total,',.2f'), sep=" ")
    negative_budget = total - budget
    print('You are $', format(negative_budget, ',.2f'), 'over your budget minimum, BALANCE YOUR BUDGET', sep=" ")
elif total < budget:
    print('Money Budgeted: $', format(budger, ',.2f'), sep=" ")
    print('Money Spent: $', format(total, ',.2f'), sep=" ")
    surplus_budget = budget - total
    print('You have $ ', format(surplus_budget, ',.2f'), 'extra money from budget, BALANCED BUDGET', sep=" ")
else:
    total = budget
    print('Money Budgeted: $', format(budget, ',.2f'), sep=" ")
    print('Money Spent: $', format(total, ',.2f'), sep=" ")
    print('You have a BALANCED budget')
