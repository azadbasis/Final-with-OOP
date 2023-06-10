from bank import Bank
from admin import Admin
from user import User


def main():
    bank = Bank()
    # admin = Admin("A001", "Admin User", 0)

    while True:
        print("1. Create User Account")
        print("2. Create Admin Account")
        print("3. Deposit Amount")
        print("4. Withdraw Amount")
        print("5. Transfer Amount")
        print("6. Check Balance")
        print("7. Check Transaction History")
        print("8. Take Loan")
        print("9. Check Total Bank Balance")
        print("10. Check Total Loan Amount")
        print("11. Toggle Loan Feature")
        print("12. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_number = input("Enter account number: ")
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, name, balance)

        elif choice == 2:
            account_number = input("Enter account number: ")
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, name, balance, is_admin=True)

        elif choice == 3:
            account_number = input("Enter account number: ")
            user = bank.get_user(account_number)
            if user:
                amount = float(input("Enter amount to deposit: "))
                user.deposit(amount,bank)
            else:
                print("User not found!")

        elif choice == 4:
            account_number = input("Enter account number: ")
            user = bank.get_user(account_number)
            if user:
                amount = float(input("Enter amount to withdraw: "))
                user.withdraw(amount,bank)
            else:
                print("User not found!")

        elif choice == 5:
            sender_account = input("Enter sender's account number: ")
            recipient_account = input("Enter recipient's account number: ")
            sender = bank.get_user(sender_account)
            recipient = bank.get_user(recipient_account)
            if sender and recipient:
                amount = float(input("Enter amount to transfer: "))
                sender.transfer(amount, recipient)
            else:
                print("User not found!")

        elif choice == 6:
            account_number = input("Enter account number: ")
            user = bank.get_user(account_number)
            if user:
                user.check_balance()
            else:
                print("User not found!")

        elif choice == 7:
            account_number = input("Enter account number: ")
            user = bank.get_user(account_number)
            if user:
                user.check_transaction_history()
            else:
                print("User not found!")

        elif choice == 8:
            account_number = input("Enter account number: ")
            user = bank.get_user(account_number)
            if user:
                amount = float(input("Enter amount to take loan: "))
                user.take_loan(amount,bank)
            else:
                print("User not found!")

        elif choice == 9:
            account_number = input("Enter account number: ")
            admin = bank.get_user(account_number)
            if isinstance(admin, Admin):
                admin.check_total_balance(bank)
            else:
                print("Only admin can check total bank balance!")

        elif choice == 10:
            account_number = input("Enter account number: ")
            admin = bank.get_user(account_number)
            if isinstance(admin, Admin):
              admin.check_total_loan(bank)
            else:
                 print("Only admin can check total loan!")

        elif choice == 11:
            account_number = input("Enter account number: ")
            admin = bank.get_user(account_number)
            if isinstance(admin, Admin):
             admin.toggle_loan_feature(bank)
            else:
                print("Only admin can check toggle loan feature!") 

        elif choice == 12:
            print("Exiting...")
            break

        print("\n")

if __name__ == "__main__":
    main()
