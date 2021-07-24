# Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles
# The conversion formula is Miles = Kilo x 0.6214

distance = float(input('What is your distance in kilometers? '))
miles = distance * 0.6214
print('Your distance is', (format(miles, '.2f')), 'miles when converted to miles')
