# gdb/logging/database_log_destination.py
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination
from gdb.db.simulated_database import SimulatedDatabase

class DatabaseLogDestination(LogDestination):
    """Database storage destination implementor backed by SimulatedDatabase."""

    # ============================================================
    # 📝 STEP 3: Implement DatabaseLogDestination
    #
    # INSTRUCTIONS:
    #   1. __init__(db): store the SimulatedDatabase in self._db.
    #   2. write(transaction): insert the transaction into the database.
    #   3. read_all(): return every transaction stored in the database.
    #   4. get_destination_name(): return "Database".
    #
    # HINT: SimulatedDatabase (gdb/db/simulated_database.py) is complete -- read its insert()
    #       and query_all() methods first.
    # ============================================================
    def __init__(self, db: SimulatedDatabase) -> None:
        self._db = db

    def write(self, transaction: Transaction) -> None:
        self._db.insert(transaction)

    def read_all(self) -> List[Transaction]:
        return self._db.query_all()

    def get_destination_name(self) -> str:
        return "Database"
