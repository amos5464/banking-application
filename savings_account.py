from account import Account


class SavingsAccount(Account):
    WITHDRAWAL_LIMIT = 1000000  # 1 million withdrawal limit

    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        """ This was done by Victor where he made the withdrawal limit and made sure the money will be withdrwan with three checks:
        1. Amount must be positive
        2. Amount can't exceed withdrawal limit
        3. Amount can't exceed balance"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.WITHDRAWAL_LIMIT:
            raise ValueError(f"Withdrawal amount exceeds limit of {self.WITHDRAWAL_LIMIT}")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        return True

    def deposit(self, amount):
        """This was done by Damian Daniel"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

        return True
