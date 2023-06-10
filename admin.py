
from user import User

class Admin(User):
  
    def __init__(self, account_number, name, balance):
     super().__init__(account_number, name, balance)


# check the total available balance of the bank.
    def check_total_balance(self,bank):
        bank.check_bank_balance()

# check the total loan amount.
    def check_total_loan(self,bank):
        bank.check_total_loan()

 # on or off the loan feature of the bank.  
    def toggle_loan_feature(self, bank):
        bank.loan_feature = not bank.loan_feature
        status = 'on' if bank.loan_feature else 'off'
        print(f'Loan feature turned {status} by {self.name}')

