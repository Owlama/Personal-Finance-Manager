class ATM:
    def __init__(self):
        self.balance = 0.0

    def check_balance(self):
        print("Your current balance is: $", self.balance)

    def withdraw_money(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful. Please take your cash.")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def deposit_money(self):
        amount = float(input("Enter the amount to deposit: $"))
        self.balance += amount
        print("Deposit successful. Current balance: $", self.balance)

    def run(self):
        print("Welcome to the ATM!")

        while True:
            print("\n1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw_money()
            elif choice == "3":
                self.deposit_money()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


atm = ATM()
atm.run()
