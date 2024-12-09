
# Coffee Bot

## Description
Coffee Bot is an interactive command-line program that allows users to order drinks at a cafe. It asks for drink size, type (such as brewed coffee, mocha, or latte), and additional options like milk choice. The bot also provides a limited-edition special drink (peppermint mocha) and handles multiple drink orders. 

## Features
- Customizes drink size (Small, Medium, Large)
- Orders various drink types (Brewed Coffee, Mocha, Latte)
- Latte milk options: 2% milk, Non-fat milk, Soy milk
- Special limited edition: Peppermint Mocha
- Handles multiple orders
- Validates user input and requests corrections when necessary
- Collects the user's name and confirms the order at the end

## How to Run
1. Clone this repository to your local machine.
2. Navigate to the project folder in the terminal.
3. Run the script by typing:

```bash
python coffee_bot.py
```

## Usage

1. The bot will greet you and ask for the size of your drink (Small, Medium, Large).
2. Next, you'll choose the type of drink you want (Brewed Coffee, Mocha, or Latte).
3. If you choose a latte, you will be asked for your milk preference (2% milk, Non-fat milk, or Soy milk).
4. If you choose a mocha, you will have the option to try a limited-edition peppermint mocha.
5. After ordering, you can add more drinks to your order or confirm your final order.
6. Finally, the bot will ask for your name and print a confirmation message with your order.

## Example
```
Welcome to the cafe!
What size drink can I get for you?
[a] Small
[b] Medium
[c] Large
> b
What type of drink would you like?
[a] Brewed Coffee
[b] Mocha
[c] Latte
> c
And what kind of milk for your latte?
[a] 2% milk
[b] Non-fat milk
[c] Soy milk
> a
Alright, that's a medium 2% milk latte!
Would you like to order another drink? (y/n)
> n
Okay, so I have:
- medium 2% milk latte
Can I get your name please? 
> John
Thanks, John! Your order will be ready shortly.
```

## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes!

## License
This project is open-source and available under the [MIT License](LICENSE).
```
