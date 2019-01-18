#Nana Antwi
#CS-21
#homework 2
#part 2

#program 1

#when joe purchased the shares

#varaible declaration
number_shares_purchased = 0.0
cost_per_share = 0.0
stockbroker_commission = 0.0
cost_shares_without_commission = 0.0
commission_cost = 0.0
total_cost_purchase = 0.0

#declare constants
NUMBER_SHARES_PURCHASED = 2000
COST_PER_SHARE = 40.00
COMMISSION_RATE = 3
COST_SHARES_WITHOUT_COMISSION = (NUMBER_SHARES_PURCHASED) * (COST_PER_SHARE)

#to get the cost of shares without brokers commission
cost_shares_without_commission = ( NUMBER_SHARES_PURCHASED ) * (COST_PER_SHARE)

#to get brokers commission
commission_cost = ( (COST_SHARES_WITHOUT_COMISSION) * (COMMISSION_RATE)) / 100

#to get the total cost of purchase
total_cost_purchase = (COST_SHARES_WITHOUT_COMISSION) + (commission_cost)

#results
print ("Cost of shares without commission :", cost_shares_without_commission)
print ("Cost of commission :", commission_cost)
print ("Total cost of the purchase :", total_cost_purchase)

