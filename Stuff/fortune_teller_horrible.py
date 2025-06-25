# BAD FORTUNE TELLER — Violates KISS, DRY code, Single Responsibility, and Separation of Concerns

import random

name = input("What is your name? ")
number = int(input("Pick a number between 1 and 5: "))

if number == 1:
    print("Hello " + name + ", you will have a great day!")
elif number == 2:
    print("Hello " + name + ", something unexpected will happen.")
elif number == 3:
    print("Hello " + name + ", today is a good day to start something new.")
elif number == 4:
    print("Hello " + name + ", be careful of new opportunities.")
elif number == 5:
    print("Hello " + name + ", trust your instincts.")
else:
    print("Invalid number!")

# No functions, no separation, repeated print logic
