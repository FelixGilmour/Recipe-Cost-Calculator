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
  ingredient_count = int(input("\nHow many ingredients are in your recipe: "))

#collecting inputs
  for i in range(ingredient_count):
      #Recipe Ingredients
      print(f"\nEntering ingredient {i+1} details:")
      print("Recipe Ingredients")
      name = input("Enter the name of the recipe ingredient: ")
      unit = input("Enter the recipe ingredient's unit (g/kg): ")
      #Ingredient Prices
      print("Ingredient Prices")
      price_per_unit = float(input("Enter the price per unit of the ingredient price ($): "))
      amount_needed = float(input("Enter the ingredient prices, amount that you need: "))
      unit = input("Enter the ingredient prices unit (g/kg): ")
      print("We will now add this to the date base and caculate the cost to male, the total cost and cost per serve!")
    
      #converting amounts as needed
      if unit.lower() == 'g':
          amount_needed_kg = amount_needed / 1000  
      else:
          amount_needed_kg = amount_needed

      #math convertions
      cost = (price_per_unit * amount_needed_kg)
    
      ingredients.append((amount_needed, unit, name, cost))

  #servings
  serving = float(input("\nEnter the number of servings you want: "))
  print(f"Great! So you want: {recipe_name} and {serving} servings!\n")

  #Calculate total cost
  total_cost = sum(cost for _, _, _, cost in ingredients)

  #Calculate cost per serving
  cost_per_serving = total_cost / serving

  #data
  print(f"\nRecipe: {recipe_name}")
  print(f"\nServings: {serving}")
  print("Recipe Ingredients:")
  print(f"{'Amount':<10} {'Unit':<10} {'Ingredient':<20}")
  for amount, unit, name in ingredients:
      print(f"{amount:<10} {unit:<10} {name:<20}")

  print("Ingredient Price:")
  print(f"{'Price':<10} {'Amount':<10} {'Unit':<20} {'Cost To Make':<20}")

  
  print(f"\nTotal: ${total_cost:.2f}")
  print(f"Per Serve: ${cost_per_serving:.2f}")

#Start the program
create_recipe_table()