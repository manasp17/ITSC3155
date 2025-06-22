
from savings_account import SavingsAccount
from BankAccount.checking_account import CheckingAccount

savings1 = SavingsAccount("Manas Patel", 2000, 500, "SA123", "111000", 0.03)
savings1.print_customer_information()
savings1.deposit(500)
savings1.apply_interest()
print("\n")

checking1 = CheckingAccount("Sanjay Patel", 1500, 200, "CA456", "222000", 700)
checking2 = CheckingAccount("Priya Sharma", 1000, 200, "CA789", "222000", 700)

checking1.print_customer_information()
checking2.print_customer_information()

checking1.transfer(600, checking2)  # Successful transfer
checking1.transfer(800, checking2)  # Should trigger transfer limit
print("\n")

savings2 = SavingsAccount("Arjun Mehta", 3000, 1000, "SA999", "111111", 0.04)
savings2.print_customer_information()
savings2.apply_interest()
print("\n")


checking3 = CheckingAccount("Arjun Mehta", 2500, 300, "CA333", "222222", 1000)
checking3.print_customer_information()
checking3.transfer(900, checking2)
