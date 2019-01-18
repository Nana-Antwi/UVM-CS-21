#Deposit

DepositC = AccountC
DepositC = float(input('Enter amount you wish to deposit into your checking account'))
DepositS = AccountS
DepositS = float(input('Enter amount you wish to deposit into your savings account'))

#withdrawal
withdrawalC = (AccountC) - float(input('Enter amount you wish to withdraw from your checking account'))
withdrawalS = (AccountS) - float(input('Enter amount you wish to withdraw from your savings account'))

while withdrawalC >= 240:
    print("You can't withdraw more than $240")
    withdrawalC = (AccountC) - float(input('Enter amount you wish to withdraw from your checking account'))

if withdrawalS >= 240:
       print(" You can't withdraw more than $240")
       withdrawalS = (AccountS) - float(input('Enter amount you wish to withdraw from your savings account'))
else:
    withdrawalC == withdrawalC
    print(" You have withdrew", withdrawalC, "from your checking account")

    withdrawalS == withdrawalS
    print("You have withdrew", withdrawalS, "from your checking account")
    

    
