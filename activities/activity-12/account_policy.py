from dataclasses import dataclass


@dataclass(frozen=True)
class AccountPolicy:
    minimum_balance: float
    interest_rate: float
    overdraft_limit: float = 0.0

    def allows_withdrawal(self, balance, amount):
        remaining = float(balance) - float(amount)
        floor = self.minimum_balance - self.overdraft_limit
        return remaining >= floor


DEFAULT_POLICIES = {
    "SAVINGS": AccountPolicy(1000.0, 4.0),
    "CURRENT": AccountPolicy(0.0, 0.0, 10000.0),
    "FIXEDDEPOSIT": AccountPolicy(50000.0, 6.5),
    "SALARY": AccountPolicy(0.0, 3.5),
}


def get_policy(account_type):
    key = str(account_type).upper().replace(" ", "").replace("_", "")
    return DEFAULT_POLICIES.get(key, AccountPolicy(0.0, 0.0))
