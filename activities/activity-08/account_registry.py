class AccountRegistry:
    """Small in-memory registry used before introducing the account factory."""

    def __init__(self):
        self._accounts = {}

    def add(self, account):
        account_number = int(account.account_number)
        if account_number in self._accounts:
            raise ValueError(f"Account {account_number} already exists")
        self._accounts[account_number] = account
        return account

    def get(self, account_number):
        return self._accounts.get(int(account_number))

    def remove(self, account_number):
        return self._accounts.pop(int(account_number), None)

    def all_accounts(self):
        return list(self._accounts.values())
