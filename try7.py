#Nana Antwi
#CS-21
#homework 2
#part 2

#program 2

#when joe sold the shares

#varaible declaration
number_shares_sold = 0.0
cost_per_share = 0.0
strokbroker_commission = 0.0
cost_shares_without_commission = 0.0
commission_cost = 0.0
total_cost_sold = 0.0
total_money_made_after_commission = 0.0
cost_buying_stocks = 0.0
profit_sale_stocks = 0.0

#declare constants
NUMBER_SHARES_SOLD = 2000
COST_PER_SHARE = 42.75
COMMISSION_RATE = 3
COST_BUYING_STOCKS = 80000
COST_SHARES_WITHOUT_COMMISSION = (NUMBER_SHARES_SOLD) * (COST_PER_SHARE)
COMMISSION_COST = ( (COST_SHARES_WITHOUT_COMMISSION) * (COMMISSION_RATE) / 100)
TOTAL_MONEY_MADE_AFTER_COMMISSION= (COST_SHARES_WITHOUT_COMMISSION) - (COMMISSION_COST)

#to get the cost of shares sold without brokers commission
cost_shares_without_commission = (NUMBER_SHARES_SOLD) * (COST_PER_SHARE)

#to get brokers commission on the sale
commission_cost = ( (COST_SHARES_WITHOUT_COMMISSION) * (COMMISSION_RATE) / 100)

#total money he made from the sale after the brokers commission
total_money_made_after_commission = (COST_SHARES_WITHOUT_COMMISSION) - (COMMISSION_COST)

#profit made from buying and selling of shares
profit_sale_stocks = (TOTAL_MONEY_MADE_AFTER_COMMISSION) - (COST_BUYING_STOCKS)

#results
print ("Cost of the sale of shares without brockers commission : ", cost_shares_without_commission)
print ("Cost of brokers commission : ", commission_cost)
print ("Total made after brokers commission : ", total_money_made_after_commission)
print ("Profit made from buying and selling of shares : ", profit_sale_stocks)
