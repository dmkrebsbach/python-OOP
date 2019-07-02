class User:             # declare a class and give it name User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount) # the specific user's account increases by the amount of the value received
        return self

    def make_withdraw(self, amount): # takes an argument that is the amount of the deposit
        self.account.withdraw(amount) # the specific user's account increases by the amount of the value received
        return self

    def display(self):
        self.account.display_account_info()
        return self


class BankAccount:      # declare a class and give it name Bank Account (a User HAS a bank account, there is an association between the two classes)
    def __init__(self, int_rate=0.01, balance=0):             
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.balance += amount # the specific user's account increases by the amount of the value received
        return self

    def withdraw(self, amount): # takes an argument that is the amount of the withdrawal
        self.balance -= amount  # the specific user's account decreases by the amount of the value received
        return self

    def yield_interest(self):
        self.balance = self.balance * (1.00 + self.int_rate)
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount 
        other_user.balance += amount
        print(self.name, 'transferred $', amount, 'to', other_user.name)
        return self
        return other_user

    def display_account_info(self): # takes an argument that is the amount of the current balance
        print('balance is', self.balance) # the specific user's account is displayed
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
damian = User("Damian Krebsbach", "damian@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdraw(50).display()
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdraw(50).display()