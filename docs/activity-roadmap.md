# Activity Roadmap

BankFlow Core Banking Platform develops through focused capability releases. Every branch adds one bounded improvement to the cumulative `main` line.

| Activity | Branch | Capability |
| --- | --- | --- |
| 01 | `activity-01-account-foundation` | Core account state and balance operations |
| 02 | `activity-02-account-validation` | Account behavior verification |
| 03 | `activity-03-account-operations` | Enhanced lifecycle, PIN, and balance safeguards |
| 04 | `activity-04-enhanced-account-tests` | Enhanced account operation coverage |
| 05 | `activity-05-validation-rules` | Reusable input validation and domain errors |
| 06 | `activity-06-account-subclasses` | Product-specific account behavior |
| 07 | `activity-07-interest-policies` | Interest policy calculation |
| 08 | `activity-08-account-registry` | Account collection and lookup services |
| 09 | `activity-09-abstract-accounts` | Abstract account contract and polymorphism |
| 10 | `activity-10-polymorphic-testing` | Cross-product integration verification |
| 11 | `activity-11-interface-factory` | Interface-driven construction with `AccountFactory` |
| 12 | `activity-12-account-policy` | Typed policy model for account decisions |
| 13 | `activity-13-rules-engine` | Centralized rules-engine evaluation |
| 14 | `activity-14-external-properties` | Runtime-loaded external business rules |
| 15 | `activity-15-funds-transfer` | Secure transfers and daily tenure-based limits |
| 16 | `activity-16-transaction-model` | Structured transaction records and receipts |
| 17 | `activity-17-command-file-logging` | Command workflows and file persistence |
| 18 | `activity-18-bridge-logging` | Pluggable file, memory, and database logging |

## Branch Workflow

1. Develop a capability on its activity branch.
2. Run the activity tests and relevant regression tests.
3. Merge the branch into the next cumulative stage.
4. Keep `main` aligned with the latest integrated activity.
