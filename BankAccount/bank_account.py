
class BankAccount:
    bank_title = "Summit National Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member

    def deposit(self, amount):
        self.current_balance += amount
        print(f"{self.customer_name} deposited ${amount}. New balance: ${self.current_balance}")

    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f"{self.customer_name} withdrew ${amount}. Remaining balance: ${self.current_balance}")
        else:
            print(f"Withdrawal denied for {self.customer_name}. Cannot go below minimum balance of ${self.minimum_balance}.")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance Requirement: ${self.minimum_balance}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.__routing_number}")
