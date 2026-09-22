from dataclasses import dataclass


@dataclass(frozen=True)
class InterestPolicy:
    annual_rate: float

    def calculate(self, balance, years=1):
        return float(balance) * self.annual_rate / 100.0 * int(years)


POLICIES = {
    "SAVINGS": InterestPolicy(4.0),
    "CURRENT": InterestPolicy(0.0),
    "FIXEDDEPOSIT": InterestPolicy(6.5),
}


def calculate_interest(account_type, balance, years=1):
    policy = POLICIES.get(str(account_type).upper().replace(" ", "").replace("_", ""))
    if policy is None:
        return 0.0
    return policy.calculate(balance, years)
