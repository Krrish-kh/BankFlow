# Architecture Notes

## My Design Goal

I designed BankFlow around one principle: money movement should be easy to follow, difficult to misuse, and straightforward to audit. For that reason, I keep account state, policy decisions, operations, transaction records, and storage concerns separate.

## Account Domain

The account classes own balances, lifecycle state, PIN verification, and product-specific behavior. Savings, current, fixed-deposit, and salary accounts share the common account contract while retaining their own rules.

## Policy Layer

I keep business decisions in `AccountRulesEngine`. It provides minimum balances, interest rates, overdraft limits, and tenure-based transfer limits. Activities 14-18 load adjustable thresholds from `config/rules/*.properties`, so changing a policy value does not require rewriting account classes.

## Operations Layer

`TransferService` coordinates a complete transfer. It checks both accounts, verifies the sender PIN, protects product minimum balances, applies the daily limit, and only then performs the debit and credit. The sender's daily total is updated after the money movement succeeds.

## Audit Layer

`Transaction` records the result of a completed operation. It stores the operation type, amount, balance after the operation, account references, status, description, and a unique identifier. The receipt formatter gives the record a human-readable representation without losing structured data.

## Command Layer

I use `TransactionCommand` as the common interface for deposit, withdrawal, and transfer commands. Each command hides how the operation is executed while allowing the caller to retrieve the resulting transaction record.

## Logging Layer

`TransactionLogger` depends on the `LogDestination` contract instead of a concrete storage class. This lets me switch between memory, file, and simulated database destinations without changing the logger or command code.

## How I Extend the Platform

- Add an account product by implementing the account contract and registering it with `AccountFactory`.
- Add a configurable policy by extending the properties files and rules-engine lookup.
- Add a new operation by implementing `TransactionCommand`.
- Add a storage backend by implementing `LogDestination`.
- Add a new audit type by extending `TransactionType` and constructing its record.

## Reliability Rules

I follow these rules throughout the project:

- Validate every request before changing a balance.
- Keep policy decisions in one place.
- Create successful audit records only after money movement completes.
- Keep storage details behind interfaces.
- Preserve earlier behavior as each later capability is added.
