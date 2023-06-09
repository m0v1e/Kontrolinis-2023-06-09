class BankAccount:
    def __init__(self, iban, balance=0):
        self.iban = iban
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f'You deposited {money} eur to your account "{self.iban}"')
        return self.balance

    def withdraw(self, money):
        self.balance -= money
        print(f'You withdraw {money} eur from your account "{self.iban}"')
        return self.balance

    def get_balance(self):
        return print(f'Your "{self.iban}" balance is: {self.balance} eur')

acc1 = BankAccount('LT20 7300 0042 3322 8484')
acc2 = BankAccount('LT38 7044 0000 1234 9876')

acc1.get_balance()
acc1.deposit(200)
acc1.get_balance()
acc1.withdraw(50)
acc1.get_balance()

acc2.get_balance()
acc2.deposit(3500)
acc2.get_balance()
acc2.withdraw(697)
acc2.get_balance()