class User:		# declare a class and give it name User
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount # the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount): # takes an argument that is the amount of the withdrawal
        self.account_balance -= amount  # the specific user's account decreases by the amount of the value received

    def display_user_balance(self): # takes an argument that is the amount of the current balance
        print('User:',self.name, 'has a balance of', self.account_balance) # the specific user's account is displayed

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount 
        other_user.account_balance += amount
        print(self.name, 'transferred $', amount, 'to', other_user.name)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
damian = User("Damian Krebsbach", "damian@python.com")

                #  Have the first user make 3 deposits and 1 withdrawal and then display their balance
                #  Have the second user make 2 deposits and 2 withdrawals and then display their balance
                #  Have the third user make 1 deposits and 3 withdrawals and then display their balance
                #  BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

guido.make_deposit(10000)
guido.make_deposit(5000)
guido.make_deposit(555)
guido.make_withdrawal(10000)
guido.display_user_balance()

monty.make_deposit(50000)
monty.make_deposit(25000)
monty.make_withdrawal(10000)
monty.make_withdrawal(20000)
monty.display_user_balance()

damian.make_deposit(25000)
damian.make_withdrawal(1000)
damian.make_withdrawal(20000)
damian.make_withdrawal(1000)
damian.display_user_balance()

monty.display_user_balance()
damian.display_user_balance()
damian.transfer_money(monty,10000)
monty.display_user_balance()
damian.display_user_balance()