from activity1.Account import Account


class TestAccount:
    @staticmethod
    def display_account(account):
        print(
            f"Account #{account.getAccountNumber()} | "
            f"{account.getName()} ({account.getAge()} yrs) | "
            f"{account.getAccountType()} | "
            f"₹{account.getBalance()} | "
            f"{account.getStatus()}"
        )

    @staticmethod
    def main():
        print("=" * 50)
        print("GLOBAL DIGITAL BANK - ACCOUNT TEST")
        print("=" * 50)

        print(">>> 1. Creating Account")
        account1 = Account(1001, "John Doe", 25, 1000.0, "Savings")
        print("Account created!")
        TestAccount.display_account(account1)

        print(">>> 2. Deposit Money")
        amount = 500.0
        result = account1.deposit(amount)
        print(f"Depositing ₹{amount}: {'SUCCESS' if result else 'FAILED (Invalid amount)'}")
        print(f"New balance: ₹{account1.getBalance()}")

        amount = -100.0
        result = account1.deposit(amount)
        print(f"Depositing ₹{amount}: {'SUCCESS' if result else 'FAILED (Invalid amount)'}")

        print(">>> 3. Withdraw Money")
        amount = 200.0
        result = account1.withdraw(amount)
        print(f"Withdrawing ₹{amount}: {'SUCCESS' if result else 'FAILED (Insufficient balance)'}")
        print(f"New balance: ₹{account1.getBalance()}")

        amount = 2000.0
        result = account1.withdraw(amount)
        print(f"Withdrawing ₹{amount}: {'SUCCESS' if result else 'FAILED (Insufficient balance)'}")
        print(f"Current balance: ₹{account1.getBalance()}")

        print(">>> 4. Creating Another Account")
        account2 = Account(1002, "Jane Smith", 30, 2000.0, "Current")
        TestAccount.display_account(account2)

        print(">>> 5. All Accounts")
        TestAccount.display_account(account1)
        TestAccount.display_account(account2)

        print("=" * 50)
        print("TEST COMPLETED!")
        print("=" * 50)


if __name__ == "__main__":
    TestAccount.main()
