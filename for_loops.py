# in shell range(7) means from 0 to 6
for i in range(7):
    print(i)  # prints numbers from 0 to 6

print("-----")

# it can be customized to start on a specific number and end on a specific number with a step value
for i in range(3, 10, 2):
    print(i)  # prints numbers from 3 to 9 with a step of 2
    
print("-----")

total = 0
expenses = [300, 200, 400, 600, 150]
for i in range(7):
    expenses.append(float(input("Enter an expense:")))
total = sum(expenses)

print("The total expenses are: ksh", total, sep="")

tot = 0
exp = []
num_expenses = int(input("How many expenses do you want to enter? "))
for i in range(num_expenses):
    exp.append(float(input("Enter an expense: ")))
tot = sum(exp)
print("The total expenses are: ksh", tot, sep="")