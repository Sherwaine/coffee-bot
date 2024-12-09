# Coffee Bot: A simple program for ordering coffee

# Helper function to print an error message when input is invalid
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Function to get the size of the drink
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    res = res.lower()
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()  # Recursively prompt the user until a valid input is given

# Function to handle ordering a latte
def order_latte():
    res = input('And what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n> ')
    res = res.lower()
    if res == 'a':
        return '2% milk latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()  # Recursively prompt for valid milk choice

# Function to handle ordering a mocha (including the special peppermint option)
def order_mocha():
    while True:
        res = input('Would you like to try our limited-edition peppermint mocha?\n[a] Sure!\n[b] Maybe next time!\n> ')
        if res == 'a':
            return 'peppermint mocha'
        elif res == 'b':
            return 'mocha'
        else:
            print_message()
            # Continue prompting until a valid choice is made

# Function to ask for the type of drink
def get_drink_type():
    res = input('What type of drink would you like?\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n> ')
    res = res.lower()
    if res == 'a':
        return 'brewed coffee'  # Directly return brewed coffee
    elif res == 'b':
        return order_mocha()  # Return the result of order_mocha()
    elif res == 'c':
        return order_latte()  # Return the result of order_latte()
    else:
        print_message()
        return get_drink_type()  # Recursively prompt until valid input is given

# Main coffee bot function to handle the ordering process
def coffee_bot():
    print('Welcome to the cafe!')  # Welcome message
    
    order_drink = 'y'  # Default response to continue ordering
    drinks = []  # List to store all drinks ordered

    while order_drink == 'y':
        size = get_size()  # Get the size of the drink
        drink_type = get_drink_type()  # Get the type of drink
        
        # Format and append the order
        drink = '{} {}'.format(size, drink_type)
        print('Alright, that\'s a {}!'.format(drink))
        drinks.append(drink)
        
        # Ask if the customer wants to order more
        while True:
            order_drink = input('Would you like to order another drink? (y/n) \n> ')
            if order_drink in ['y', 'n']:
                break
    
    # Display all orders
    print('Okay, so I have:')
    for drink in drinks:
        print('-', drink)
    
    # Ask for customer name
    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your order will be ready shortly.'.format(name))

# Call the coffee bot to start the process
coffee_bot()
