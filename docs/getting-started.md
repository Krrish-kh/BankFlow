# Getting Started

## Requirements

- Python 3.10 or newer
- Git
- PowerShell, Command Prompt, or a Unix-compatible shell

The project uses the Python standard library for its core implementation and tests.

## Clone

```powershell
git clone https://github.com/Krrish-kh/BankFlow.git
Set-Location .\BankFlow
```

## Run an Activity

Each later activity is self-contained. Change into the activity directory before running its module tests:

```powershell
Set-Location .\activities\activity-18
python -m gdb.tests.test_bridge_logging -v
```

The most complete operational verification sequence is:

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

## Work With a Feature Branch

```powershell
git fetch origin
git switch activity-18-bridge-logging
python -m gdb.tests.test_bridge_logging -v
git switch main
```

Activity branches are cumulative snapshots. New work should use a descriptive branch name and should preserve the existing activity folder layout.

## Configuration

Activities 14-18 load account rules from `config/rules/*.properties`. Keep configuration changes localized to the activity that owns the behavior and validate them with the corresponding tests.
