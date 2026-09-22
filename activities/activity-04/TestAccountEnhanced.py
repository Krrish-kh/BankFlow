from activity3.AccountEnhanced import Account


class TestAccountEnhanced:
    accounts = []

    @staticmethod
    def display_account(account):
        pin_status = "Yes" if account.hasPin() else "No"
        return (
            f"Account #{account.getAccountNumber()} | "
            f"{account.getName()} ({account.getAge()} yrs) | "
            f"{account.getAccountType()} | "
            f"₹{account.getBalance()} | "
            f"{account.getStatus()} | PIN: {pin_status}"
        )

    @staticmethod
    def add_account(account):
        TestAccountEnhanced.accounts.append(account)
        return account

    @staticmethod
    def main():
        print("=" * 60)
        print("ENHANCED ACCOUNT TEST (BOOLEAN RETURNS)")
        print("=" * 60)
        print()

        print(">>> Test 1: Valid Account Creation")
        account1 = TestAccountEnhanced.add_account(
            Account(1001, "John Doe", 25, 1000.0, "Savings")
        )
        print(TestAccountEnhanced.display_account(account1))

        print(">>> Test 2: Invalid Age (under 18)")
        print("Creating account with age 16")
        account2 = TestAccountEnhanced.add_account(
            Account(1002, "Young Kid", 16, 500.0, "Savings")
        )
        print(f"Age auto-corrected to: {account2.getAge()}")
        print(TestAccountEnhanced.display_account(account2))

        print(">>> Test 3: Invalid Account Type")
        print('Creating account with type "Invalid"')
        account3 = TestAccountEnhanced.add_account(
            Account(1003, "Test User", 25, 500.0, "Invalid")
        )
        print(f"Account type defaulted to: {account3.getAccountType()}")
        print(TestAccountEnhanced.display_account(account3))

        print(">>> Test 4: Minimum Balance Enforcement on Creation")
        print("Creating Savings account with ₹300 (below minimum)")
        account4 = TestAccountEnhanced.add_account(
            Account(1004, "Bob Wilson", 25, 300.0, "Savings")
        )
        print(f"Balance auto-corrected to minimum: ₹{account4.getBalance()}")
        print(TestAccountEnhanced.display_account(account4))

        print(">>> Test 5: Withdrawal with Minimum Balance")
        account5 = TestAccountEnhanced.add_account(
            Account(1005, "Alice Brown", 30, 1200.0, "Current")
        )
        account5.setPin(1234)
        print(f"Initial: {TestAccountEnhanced.display_account(account5)}")
        amount = 200.0
        result = account5.withdraw(amount, 1234)
        print(f"Withdrawing ₹{amount}: {'SUCCESS' if result else 'FAILED (Minimum balance violation)'}")
        print(f"New balance: ₹{account5.getBalance()}")
        print(f"After withdrawal: {TestAccountEnhanced.display_account(account5)}")
        amount = 100.0
        result = account5.withdraw(amount, 1234)
        print(f"Withdrawing ₹{amount} (would leave ₹{account5.getBalance() - amount}): {'SUCCESS' if result else 'FAILED (Minimum balance violation)'}")
        print(f"Current balance: ₹{account5.getBalance()}")

        print(">>> Test 6: Account Status Management")
        account6 = TestAccountEnhanced.add_account(
            Account(1006, "Charlie Green", 35, 2000.0, "Savings")
        )
        print(f"Initial: {TestAccountEnhanced.display_account(account6)}")
        result = account6.closeAccount()
        print(f"Closing account: {'SUCCESS' if result else 'FAILED'}")
        print(f"After close: {TestAccountEnhanced.display_account(account6)}")
        print()
        amount = 500.0
        result = account6.deposit(amount)
        print(f"Depositing ₹{amount} to closed account: {'SUCCESS' if result else 'FAILED (Account inactive)'}")
        result = account6.reopenAccount()
        print(f"Reopening account: {'SUCCESS' if result else 'FAILED'}")
        print(f"After reopen: {TestAccountEnhanced.display_account(account6)}")

        print(">>> Test 7: PIN Protection")
        account7 = TestAccountEnhanced.add_account(
            Account(1007, "Diana Prince", 28, 1500.0, "Savings")
        )
        result = account7.setPin(1234)
        print(f"Setting PIN 1234: {'SUCCESS' if result else 'FAILED'}")
        amount = 200.0
        result = account7.withdraw(amount, 1234)
        print(f"Withdrawing ₹{amount} with correct PIN (1234): {'SUCCESS' if result else 'FAILED'}")
        print(f"New balance: ₹{account7.getBalance()}")
        amount = 100.0
        result = account7.withdraw(amount, 9999)
        print(f"Withdrawing ₹{amount} with incorrect PIN (9999): {'SUCCESS' if result else 'FAILED (Incorrect PIN)'}")
        account_without_pin = Account(1008, "No PIN User", 28, 1000.0, "Savings")
        result = account_without_pin.withdraw(amount, 1234)
        print(f"Withdrawing ₹{amount} with PIN not set: {'SUCCESS' if result else 'FAILED (PIN not set)'}")

        print(">>> Test 8: All Accounts Summary")
        for account in TestAccountEnhanced.accounts:
            print(TestAccountEnhanced.display_account(account))

        print("=" * 60)
        print("ENHANCED TEST COMPLETED!")
        print("=" * 60)


if __name__ == "__main__":
    TestAccountEnhanced.main()
