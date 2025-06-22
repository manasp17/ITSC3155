
from BankAccount.bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit  # $ per transaction

    def transfer(self, amount, recipient_account):
        if amount > self.transfer_limit:
            print(f"Transfer denied for {self.customer_name}. Amount exceeds transfer limit of ${self.transfer_limit}.")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Transfer denied for {self.customer_name}. Cannot go below minimum balance of ${self.minimum_balance}.")
        else:
            self.current_balance -= amount
            recipient_account.current_balance += amount
            print(f"{self.customer_name} transferred ${amount} to {recipient_account.customer_name}. Remaining balance: ${self.current_balance}")
