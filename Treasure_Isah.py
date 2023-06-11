class BankAccount:
    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrawal successful. Current balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. Current balance: {self.balance}"


# Create a bank account
account = BankAccount("123456789", "Savings", 1000)

# User input
transaction_type = input("Enter 'w' to withdraw or 'd' to deposit: ")

if transaction_type.lower() == "w":
    amount = float(input("Enter the withdrawal amount: "))
    print(account.withdraw(amount))
elif transaction_type.lower() == "d":
    amount = float(input("Enter the deposit amount: "))
    print(account.deposit(amount))
else:
    print("Invalid transaction type")
