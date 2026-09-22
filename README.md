# Aurelia Ledger

**A modular banking platform for reliable account operations, policy-driven money movement, and auditable transaction workflows.**

Aurelia Ledger models the evolution of a financial services core from a simple account ledger into a structured platform with account products, configurable policy, secure transfers, transaction records, command-based operations, and pluggable logging destinations.

## Product Capabilities

- Account lifecycle management with deposits, withdrawals, PIN protection, and status controls
- Savings, current, fixed-deposit, and salary account products
- Centralized policy evaluation for balances, interest, overdrafts, and transfer limits
- External `.properties` configuration for operational rules
- Daily transfer limits based on account type and customer tenure
- Structured transaction records with formatted receipts and unique identifiers
- Command objects for deposit, withdrawal, and transfer workflows
- File, in-memory, and simulated database logging destinations
- Runtime switching between logging backends through a bridge abstraction

## Architecture

The implementation is organized as a progressive set of compatible capability layers:

```text
Account products
	|
Policy and rules engine ---- external configuration
	|
Transfer service
	|
Transaction model
	|
Command workflows ---- logging destinations
```

The `main` branch is the cumulative release line. Activity branches are feature snapshots that can be reviewed independently and merged forward without replacing later capabilities.

## Repository Layout

```text
activities/
  activity-01/ ... activity-18/   progressive capability snapshots
docs/                             architecture and operating notes
README.md                         project overview
```

Each activity folder is self-contained. The later activities use the `gdb` package structure and include their own configuration and tests.

## Getting Started

Python 3.10 or newer is recommended. Clone the repository and run a capability-specific test suite from its activity directory:

```powershell
git clone https://github.com/Krrish-kh/BANKING_SYSTEM.git
Set-Location .\BANKING_SYSTEM\activities\activity-18
python -m gdb.tests.test_bridge_logging -v
```

Useful verification commands:

```powershell
Set-Location .\activities\activity-15
python -m gdb.tests.test_transfer -v

Set-Location ..\activity-16
python -m gdb.tests.test_transaction_model -v

Set-Location ..\activity-17
python -m gdb.tests.test_command_logging -v

Set-Location ..\activity-18
python -m gdb.tests.test_bridge_logging -v
```

## Release Roadmap

| Phase | Capabilities |
| --- | --- |
| Foundation | Account state, validation, lifecycle, and product behavior |
| Policy | Interest, overdraft, account policy, rules engine, and external configuration |
| Operations | Account factory, transfers, tenure tiers, and daily limits |
| Audit | Transactions, receipts, commands, persistence, and logging destinations |

The complete activity-to-feature map is available in [docs/activity-roadmap.md](docs/activity-roadmap.md). System boundaries and extension points are described in [docs/architecture.md](docs/architecture.md).

## Branch Convention

Branches follow `activity-XX-feature-name`, for example:

```text
activity-15-funds-transfer
activity-16-transaction-model
activity-17-command-file-logging
activity-18-bridge-logging
```

## License

No license has been declared for this repository yet.
