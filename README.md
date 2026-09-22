# BankFlow Core Banking Platform

BankFlow is a modular core banking platform for account management, policy-driven money movement, and transaction auditability.

## Start Here

For setup and the first working simulation, open the [Getting Started guide](https://github.com/Krrish-kh/BankFlow/wiki/Getting-Started).

```powershell
git clone https://github.com/Krrish-kh/BankFlow.git
Set-Location .\BankFlow
python tools\simulate_bankflow.py transfer
```

## What BankFlow Covers

- Account products, lifecycle management, deposits, withdrawals, and PIN protection
- Centralized and externally configured account rules
- Secure transfers with tenure-based daily limits
- Structured transaction records and receipts
- Command-based operations and pluggable logging destinations
- File, memory, and simulated database logging
- A VS Code learning agent for interactive simulations

## Documentation

The detailed project documentation is maintained in the [BankFlow Wiki](https://github.com/Krrish-kh/BankFlow/wiki):

- [Getting Started](https://github.com/Krrish-kh/BankFlow/wiki/Getting-Started)
- [Architecture](https://github.com/Krrish-kh/BankFlow/wiki/Architecture)
- [Activity Roadmap](https://github.com/Krrish-kh/BankFlow/wiki/Activity-Roadmap)

The same documentation is versioned in the repository under [`docs/`](docs/).

## Repository

- `main` contains the cumulative implementation.
- `activities/activity-01` through `activities/activity-18` contain progressive capability snapshots.
- `.github/agents/bankflow-simulator.agent.md` defines the interactive VS Code learning agent.

## Verification

```powershell
Set-Location .\activities\activity-18
python -m gdb.tests.test_bridge_logging -v
```
