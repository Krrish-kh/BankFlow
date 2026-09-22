class AccountValidationError(ValueError):
    """Raised when account input does not satisfy a banking rule."""


def validate_account(account_number, name, age, initial_balance):
    if int(account_number) <= 0:
        raise AccountValidationError("Account number must be positive")
    if not name or not name.strip():
        raise AccountValidationError("Account holder name is required")
    if int(age) < 18:
        raise AccountValidationError("Customer must be at least 18 years old")
    if float(initial_balance) < 0:
        raise AccountValidationError("Initial balance cannot be negative")
    return True
