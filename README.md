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
| Week 4 | 12-14 | Account policy objects, rules-engine integration, and external properties |
| Week 5 | 15-16 | Funds transfer with daily limits and transaction audit records |
| Week 6 | 17-18 | Command pattern, file logging, bridge logging, and database destination |

## Branch Strategy

Branches are cumulative and named for the feature completed by that activity:

```text
activity-01-account-foundation
activity-02-account-validation
activity-03-account-operations
activity-04-enhanced-account-tests
activity-05-validation-rules
activity-06-account-subclasses
activity-07-interest-policies
activity-08-account-registry
activity-09-account-services
activity-10-account-rules
activity-11-service-integration
activity-12-account-policy
activity-13-rules-engine
activity-14-external-properties
activity-15-funds-transfer
activity-16-transaction-model
activity-17-command-file-logging
activity-18-bridge-logging
```

`main` contains the cumulative result through activity 18. Each activity branch adds one focused improvement while preserving the behavior established by earlier activities. Future refinements can be applied to their activity branch and merged forward into `main` without replacing later features.

## Development Progression

The project grows in deliberate steps: account state and validation lead to product-specific behavior; policy and interest handling lead to abstract accounts and factories; the rules engine then externalizes policy; transfers add operational workflows; transactions, commands, and pluggable logging complete the audit architecture.

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
