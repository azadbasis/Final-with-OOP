
from bank import Bank
class User:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transaction_history = []
        self.bank=Bank()
       

    #  deposit  amount
    def deposit(self, amount,bank):
        if amount>0:
            self.balance += amount
            bank.bank_balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print("Amount deposited successfully!")
        else:
            print("Failed to deposit!!\nThe amount must be positive!")    
        

    def withdraw(self, amount, bank):

        if amount < 0:
            print("Invalid withdrawal amount. Amount must be positive.")
            return
        if amount > self.balance:
            print(f'Insufficient funds in {self.name} account')
            return
        if amount > bank.bank_balance:
            print('Bank is bankrupt')
            return
        self.balance -= amount
        bank.bank_balance -= amount
        self.transaction_history.append(f'Withdrew {amount}')
        print(f'{amount} withdrawn from {self.name} account')     

              
    #  transfer the amount from his account to another user account.
    def transfer(self, amount, recipient):
        if amount < 0:
            print("Invalid transfer amount. Amount must be positive.")
            return
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
          
        else:
            print("Insufficient balance!")

    #  check available balance.
    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

    #  check transaction history.
    def check_transaction_history(self):
        if len(self.transaction_history)== 0:
                print("There is no transaction!!")
        else:        
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)



    def take_loan(self, amount, bank):

        if amount < 0:
            print("Invalid loan amount. Amount must be positive.")
            return
        
        if not bank.loan_feature:
            print('Loan feature is currently turned off')
            return
        
        if amount > 2 * self.balance:
            print(f'Loan amount exceeds twice the balance of {self.name} account')
            return
        
        self.balance += amount
        bank.bank_balance -= amount
        bank.total_loan += amount
        self.transaction_history.append(f'Took loan of {amount}')
        print(f'{self.name} took loan of {amount} from bank')     