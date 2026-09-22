# Banking System

Progressive banking-system coursework organized by activity and feature branch.

## Repository Layout

Each activity lives under `activities/activity-01` through `activities/activity-18`.
Instructional material, questions, archives, generated caches, and submission wrappers are excluded from the clean project tree.

## Weekly Roadmap

| Week | Activities | Focus |
| --- | --- | --- |
| Week 1 | 01-04 | Account foundations, validation, and enhanced account behavior |
| Week 2 | 05-08 | Validation, account subclasses, interest policies, and account registry |
| Week 3 | 09-11 | Additional account capabilities and service-level behavior |
| Week 4 | 12-14 | Typed account policy bridge, rules-engine integration, and external properties |
| Week 5 | 15-16 | Funds transfer with daily limits and transaction audit records |
| Week 6 | 17-18 | Command pattern, file logging, bridge logging, and database destination |

## Branch Strategy

Branches are cumulative and named for the feature completed by that activity:

```text
activity-01-account-foundation
activity-02-account-validation
activity-03-account-operations
activity-04-enhanced-account-tests
activity-05-checkpoint
activity-06-checkpoint
activity-07-checkpoint
activity-08-checkpoint
activity-09-account-services
activity-10-account-rules
activity-11-service-integration
activity-12-checkpoint
activity-13-rules-engine
activity-14-external-properties
activity-15-funds-transfer
activity-16-transaction-model
activity-17-command-file-logging
activity-18-bridge-logging
```

`main` contains the cumulative result through activity 18. A later activity 12 implementation can be added on `activity-12-checkpoint`, merged into the subsequent activity branches, and then merged into `main` without deleting or replacing activity 18.

## Reconstructed Bridge Activities

Activities 5-8 and 12 were not available in the supplied semester folders. They contain small compatibility implementations inferred from the surrounding progression: validation, product subclasses, interest policies, an account registry, and a typed policy model. These folders are isolated so a later original submission can replace only its matching activity without changing activity 18.

## Local Verification

Run tests from the activity folder that contains the relevant `gdb` package. For example:

```powershell
Set-Location .\activities\activity-15
python -m gdb.tests.test_transfer -v
```

## GitHub Deployment

```powershell
git remote -v
git branch -a
git push origin main
git push origin --all
```
