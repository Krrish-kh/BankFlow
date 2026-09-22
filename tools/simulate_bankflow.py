"""Run small, deterministic BankFlow demonstrations for the learning agent."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ACTIVITY_ROOT = Path(__file__).resolve().parents[1] / "activities" / "activity-18"
sys.path.insert(0, str(ACTIVITY_ROOT))

from gdb.command.deposit_command import DepositCommand  # noqa: E402
from gdb.command.transfer_command import TransferCommand  # noqa: E402
from gdb.domain.account_factory import AccountFactory  # noqa: E402
from gdb.logging.memory_log_destination import MemoryLogDestination  # noqa: E402
from gdb.logging.transaction_logger import TransactionLogger  # noqa: E402
from gdb.service.transfer_service import TransferService  # noqa: E402


def create_accounts():
    sender = AccountFactory.create_account(
        "SAVINGS", 1001, "Rajesh Sharma", 30, 100000.0, 0
    )
    receiver = AccountFactory.create_account(
        "CURRENT", 1002, "Priya Patel", 28, 50000.0, 0
    )
    sender.set_pin(1234)
    receiver.set_pin(5678)
    return sender, receiver


def run_transfer():
    sender, receiver = create_accounts()
    service = TransferService()
    logger = TransactionLogger(MemoryLogDestination())
    command = TransferCommand(service, sender, receiver, 5000.0, 1234)

    print("Scenario: transfer Rs. 5,000 from Savings #1001 to Current #1002")
    print(f"Before: sender=Rs. {sender.get_balance():,.2f}, receiver=Rs. {receiver.get_balance():,.2f}")
    command.execute()
    logger.log(command.get_transaction())
    print(f"After:  sender=Rs. {sender.get_balance():,.2f}, receiver=Rs. {receiver.get_balance():,.2f}")
    print(f"Audit records: {len(logger.get_transactions())}")
    print(logger.get_transactions()[0].get_receipt())


def run_audit():
    account, _ = create_accounts()
    logger = TransactionLogger(MemoryLogDestination())
    command = DepositCommand(account, 2500.0)

    print("Scenario: deposit Rs. 2,500 and create an audit record")
    command.execute()
    logger.log(command.get_transaction())
    print(f"Balance: Rs. {account.get_balance():,.2f}")
    print(logger.get_transactions()[0].get_receipt())


def main():
    parser = argparse.ArgumentParser(description="Run BankFlow learning simulations")
    parser.add_argument(
        "scenario",
        choices=("transfer", "audit"),
        nargs="?",
        default="transfer",
        help="simulation to run",
    )
    args = parser.parse_args()

    if args.scenario == "audit":
        run_audit()
    else:
        run_transfer()


if __name__ == "__main__":
    main()
