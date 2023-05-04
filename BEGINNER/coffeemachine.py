MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def money():
    print("Please enter coins:\n")
    p = float(input("How many pennies? "))
    n = float(input("How many nickles? "))
    d = float(input("How many dimes? "))
    q = float(input("How many quarters? "))
    balance = p * 0.01 + n * 0.05 + d * 0.1 + q * 0.25
    return round(balance, 2)


profit = 0
machine = True
while machine:
    coffee = input("What would you like?(espresso/latte/cappuccino)\n").lower()


    def check_resource():
        if resources['water'] < MENU[coffee]['ingredients']['water']:
            print("Not enough water.")
            return False
        if resources['milk'] < MENU[coffee]['ingredients']['milk']:
            print("Not enough milk.")
            return False
        if resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
            print("Not enough coffee.")
            return False
        else:
            return True


    def resource_update():
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
        resources['milk'] -= MENU[coffee]['ingredients']['milk']


    if coffee == 'espresso':
        if check_resource():
            total = money()
            if total > MENU[coffee]['cost']:
                print("Here is your espresso coffee sir/ma'am. Enjoy.")
                print(f"Here is your change ${total - MENU[coffee]['cost']}")
                profit += MENU[coffee]['cost']
                resource_update()

            else:
                print("Not enough coins")

    elif coffee == 'latte':
        if check_resource():
            total = money()
            if total > MENU[coffee]['cost']:
                print("Here is your latte coffee sir/ma'am. Enjoy.")
                print(f"Here is your change ${round(total - MENU[coffee]['cost'],2)}")
                profit += MENU[coffee]['cost']
                resource_update()

            else:
                print("Not enough coins")

    elif coffee == 'cappuccino':
        if check_resource():
            total = money()
            if total > MENU[coffee]['cost']:
                print("Here is your cappuccino coffee sir/ma'am. Enjoy.")
                print(f"Here is your change ${total - MENU[coffee]['cost']}")
                profit += MENU[coffee]['cost']
                resource_update()

            else:
                print("Not enough coins")

    elif coffee == 'report':
        print(f" Water : {resources['water']}mL\n Milk : {resources['milk']}mL\n Coffee : {resources['coffee']}gm\n "
              f"Money : ${profit} ")

    elif coffee == 'off':
        machine = False
