# Base class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: UGX {amount}")

    def withdraw(self, amount):
        pass

    def display_balance(self):
        print(f"Account Balance: UGX {self.balance}")


# Savings Account
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: UGX {amount}")
        else:
            print("Insufficient funds in Savings Account.")


# Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn: UGX {amount}")
        else:
            print("Overdraft limit exceeded.")


# Creating accounts
savings = SavingsAccount("SA101", 500000)
current = CurrentAccount("CA201", 300000, 200000)

# Savings Account Transactions
print("Savings Account")
savings.deposit(100000)
savings.withdraw(200000)
savings.display_balance()

print()

# Current Account Transactions
print("Current Account")
current.deposit(50000)
current.withdraw(450000)
current.display_balance()