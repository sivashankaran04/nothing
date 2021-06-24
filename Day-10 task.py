class BankAccount:
    def __init__(self):
        self.balance = 0
        print("\nWelcome to the Deposit & Withdrawal Machine")

    def display(self):
        print("\nNet Available Balance = ", self.balance)


class Deposit(BankAccount):
    def deposit(self):
        amount = float(input("Enter amount to be Deposited : "))
        self.balance += amount
        print("\nAmount Deposited : ", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn : "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew : ", amount)
        else:
            print("\nInsufficient balance !!")


s = p = Deposit()
p.deposit()
s.withdraw()
s.display()
