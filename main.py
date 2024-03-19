import time
import random
import sys

#start
name = "Felix Gilmour"
school = "James Hargest College"
course = "Programming Evidence Internal for 2.7 and 2.8 ~ 12 credits"
due_date = "Due: 12 April 2024"
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
time.sleep(1)
servingsize_input = input("How many servings are in your recipe:  ")
print(f"Great! So you want: {recipename_input} and a serving size of {servingsize_input} for the {recipename_input}!\n")

#wait
time.sleep(3)

#main code
print("Okay, now we can get started!")
time.sleep(3)

#creating the database
def create_recipe_table():
  ingredient_sizing=int(input("How many ingredients are in your recipe:"))
  #box
  ingredients=[]
  #i_sizing
  for i in range(ingredient_sizing):
    #amount, unit, name, price
    amount=float(input(f"Enter Amount {i+1}:"))
    unit=input(f"Enter Unit {i+1}:")
    name=input(f"Enter name of the ingredient {i+1}:")
    price=float(input(f"Enter in the price of the ingredient {i+1} (Per unit):"))

    #add ingredients toi the database
    



#finish area
