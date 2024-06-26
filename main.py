import time

# start
name = "Felix Gilmour"
school = "James Hargest College"
course = "Programming Evidence Internal for 2.7 and 2.8 ~ 12 credits"
due_date = "Due: 12 April 2024"

# /n representing breaking new lines
print(f"\033[4;31;40m Name: {name}\n"
      f"{school}\n"
      f"{course}\n"
      f"{due_date}\n\n")
time.sleep(1)

# age verification
is_age_verified = True
#while true changed format to while is_age_verified:
while is_age_verified:
    print("\033[0;30;47m This is designed for people aged between 13 and 18 years old")
    age_input = input("Please enter your age: ")
    if not age_input.isdigit():
        print("Please enter a valid age")
    else:
      #if age lower or older then prints invalid age
        age = int(age_input)
        if age < 13:
            print("You are too young to use this program")
        elif age > 18:
            print("You are too old to use this program")
        else:
            print("You are the correct age to use this program")
            break

# enter name
name_input = input("\033[4;31;40m Enter your name: ")

#prints name
print(f"Welcome {name_input} to my Recipe Cost Calculator!\n")

# wait
time.sleep(3)

# main code
print("Okay, now we can get started!")
time.sleep(3)

# creating the database and looping the code
def create_recipe_table():
    ingredients = []
    # stores costs of individual ingredients
    ingredient_cost = []
    while True:
        try:
          #asks for ingredients count
            ingredient_count = int(input("\033[1;34;40m \nHow many ingredients are in your recipe: "))
        except ValueError:
          #prints invalid input
            print("Please enter a valid number")
            continue
        else:
            break

    # collecting inputs
    for i in range(ingredient_count):
        while True:
            # Recipe Ingredients
            # collecting ingredient count and adds +1 every time it loops
            print(f"\nEntering ingredient {i + 1} details:")
            # printing recipe ingredients
            print("Recipe Ingredients")

            # collecting the amount needed 1
            try:
                amount_needed1 = int(input("Enter the recipe ingredient's amount that you need, number only: "))
            except ValueError:
                print("Please enter a valid number")
                continue

            # collecting the unit 1
            unit1 = input("Enter the recipe ingredient's unit (g/kg): ")

            # collecting the name 1
            name1 = input("Enter the name of the recipe ingredient: ")

            # Ingredient Prices
            print("Ingredient Prices")

            # collecting the price per unit 2
            try:
                price_per_unit2 = int(input("Enter the price per unit of the ingredient price number only ($): "))
            except ValueError:
                print("Please enter a valid number")
                continue

            # collecting the amount needed 2
            try:
                amount_needed2 = int(input("Enter the ingredient prices, amount that you need number only: "))
            except ValueError:
                print("Please enter a valid number")
                continue

            # collecting the unit 2
            unit2 = input("Enter the ingredient prices unit (g/kg): ")

            # printing database results
            time.sleep(3)
            print("We will now add this to the database and calculate the cost to make, the total cost and cost per serve!")
            time.sleep(3)

            # converting the amounts as needed
            # converting to kg
            if unit1.lower() == 'g':
                amount_needed_kg1 = amount_needed1 / 1000
            else:
                amount_needed_kg1 = amount_needed1
#if unit 1~or 2 is not in kg and in g converting to g to pput into the final output
            if unit2.lower() == 'g':
                amount_needed_kg2 = amount_needed2 / 1000
            else:
                amount_needed_kg2 = amount_needed2

            # math conversions
            cost = price_per_unit2 * amount_needed_kg1
            ingredient_cost.append(cost)  # cost of ingredients
            ingredients.append((amount_needed1, unit1, name1, price_per_unit2, amount_needed2, unit2))
            break

    # recipe name
    recipe_name = input("What is your recipe's name that you are calculating the cost of:  ")

    # wait
    time.sleep(3)

    # asking for serving count and dening continuing if a word
    while True:
        try:
            serving = float(input("\nEnter the number of servings you want: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        else:
            break
          
#confirming what the user wants
    time.sleep(3)
    print(f"Great! So you want: {recipe_name} and {serving} servings!\n")

    # Calculate total cost
    total_cost = sum(ingredient_cost)

    # Calculate cost per serving
    cost_per_serving = total_cost / serving

    # seps
    sep1 = '💵'
    sep2 = '📝'

    # data printed
    print(f"\nRecipe: {recipe_name}")
    print(f"\nServings: {serving}")
  
    # prints Recipe Ingredients
    print("Recipe Ingredients:")
    print(f"{'Amount':<10} {'Unit':<10} {'Ingredient':<20}")
    for amount1, unit1, name1, _, _, _ in ingredients:
        print(f"{sep1} {amount1:<10} {unit1:<10} {sep2} {name1:<20}")

    # prints Ingredient Price
    print("Ingredient Price:")
    print(f"{'Price':<10} {'Amount':<10} {'Unit':<10}")
    for _, _, _, price_per_unit2, amount_needed2, unit2 in ingredients:
        print(f"{sep1} {price_per_unit2:<10} {amount_needed2:<10} {unit2:<10}")

    # prints total cost
    print(f"\nTotal: ${total_cost:.2f}")
    print(f"Per Serve: ${cost_per_serving:.2f}")


    time.sleep(10)

    #play again
    playagain = input("Do you want to play again, yes or no?>>  ")
    if playagain.lower() == 'yes':
      #f allow name to be printed in the code
      print(f"Nah, you can't play again {name_input}!")
  
    else:
      print("See ya later, loser")
  
# Start the program
create_recipe_table()