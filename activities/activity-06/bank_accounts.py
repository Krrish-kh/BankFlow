class BankAccount:
    """Common account behavior before the abstract account hierarchy."""

    minimum_balance = 0.0

    def __init__(self, account_number, name, balance):
        self.account_number = int(account_number)
        self.name = name.strip()
        self.balance = float(balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def can_withdraw(self, amount):
        return self.balance - float(amount) >= self.minimum_balance

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0 or not self.can_withdraw(amount):
            return False
        self.balance -= amount
        return True


class SavingsAccount(BankAccount):
    minimum_balance = 500.0


class CurrentAccount(BankAccount):
    minimum_balance = 1000.0
