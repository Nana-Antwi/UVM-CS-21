#CS021A
#Kayvan Ehteshami, Nana Antwi, Battour Gyau, Amanda Kurtz
#ATM Simulator
print("Welcome to ATM simulator 2014.\nIn order to begin, we need to set up your account")
#define variables

againe = False

while againe == False:
	Name = input("We need a name for your account, please enter your full name: ")
	Pin = int(input("Please enter a four digit pin to be associated with your account: "))
	while Pin < 0 or Pin > 9999:
		Pin = int(input("That is invalid input please enter a four digit pin to be associated with your account: "))
	AccountC = float(input("Please make a deposit to your checking while you set up your account: \n"))
	while AccountC <= 0:
		AccountC = format(float(input("That is invalid input please make a deposit to your checking while you set up your account: ")), '.2f')
	AccountS = float(input("Please make a deposit to your savings while you set up your account: \n"))
	while AccountS <= 0:
		AccountS = format(float(input("That is invalid input please make a deposit to your savings while you set up your account: ")), '.2f')
	print("Verify the following information: \n Your name is: " + str(Name) + "\n Your pin is: " + str(Pin) + "\n Your account has: $" + str(Account))
	againe = input("Is this information correct (True/False): ")
	if againe == "False" or againe == "false":
		againe = False
	else:
		againe = True
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
    

