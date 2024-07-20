class BankAccount:
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

        def deposit(amount): 
              account_balance + amount
        
        def withdraw(amount): 
            if account_balance >= amount:
              account_balance =- amount
              return True
            else: 
                return False
        
        def display_balance(): 
            return f"Current Balance:{account_balance}"
        
