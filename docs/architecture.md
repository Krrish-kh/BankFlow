# Architecture

## Purpose

Aurelia Ledger is structured as a small banking core with clear boundaries between account state, policy, operations, audit records, and storage.

## Core Layers

### Account Domain

Account classes own balances, lifecycle state, PIN verification, product rules, and account-specific behavior. Concrete products share the common account contract while defining their own minimum balance and interest behavior.

### Policy

`AccountRulesEngine` centralizes business decisions such as minimum balances, interest rates, overdrafts, and tenure-based transfer limits. External properties files keep adjustable thresholds outside the domain classes.

### Operations

`TransferService` coordinates a complete funds transfer. It validates both accounts, verifies the sender, checks product and daily limits, then performs debit, credit, and audit-total updates in a controlled order.

### Audit

`Transaction` is an immutable-style record of a completed money movement. Commands wrap deposits, withdrawals, and transfers so callers can execute an operation and retrieve its audit record through one interface.

### Logging

The logging abstraction delegates persistence to a destination interface. File, memory, and simulated database destinations can be selected at runtime without changing the logger or command classes.

## Extension Points

- Add an account product by implementing the account contract and registering it with `AccountFactory`.
- Add a policy by extending the properties files and rules-engine lookup.
- Add a command by implementing `TransactionCommand`.
- Add a storage backend by implementing `LogDestination`.
- Add a transaction type by extending `TransactionType` and constructing the corresponding record.

## Reliability Principles

- Validate before changing balances.
- Keep policy decisions centralized.
- Record successful operations only after money movement completes.
- Keep storage details behind interfaces.
- Preserve earlier activity behavior as later capabilities are introduced.
