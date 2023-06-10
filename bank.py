
class Bank:

  # Define a class attribute for the total loan amount of the bank
    # total_loan = 0
    # total_bank_balance=0


    def __init__(self):
        self.users = []
        self.bank_balance = 0
        self.total_loan=0
        self.loan_feature = True

    def add_user(self, user):
        self.users.append(user)
        self.bank_balance += user.balance

    # def get_user(self, value):
    #     for user in self.users:
    #         if user.account_number == value:
    #             return user
    #     return None
    def get_user(self, value):
        for user in self.users:
            if user.account_number == value:
                from admin import Admin
                if isinstance(user, Admin):
                    return user
                elif not isinstance(user, Admin):
                    return user
        return None

    def create_account(self, account_number, name, balance, is_admin=False):
        if balance < 0:
           print("Failed to create account! The initial balance cannot be negative.")
           return
        if is_admin:
            from admin import Admin
            user = Admin(account_number, name, balance)
        else:
            from user import User
            user = User(account_number, name, balance)
        self.add_user(user)
        print("Account created successfully!")

    def check_bank_balance(self):
        #  total_balance = sum(user.balance for user in self.users if user.balance > 0)
         print(f"Bank Balance: {self.bank_balance}")
      
        # print(f"Bank Balance: {self.bank_balance}")

    def check_total_loan(self):
        # total_loan = sum(user.balance for user in self.users if user.balance > 0)
        print(f"Total Loan Amount: {self.total_loan}")

 
    
    # def toggle_loan_feature(self):
    #     self.loan_feature = not self.loan_feature
    #     status = 'on' if self.loan_feature else 'off'
    #     print(f'Loan feature turned {status}')
