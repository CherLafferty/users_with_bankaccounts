class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
    # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Chargin a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance) > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = BankAccount(0.02, 10)
checking = BankAccount(0.04, 1000)

class User:
    #constructor
    #instance method
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.account = BankAccount(int_rate=0.01, balance=0)
    #method
    def make_deposit(self, amount):
        self.account.deposit += amount

    def make_withdrawl(self, amount):
        self.account.withdraw -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


cher = User("Cher")
nibbles = User("Mr. Nibbles")
benny_bob = User("Benny Bob")


# savings.deposit(100).deposit(200).deposit(200).withdraw(150).yield_interest().display_account_info()
# checking.deposit(1000).deposit(2000).withdraw(100).withdraw(200).withdraw(100).withdraw(100).yield_interest().display_account_info()
# BankAccount.print_all_accounts()