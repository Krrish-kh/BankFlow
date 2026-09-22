# gdb/logging/transaction_log.py
import pickle
import os
from typing import List
from gdb.domain.transaction import Transaction

class TransactionLog:
    """File persistence logger for Transaction records using pickle serialization."""

    # ============================================================
    # 📝 STEP 11: Constructor & Fields
    #
    # INSTRUCTIONS:
    #   1. Store log_file (the path of the pickle file) in self._log_file.
    #   2. Start with an empty list in self._transactions.
    # ============================================================
    def __init__(self, log_file: str = "transactions.log") -> None:
        self._log_file = log_file
        self._transactions: List[Transaction] = []

    def log_transaction(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)
        self.save_to_file()

    def save_to_file(self) -> None:
        with open(self._log_file, "wb") as file:
            pickle.dump(self._transactions, file)

    def load_from_file(self) -> List[Transaction]:
        if not os.path.exists(self._log_file):
            self._transactions = []
            return list(self._transactions)

        try:
            with open(self._log_file, "rb") as file:
                self._transactions = pickle.load(file)
        except (OSError, EOFError, pickle.PickleError):
            self._transactions = []

        return list(self._transactions)

    def get_transactions(self) -> List[Transaction]:
        return self._transactions

    def clear(self) -> None:
        self._transactions = []
        try:
            if os.path.exists(self._log_file):
                os.remove(self._log_file)
        except OSError:
            pass
