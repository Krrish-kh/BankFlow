# Welcome to BankFlow

BankFlow is a modular core banking platform focused on dependable account operations, controlled money movement, and traceable transaction workflows.

I built the platform in progressive stages so each capability can be understood, tested, and extended independently. The current release brings those stages together into one cumulative banking core.

## Explore BankFlow

- [Getting Started](Getting-Started) - install, run, and verify the project
- [Architecture](Architecture) - understand the system boundaries and extension points
- [Activity Roadmap](Activity-Roadmap) - follow the platform's capability progression

## Core Areas

| Area | Purpose |
| --- | --- |
| Accounts | Manage account products, balances, lifecycle, and PIN protection |
| Rules | Centralize configurable financial policies and limits |
| Transfers | Move funds with validation and daily control rules |
| Transactions | Record successful operations with receipts and identifiers |
| Commands | Execute banking operations through a consistent interface |
| Logging | Store audit records in file, memory, or database-style destinations |

## Current Release

The `main` branch contains the integrated implementation through activity 18. The final stage provides command workflows and runtime-selectable logging destinations on top of the transaction and transfer layers.

## Quick Links

- [Source repository](https://github.com/Krrish-kh/BankFlow)
- [Main branch](https://github.com/Krrish-kh/BankFlow/tree/main)
- [Activity branches](https://github.com/Krrish-kh/BankFlow/branches)
