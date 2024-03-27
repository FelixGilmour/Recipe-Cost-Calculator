#imports
import time

#start
name = "Felix Gilmour"
school = "James Hargest College"
course = "Programming Evidence Internal for 2.7 and 2.8 ~ 12 credits"
due_date = "Due: 12 April 2024"

#/n representing new lines
print(f"Name: {name}\n"
      f"{school}\n"
      f"{course}\n"
      f"{due_date}\n\n")
time.sleep(1)

#entername
name_input = input("Enter your name: ")
print(f"Welcome {name_input} to my Recipe Cost Calculator!\n")

#wait
time.sleep(3)

#recipename
recipe_name = input("What is your recipe's name that you are calculating the cost of:  ")

#wait
time.sleep(3)

#main code
print("Okay, now we can get started!")
time.sleep(3)

#creating the database and looping the code
def create_recipe_table():
  ingredients = []
  # to store costs of individual ingredients
  ingredient_cost = []  
  ingredient_count = int(input("\nHow many ingredients are in your recipe: "))

  #collecting inputs
  for i in range(ingredient_count):
      #Recipe Ingredients
      print(f"\nEntering ingredient {i+1} details:")
      print("Recipe Ingredients")
      amount_needed1 = float(input("Enter the recipe ingredient's, amount that you need: "))
      unit1 = input("Enter the recipe ingredient's unit (g/kg): ")
      name1 = input("Enter the name of the recipe ingredient: ")

      #Ingredient Prices
      print("Ingredient Prices")
      price_per_unit2 = float(input("Enter the price per unit of the ingredient price ($): "))
      amount_needed2 = float(input("Enter the ingredient prices, amount that you need: "))
      unit2 = input("Enter the ingredient prices unit (g/kg): ")
      print("We will now add this to the date base and caculate the cost to make, the total cost and cost per serve!")

      #converting the amounts as needed
      if unit1.lower() == 'g':
          amount_needed_kg1 = amount_needed1 / 1000  
      else:
          amount_needed_kg1 = amount_needed1

      if unit1.lower() == 'g':
          amount_needed_kg2 = amount_needed2 / 1000  
      else:
          amount_needed_kg2 = amount_needed2

      #math conversions
      cost = price_per_unit2 * amount_needed_kg1
      ingredient_cost.append(cost)  #cost of ingredients
      ingredients.append((amount_needed1, unit1, name1, price_per_unit2, amount_needed2, unit2))

  #servings
  serving = float(input("\nEnter the number of servings you want: "))
  print(f"Great! So you want: {recipe_name} and {serving} servings!\n")

  #Calculate total cost
  total_cost = sum(ingredient_cost)

  #Calculate cost per serving
  cost_per_serving = total_cost / serving

  #data
  print(f"\nRecipe: {recipe_name}")
  print(f"\nServings: {serving}")
  #prints Recipe Ingredients
  print("Recipe Ingredients:")
  print(f"{'Amount':<10} {'Unit':<10} {'Ingredient':<20}")
  for amount1, unit1, name1, _, _, _ in ingredients:
      print(f"{amount1:<10} {unit1:<10} {name1:<20}")

  #prints Ingredient Price
  print("Ingredient Price:")
  print(f"{'Price':<10} {'Amount':<10} {'Unit':<20} {'Cost To Make':<20}")
  for price_per_unit2, amount_needed2, unit2, _ , _, _ in ingredients:
      print(f"{price_per_unit2:<10} {amount_needed2:<10} {unit2:<10} {name:<20}")
    
  #prints total cost
  print(f"\nTotal: ${total_cost:.2f}")
  print(f"Per Serve: ${cost_per_serving:.2f}")

#Start the program
create_recipe_table()