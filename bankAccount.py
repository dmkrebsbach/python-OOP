class BankAccount:
    def __init__(self, acct_name='Acctx', int_rate=0.01, balance=0):             
        self.acct_name = acct_name
        self.int_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount # the specific user's account increases by the amount of the value received
        return self # your code here         
    
    def withdraw(self, amount): # takes an argument that is the amount of the withdrawal
        self.account_balance -= amount # the specific user's account decreases by the amount of the value received
        return self # allows for chaining methods
    
    def yield_interest(self):
        self.account_balance = self.account_balance * (1.00 + self.int_rate)
        return self

    def display_account_info(self): # takes an argument that is the amount of the current balance
        print('Acct Name',self.acct_name, 'has a balance of', self.account_balance) # the specific user's account is displayed
        return self



acct1 = BankAccount('acct1', 0.05, 50000)
acct2 = BankAccount('acct2', 0.03, 0)

acct1.deposit(500).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()
acct2.deposit(5000).deposit(5000).withdraw(1000).withdraw(500).withdraw(200).withdraw(1750).yield_interest().display_account_info()
