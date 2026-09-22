# BankFlow Core Banking Platform

**A modular core banking platform for account management, policy-driven money movement, and transaction auditability.**

I built BankFlow as a practical banking core that grows from account fundamentals into a layered system for secure transfers, configurable rules, transaction records, command workflows, and interchangeable logging backends.

## What I Built

- Account lifecycle management, deposits, withdrawals, PIN protection, and status controls
- Savings, current, fixed-deposit, and salary account products
- Centralized rules for balances, interest, overdrafts, tenure, and transfer limits
- External `.properties` configuration for operational thresholds
- Daily transfer limits based on account type and customer tenure
- Structured transaction records, unique identifiers, and formatted receipts
- Command objects for deposit, withdrawal, and transfer operations
- File, memory, and simulated database logging destinations
- Runtime switching between logging backends through a common destination contract

## How the System Fits Together

```text
Account products
      |
Rules engine <---- external configuration
      |
Transfer service
      |
Transaction records
      |
Commands ---- logging destinations
```

I keep `main` as the cumulative release line. Each activity branch records one focused capability and can be reviewed independently before it is carried forward.

## Repository Layout

```text
activities/
  activity-01/ ... activity-18/   capability snapshots
.github/agents/                   VS Code learning agent
 docs/                            architecture and operating notes
tools/                            local simulation runners
README.md                         project overview
```

The later activities use a self-contained `gdb` package with configuration and tests. The earlier activities retain their original lightweight structure so the progression remains visible.

## Quick Start

I use Python 3.10 or newer and the standard library for the core implementation.

```powershell
git clone https://github.com/Krrish-kh/BankFlow.git
Set-Location .\BankFlow\activities\activity-18
python -m gdb.tests.test_bridge_logging -v
```

To run the main operational checks:

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

## Try a Simulation

I included a small simulator that uses the final activity implementation and prints observable balances and audit records:

```powershell
Set-Location .\BankFlow
python tools\simulate_bankflow.py transfer
python tools\simulate_bankflow.py audit
```

The **BankFlow Simulator** custom agent can run these scenarios on request and explain the source path as an interactive lesson. Its definition is in `.github/agents/bankflow-simulator.agent.md`.

## Development Path

| Stage | What I added |
| --- | --- |
| Foundation | Account state, validation, lifecycle, and product behavior |
| Policy | Interest, overdraft, account policy, rules, and external configuration |
| Operations | Factories, transfers, tenure tiers, and daily limits |
| Audit | Transactions, receipts, commands, persistence, and logging destinations |

The detailed activity map is in [docs/activity-roadmap.md](docs/activity-roadmap.md). The system boundaries and extension points are in [docs/architecture.md](docs/architecture.md). Setup and contribution notes are in [docs/getting-started.md](docs/getting-started.md).

## Branch Naming

I use `activity-XX-feature-name`, for example:

```text
activity-15-funds-transfer
activity-16-transaction-model
activity-17-command-file-logging
activity-18-bridge-logging
```

## License

No license has been declared for this repository yet.
