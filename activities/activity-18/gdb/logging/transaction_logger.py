# gdb/logging/transaction_logger.py
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination

class TransactionLogger:
    """Bridge Abstraction: delegates logging operations to LogDestination implementor."""

    # ============================================================
    # 📝 STEP 4: Implement Bridge Constructor & Methods
    #
    # INSTRUCTIONS:
    #   1. __init__: store destination (a LogDestination) in self._destination.
    #   2. log(transaction): if transaction is not None, call self._destination.write(transaction).
    #   3. get_transactions(): return self._destination.read_all().
    #   4. get_destination(): return the current destination.
    #   5. set_destination(destination): replace self._destination -- this is how the backend is switched at runtime.
    # ============================================================
    def __init__(self, destination: LogDestination) -> None:
        self._destination = destination

    def log(self, transaction: Transaction) -> None:
        if transaction is not None:
            self._destination.write(transaction)

    def get_transactions(self) -> List[Transaction]:
        return self._destination.read_all()

    def get_destination(self) -> LogDestination:
        return self._destination

    def set_destination(self, destination: LogDestination) -> None:
        self._destination = destination
