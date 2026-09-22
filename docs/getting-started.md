# Getting Started

This guide is how I set up and verify BankFlow locally.

**Wiki version:** [BankFlow Getting Started](https://github.com/Krrish-kh/BankFlow/wiki/Getting-Started)

## Requirements

- Python 3.10 or newer
- Git
- PowerShell, Command Prompt, or a Unix-compatible shell

The core implementation uses the Python standard library. No external package installation is required for the activity test suites.

## Clone the Repository

```powershell
git clone https://github.com/Krrish-kh/BankFlow.git
Set-Location .\BankFlow
```

## Run the Latest Activity

The final activity contains the complete command and bridge-logging implementation:

```powershell
Set-Location .\activities\activity-18
python -m gdb.tests.test_bridge_logging -v
```

## Run the Main Verification Sequence

```powershell
Set-Location ..\activity-15
python -m gdb.tests.test_transfer -v
Set-Location ..\activity-16
python -m gdb.tests.test_transaction_model -v
Set-Location ..\activity-17
python -m gdb.tests.test_command_logging -v
Set-Location ..\activity-18
python -m gdb.tests.test_bridge_logging -v
```

## Run a Simulation

From the repository root:

```powershell
python tools\simulate_bankflow.py transfer
python tools\simulate_bankflow.py audit
```

The simulator uses the activity-18 implementation and prints the balance changes and transaction receipts that I expect from each scenario.

## Inspect an Activity Branch

```powershell
git fetch origin
git switch activity-18-bridge-logging
python -m gdb.tests.test_bridge_logging -v
git switch main
```

Activity branches are cumulative snapshots. When I add a new feature, I keep the existing activity folder layout and use a descriptive branch name.

## Configuration

Activities 14-18 load business rules from `config/rules/*.properties`. I keep configuration changes with the activity that owns the behavior and verify them through the corresponding tests.
