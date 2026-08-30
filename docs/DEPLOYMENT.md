# MilestoneJury Deployment Evidence

This file is intentionally incomplete until the contract is deployed and exercised with real public data. Do not replace the fields below with invented hashes, links, verdicts, or screenshots.

| Evidence item | Real value after deployment |
|---|---|
| Network | GenLayer Studionet |
| Chain ID | `61999` |
| Contract address | `0x82a061814068fcC3CE15E86262aAf151DB9d4063` |
| Explorer contract URL | https://explorer-studio.genlayer.com/address/0x82a061814068fcC3CE15E86262aAf151DB9d4063 |
| Deployment transaction | https://explorer-studio.genlayer.com/tx/0x5218757c46445875a70674fae25c09682a1a36ac69da8aab3a0fdb39c35b2caf |
| Milestone configuration transaction | `PENDING_REAL_DEPLOYMENT` |
| Delivery-adjudication transaction | `PENDING_REAL_DEPLOYMENT` |
| Finalized status | `FINALIZED` |
| Public delivery URL used in the test | `PENDING_REAL_DEPLOYMENT` |
| Actual consensus decision | `PENDING_REAL_DEPLOYMENT` |
| View-method output captured after finality | `get_status()` returned `decision: NOT_CONFIGURED`, `eligibility: NOT_ELIGIBLE`, `score: 0`, with blank title/criteria/url — expected initial state. |

## Required verification

Before publishing or submitting this contribution, open the Explorer links in an unauthenticated browser session, confirm that the deployed contract is separate from all VeriFlow contracts, and ensure the final transaction is genuinely finalized. The exact source in `MilestoneJury_Studio.py` must match the deployed source.
