# Write a program that will ask users for fat and carbohydrate grams consumed in a day
# Then, calculate the number of calories from fat and carbs (each)
# Fat grams = 9 cals, carb grams = 4 cals, 50g fat = 450 cals

def main():
    fat = int(input('How many fat grams have you eaten today? '))
    carbs = int(input('How many carbs have you eaten today? '))
    day_fat(fat)
    day_carbs(carbs)

def day_fat(num):
    total_fat = (num * 9)
    print('Your total fat calories for the day is: ', total_fat)

def day_carbs(num):
    total_carbs = (num * 4)
    print('Your total carbohydrate calories for the day is: ', total_carbs)

main()