from account import Account

class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return super().withdraw(amount)
    "Godwin created the withdrawal"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return True
    "Damian created the deposit"