# Write a program that asks the user to enter replacement cost of a building,
# then displays the min amount of insurance needed to buy for the property (80% to cover structure)

replacement_cost = float(input('What is the cost for replacing your structure? '))
min_insurance = replacement_cost * .80
print('The minimum insurance you need is $', (format(min_insurance, '.2f')), 'to cover the replacement cost of your structure')

