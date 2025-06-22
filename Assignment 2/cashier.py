# cashier.py

class Cashier:

    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        total = (dollars * 1.00) + (half_dollars * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return round(total, 2)

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. It has been refunded.")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Here is $0.0 in change.")
            return True
