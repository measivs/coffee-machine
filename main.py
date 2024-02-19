MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def insufficient_resources():
    if q == 'espresso':
        if resources['water'] < 50:
            print('Sorry there is not enough water.')
            return True
        if resources['coffee'] < 18:
            print('Sorry there is not enough coffee.')
            return True
    elif q == 'latte':
        if resources['water'] < 200:
            print('Sorry there is not enough water.')
            return True
        if resources['milk'] < 150:
            print('Sorry there is not enough milk.')
            return True
        if resources['coffee'] < 24:
            print('Sorry there is not enough coffee.')
            return True
    elif q == 'cappuccino':
        if resources['water'] < 250:
            print('Sorry there is not enough water.')
            return True
        if resources['milk'] < 100:
            print('Sorry there is not enough milk.')
            return True
        if resources['coffee'] < 24:
            print('Sorry there is not enough coffee.')
            return True
    return False


def coins_process():
    global money
    print('please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    coins_sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if q == 'espresso':
        if coins_sum > 1.5:
            change = round(coins_sum - 1.5, 2)
            print(f'Here is ${change} in change.')
            print(f'here is your espresso ☕ enjoy!')
            resources['water'] -= 50
            resources['coffee'] -= 18
            money += 1.5
        else:
            print('Sorry that\'s not enough money. Money refunded.')
    if q == 'latte':
        if coins_sum > 2.5:
            change = round(coins_sum - 2.5, 2)
            print(f'Here is ${change} in change.')
            print(f'here is your latte ☕ enjoy!')
            resources['water'] -= 200
            resources['milk'] -= 150
            resources['coffee'] -= 24
            money += 2.5
        else:
            print('Sorry that\'s not enough money. Money refunded.')
    if q == 'cappuccino':
        if coins_sum > 3:
            change = round(coins_sum - 3, 2)
            print(f'Here is ${change} in change.')
            print(f'here is your cappuccino ☕ enjoy!')
            resources['water'] -= 250
            resources['milk'] -= 100
            resources['coffee'] -= 24
            money += 3
        else:
            print('Sorry that\'s not enough money. Money refunded.')


money = 0
process_continue = True
while process_continue:
    q = input('What would you like? (espresso/latte/cappuccino): ')
    if q == 'off':
        process_continue = False
    elif q == 'report':
        print(f'water: {resources['water']}ml')
        print(f'milk: {resources['milk']}ml')
        print(f'coffee: {resources['coffee']}ml')
        print(f"money: ${money}")
    else:
        if not insufficient_resources():
            coins_process()
