import menu

# Initial resources
machine_resources = {
    "water": 200,
    "milk": 200,
    "coffee": 100,
    "money": 0
}



def print_report():
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${machine_resources['money']:.2f}")

def refill_resources(machine_resources):
    print("Refilling resources manually...")

    water_add = int(input("How much water to add (ml)? "))
    milk_add = int(input("How much milk to add (ml)? "))
    coffee_add = int(input("How much coffee to add (g)? "))
    money_add = int(input("How much money to add ($)? "))

    machine_resources["water"] += water_add
    machine_resources["milk"] += milk_add
    machine_resources["coffee"] += coffee_add
    machine_resources["money"] += money_add

    print("Resources updated successfully!")
    print(machine_resources)



def check_resources(drink_name):
    """Return True if enough resources exist, else False"""
    ingredients_needed = menu.MENU[drink_name]["ingredients"]
    for item, amount in ingredients_needed.items():
        if machine_resources[item] < amount:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins:")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total

def make_coffee(drink_name):
    """Deduct ingredients and update money"""
    ingredients = menu.MENU[drink_name]["ingredients"]
    for item, amount in ingredients.items():
        machine_resources[item] -= amount
    machine_resources["money"] += menu.MENU[drink_name]["cost"]
    print(f"Here is your {drink_name} ☕. Enjoy!")

def transaction(drink_name):
    """Process coins and check if transaction is successful"""
    cost = menu.MENU[drink_name]["cost"]
    inserted = process_coins()
    if inserted >= cost:
        change = round(inserted - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        make_coffee(drink_name)
    else:
        print("Sorry, not enough money. Money refunded.")

# Main loop
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        break
    elif choice == "report":
        print_report()
    elif choice == "refill":
        print(machine_resources)
        refill_resources(machine_resources)

    elif choice in menu.MENU:
        if check_resources(choice):
            transaction(choice)
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
