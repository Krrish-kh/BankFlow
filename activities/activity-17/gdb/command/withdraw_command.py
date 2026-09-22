# gdb/command/withdraw_command.py
from typing import Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.transaction import Transaction
from gdb.command.transaction_command import TransactionCommand

class WithdrawCommand(TransactionCommand):
    """Command executing a withdrawal operation."""

    # ============================================================
    # 📝 STEP 5: Constructor
    #
    # INSTRUCTIONS:
    #   1. Store account in self._account.
    #   2. Store amount (as a float) in self._amount and pin (as an int) in self._pin.
    #   3. Set self._transaction = None -- execute() fills it in later.
    # ============================================================
    def __init__(self, account: IAccount, amount: float, pin: int) -> None:
        self._account = account
        self._amount = float(amount)
        self._pin = int(pin)
        self._transaction: Optional[Transaction] = None

    def execute(self) -> None:
        self._transaction = self._account.withdraw_with_transaction(self._amount, self._pin)

    def get_transaction(self) -> Optional[Transaction]:
        return self._transaction
