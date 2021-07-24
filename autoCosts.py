# Write a program that asks the user to enter the monthly costs for the following
# expenses incurred from a car: loan payment, insurance, gas, oil, tires and maintenance
# Display the total monthly costs of these expenses, and total annual cost (30 days)

payment = float(input('Enter the amount of your monthly loan payment: '))
insurance = float(input('Enter the amount of your monthly insurance: '))
gas = float(input('Enter the amount of your monthly gas: '))
oil = float(input('Enter the amount of your monthly oil: '))
tires = float(input('Enter the amount of your monthly tires: '))
maintenance = float(input('Enter the amount of your monthly maintenance: '))

month_expenses = (payment + insurance + gas + oil + tires + maintenance)
year_expenses = (month_expenses * 12)

print('This is your monthly expense for owning your car: ', month_expenses)
print('This is your annual expense for owning your car: ', year_expenses)


