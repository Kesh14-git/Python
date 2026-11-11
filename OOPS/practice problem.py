def create_account():
    acc_no = input("Enter Account number:")
    if acc_no in accounts:
        print("Account already exists!")
    else:
        name = input("Enter Account Holder Name:")
        balance = float(input("Enter Initial Deposit:"))

        accounts[acc_no] = {
            "name":name,
            "balance": balance
        }

        print("Account created successfully!")

def check_balance():
    acc_no = input("Enter Account Number:")
    if acc_no in accounts:
        print("Account Holder:",accounts[acc_no]["name"])
        print("Balance:",accounts[acc_no]["balance"])
    else:
        print("Account not found!")

def deposit():
    acc_no = input("Enter Account Number:")
    if acc_no in accounts:
        amount = float(input("Enter Deposit Amount:"))

        if amount > 0:
            accounts[acc_no]["balance"] += amount
            print("Amount deposited successfully!")
            print("Updated Balnce:",accounts[acc_no]["balance"])
        else:
            print("Account not found!")

def withdraw():
    acc_no = input("Enter Account Number:")
    if acc_no in accounts:
        amount = float(input("Enter Withdrawal Amount:"))

        if amount <=0:
            print("Invalid amount!")
        elif amount > accounts[acc_no]["balance"]:
            print("Insufficient balance!")
        else:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found!")

def banking_system():
    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()

        elif choice == 2:
            check_balance()

        elif choice == 3:
            deposit()

        elif choice == 4:
            withdraw()

        elif choice == 5:
            print("Thank you for using our Banking System!")
            break

        else:
            print("Invalid choice!")


banking_system()





         


