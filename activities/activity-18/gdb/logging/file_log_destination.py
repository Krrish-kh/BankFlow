# gdb/logging/file_log_destination.py
import pickle
import os
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination

class FileLogDestination(LogDestination):
    """File storage destination implementor using pickle serialization."""

    # ============================================================
    # 📝 STEP 2: Implement FileLogDestination
    #
    # INSTRUCTIONS:
    #   1. __init__: store filename in self._filename.
    #   2. write(transaction): load the existing list with self.read_all(), append the transaction,
    #      then pickle.dump() the whole list back to the file (open it in mode "wb").
    #   3. read_all(): if the file exists, pickle.load() the list from it (mode "rb") and return it;
    #      return [] if the file is missing or cannot be read.
    #   4. clear(): delete the file if it exists (ignore an OSError if the delete fails).
    # ============================================================
    def __init__(self, filename: str = "transactions.log") -> None:
        self._filename = filename

    def write(self, transaction: Transaction) -> None:
        records = self.read_all()
        records.append(transaction)
        with open(self._filename, "wb") as file:
            pickle.dump(records, file)

    def read_all(self) -> List[Transaction]:
        if not os.path.exists(self._filename):
            return []

        try:
            with open(self._filename, "rb") as file:
                data = pickle.load(file)
            if isinstance(data, list):
                return data
        except (OSError, EOFError, pickle.PickleError):
            pass

        return []

    def get_destination_name(self) -> str:
        return f"File: {self._filename}"

    def clear(self) -> None:
        try:
            if os.path.exists(self._filename):
                os.remove(self._filename)
        except OSError:
            pass
