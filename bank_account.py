# Partner: [Write your partner's name here, if any]

class BankAccount:
    # 1. Class attribute: Title of the bank
    bank_title = "Summit National Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        # 2. Instance attributes
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # 3. Method: deposit
    def deposit(self, amount):
        self.current_balance += amount
        print(f"{self.customer_name} deposited ${amount}. New balance: ${self.current_balance}")

    # 3. Method: withdraw with validation (4)
    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f"{self.customer_name} withdrew ${amount}. Remaining balance: ${self.current_balance}")
        else:
            print(f"Withdrawal denied for {self.customer_name}. Cannot go below minimum balance of ${self.minimum_balance}.")

    # 3. Method: print_customer_information including bank title
    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance Requirement: ${self.minimum_balance}")


# 5. Create at least two different instances to make sure it works

# First customer
account1 = BankAccount("Manas Patel", 1500, 300)
account1.print_customer_information()
account1.deposit(200)
account1.withdraw(1000)
account1.withdraw(500)  # Should trigger validation

print("\n")

# Second customer
account2 = BankAccount("Sanjay Patel", 800, 100)
account2.print_customer_information()
account2.deposit(150)
account2.withdraw(700)
account2.withdraw(300)  # Should trigger validation
