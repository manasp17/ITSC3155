# main.py
# Manas Patel
# GitHub Repo: https://github.com/manasp17/sandwich-machine

import data
import sandwich_maker
import cashier

def main():

    maker = sandwich_maker.SandwichMaker(data.resources)
    cashier_obj = cashier.Cashier()

    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            break
        elif choice == "report":
            maker.report()
        elif choice in data.recipes:
            sandwich = data.recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if maker.check_resources(ingredients):
                payment = cashier_obj.process_coins()
                if cashier_obj.transaction_result(payment, cost):
                    maker.make_sandwich(choice, ingredients)

        else:
            print("Invalid input. Please choose from small, medium, large, report, or off.")

if __name__ == "__main__":
    main()
