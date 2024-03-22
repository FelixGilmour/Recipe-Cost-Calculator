#imports
import random
import sys
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
recipename_input = input("What is your recipe's name that you are calculating the cost of:  ")

#wait
time.sleep(3)

#main code
print("Okay, now we can get started!")
time.sleep(3)

#creating the database and looping the code
def create_recipe_table():
  ingredient_sizing=int(input("How many ingredients are in your recipe:"))
  #box
  ingredients=[]
  
  #i_sizing
  for i in range(ingredient_sizing):
    
    #collecting the amount, unit, name, price
    name=input(f"Enter name of the ingredient {i+1}:")
    price=float(input(f"Enter in the price of the ingredient {i+1} ($):"))
    unit=input(f"Enter the ingredients unit {i+1}:")
    amount=float(input(f"Enter the amount using {i+1}:"))

    #add ingredients to the database
    ingredients.append((amount, unit, name, price))
    
    #found on a website idk how it works
    total_cost=sum(amount*price for amount,_,_,price in ingredients)
    servings=float(input("Enter your number of servings: "))
    cost_per_serving=total_cost/servings

    print(f"Great! So you want: {recipename_input} and a serving size of {servings} for the {recipename_input}!\n")

    #table/s showing on code
    print("Here is your recipe:")
    
    #print ingredients
    print("/nRecipie Ingredients")
    
    #asked ai for help with this part - is supposed to format the table correctly so the user can see it
    print("{:<10} {:<10} {:<15} {:<15}".format("Amount", "Unit", "Name", "Price"))
    for amount, unit, name, price in ingredients:
      #{.2f} is showng the string floating number
      print("{:<10} {:<10} {:<15} {:<15.2f}".format(amount, unit, name, price))
      
    #
    print("")
    #
    print("")


    #
    
    
    















#finish/start
create_recipe_table()
