#Get details if loan
money_owed = float(input("Enter the amount of money owed in Kenyan shillings: \n")) 
apr = float(input("Enter the annual percentage rate (APR) (e.g., enter 5 for 5%): \n"))
payment = float(input("Enter the monthly payment amount in Kenyan shillings: \n"))
months = int(input("Enter the number of months to pay off the loan: \n"))

monthly_rate = apr / 100 / 12

for x in range(months):
    interest_paid = money_owed * monthly_rate
    
    money_owed = money_owed + interest_paid
    
    if money_owed < payment and money_owed > 0:
        print("The last payment is", money_owed)
        print("You paid off the loan in", x + 1, "months")
        break
    
    money_owed = money_owed - payment
   
print("paid", payment, "of which", interest_paid, "was interest") 
print("You still owe", money_owed, "after", months, "months")        
