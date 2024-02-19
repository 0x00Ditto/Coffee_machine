from coffee_price import coffee
from coin_operated import money
import random
import time

# This function gonna check if we have the minimal stock for make a coffee:
def checker(min_stock,actual_stock):
  all_good = True
  if min_stock['water'] > actual_stock['water']:
    print("We don't have enough water")
    all_good = False

  if min_stock['milk'] > actual_stock['milk']:
    print("We don't have enough milk")
    all_good = False

  if min_stock['coffee'] > actual_stock['coffee']:
    print("We don't have enough coffee")
    all_good = False

  if all_good:
    return"Good Choice!"
  else:
    return False


def find_coffee_details(choice):
  if choice in coffee:
    return coffee[choice]
  else:
    return "We don't have this coffee"

def money_operated(cost,money2):
  temp_calc = (
    float(money['quarter']) * int(money2['quarters']) +
    float(money['dime']) *  int(money2['dimes']) +
    float(money['nickel']) *  int(money2['nickles']) +
    float(money['penny']) *  int(money2['pennies'])
   )

  if cost['price'] > temp_calc:
    print("Sorry that's is not enough money. Money refunded.")
  elif cost['price'] == temp_calc:
    print("We prepare your coffee")
    for i in range(5, 0, -1):
      print(f"Your {cost['name']} be ready in {i}s")
      time.sleep(1)
    print(f"Enjoy your {cost['name']}!")
  elif temp_calc > cost['price']:
    print("We prepare your coffee")
    for i in range(5, 0, -1):
      print(f"Your {cost['name']} be ready in {i}s")
      time.sleep(1)
    print(f"Enjoy your {cost['name']}!")
    change = round(temp_calc - cost['price'],2)
    return f"Here is {change} in change"
  else:
    print("Sorry that's is not enough money. Money refunded.")


def machinecoffee():

  stock = {
  "water": random.randint(1,400),
  "coffee": random.randint(1,50),
  "milk": random.randint(1,200)
  }
  while True:

    money_user = {
      "quarters": 0,
      "dimes": 0,
      "nickles": 0,
      "pennies": 0
    }
    choice_coffee = input("What would you like? (Espresso/Latte/Cappuccino or 'quit' to exit): ").lower()
    if choice_coffee == 'quit':
      break
    if choice_coffee == 'report':
       print(stock)
       stock_max = input("Do you want refill our stock? Type ='Y' or 'N' ").lower()
       if stock_max == 'y':
         stock['water'] = 1000
         stock['coffee'] = 250
         stock['milk'] = 500
         continue
       else:
         return 0
    if choice_coffee == 'off':
      return 0
    coffee_details = find_coffee_details(choice_coffee)
    print(coffee_details)
    if coffee_details == 'hack':
      print(f"""
      {coffee_details['name']} \n
      {coffee_details['price']} \n
      {coffee_details['water']}  \n
      {coffee_details['coffee']}  \n
      {coffee_details['milk']}     \n
            """)
      return 0
    if coffee_details and checker(coffee_details, stock):
      print("Please insert Coins.")

      try:
        money_user['quarters'] = int(input("How many quarters?:"))
        money_user['dimes'] = int(input("How many dimes?:"))
        money_user['nickles'] = int(input("How many nickles?:"))
        money_user['pennies'] = int(input("How many pennies?:"))

      except ValueError:
        print("Invalid input, please insert numeric values.")
        continue

      money_response = money_operated(coffee_details,money_user)
      if money_response:
        print(money_response)
        # Update stock after successful transaction
        stock['water'] -= coffee_details['water']
        stock['coffee'] -= coffee_details['coffee']
        stock['milk'] -= coffee_details['milk']
        break
      else:
        continue
    else:
      continue

machinecoffee()