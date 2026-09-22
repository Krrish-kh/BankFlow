# gdb/command/deposit_command.py
from typing import Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.transaction import Transaction
from gdb.command.transaction_command import TransactionCommand

class DepositCommand(TransactionCommand):
    """Command executing a deposit operation."""

    # ============================================================
    # 📝 STEP 2: Constructor
    #
    # INSTRUCTIONS:
    #   1. Store account in self._account.
    #   2. Store amount (as a float) in self._amount.
    #   3. Set self._transaction = None -- execute() fills it in later.
    # ============================================================
    def __init__(self, account: IAccount, amount: float) -> None:
        self._account = account
        self._amount = float(amount)
        self._transaction: Optional[Transaction] = None

    def execute(self) -> None:
        self._transaction = self._account.deposit_with_transaction(self._amount)

    def get_transaction(self) -> Optional[Transaction]:
        return self._transaction
