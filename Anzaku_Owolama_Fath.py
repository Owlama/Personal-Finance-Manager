account_type = input("Enter account type (savings or current): ")

transaction_type = input("Enter transaction type (withdrawal or deposit): ")

if account_type == "savings":
    old_balance = 50000  # Example initial balance for savings account
    # Step 4: Get the amount for withdrawal or deposit
    amount = float(input("Enter the amount: "))

    if transaction_type == "withdrawal":
        if amount <= old_balance:
            new_balance = old_balance - amount
            print("Success, new balance is $" + str(new_balance))
        else:
            print("Failed, transaction failed.")
    elif transaction_type == "deposit":
        new_balance = old_balance + amount
        print("Success, new balance is $" + str(new_balance))
    else:
        print("Invalid transaction type.")
elif account_type == "current":
    old_balance = 100000  # Example initial balance for current account
    if transaction_type == "withdrawal":
        amount = float(input("Enter the amount: "))
        if amount <= old_balance:
            new_balance = old_balance - amount
            print("Success, new balance is $" + str(new_balance))
        else:
            print("Failed, transaction failed.")
    elif transaction_type == "deposit":
        new_balance = old_balance + amount
        print("Success, new balance is $" + str(new_balance))
    else:
        print("Invalid transaction type.")
else:
    print("Invalid account type.")
