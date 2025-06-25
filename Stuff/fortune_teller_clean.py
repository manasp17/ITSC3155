# GOOD FORTUNE TELLER — follows KISS, DRY code, Single Responsibility, and Separation of Concerns

import random

def get_user_name():
    """Prompt for user name."""
    return input("What is your name? ")

def get_user_number():
    """Prompt for number between 1 and 5."""
    while True:
        try:
            number = int(input("Pick a number between 1 and 5: "))
            if 1 <= number <= 5:
                return number
            else:
                print("Number must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

def tell_fortune(name, number):
    """Return a fortune message based on number."""
    fortunes = {
        1: "you will have a great day!",
        2: "something unexpected will happen.",
        3: "today is a good day to start something new.",
        4: "be careful of new opportunities.",
        5: "trust your instincts."
    }
    return f"Hello {name}, {fortunes[number]}"

def main():
    """Main program flow."""
    name = get_user_name()
    number = get_user_number()
    message = tell_fortune(name, number)
    print(message)

if __name__ == "__main__":
    main()
