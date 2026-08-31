# MilestoneJury Deployment Evidence

This file is intentionally incomplete until the contract is deployed and exercised with real public data. Do not replace the fields below with invented hashes, links, verdicts, or screenshots.

| Evidence item | Real value after deployment |
|---|---|
| Network | GenLayer Studionet |
| Chain ID | `61999` |
| Contract address | `0x82a061814068fcC3CE15E86262aAf151DB9d4063` |
| Explorer contract URL | https://explorer-studio.genlayer.com/address/0x42c60cC74e76C69b90c2a30285c7fb2f9dD12228 |
| Deployment transaction | https://explorer-studio.genlayer.com/tx/0x5218757c46445875a70674fae25c09682a1a36ac69da8aab3a0fdb39c35b2caf |
| Milestone configuration transaction | `PENDING_REAL_DEPLOYMENT` |
| Delivery-adjudication transaction | `PENDING_REAL_DEPLOYMENT` |
| Finalized status | `FINALIZED` |
| Public delivery URL used in the test | `PENDING_REAL_DEPLOYMENT` |
| Actual consensus decision | `PENDING_REAL_DEPLOYMENT` |
| View-method output captured after finality | `get_status()` returned `decision: NOT_CONFIGURED`, `eligibility: NOT_ELIGIBLE`, `score: 0`, with blank title/criteria/url — expected initial state. |

## Required verification

Before publishing or submitting this contribution, open the Explorer links in an unauthenticated browser session, confirm that the deployed contract is separate from all VeriFlow contracts, and ensure the final transaction is genuinely finalized. The exact source in `MilestoneJury_Studio.py` must match the deployed source.

## Verified finalized deployment evidence

This section records the corrected owner-guarded deployment and the real finalized adjudication evidence. The source used for the deployment is the `MilestoneJury.py` file in this repository at the pushed `main` branch.

| Evidence | Verified value |
|---|---|
| Contract address | [`0x72a4d24d18B2126D1Bdac3aCDE8B54F578b592E9`](https://explorer-studio.genlayer.com/address/0x72a4d24d18B2126D1Bdac3aCDE8B54F578b592E9) |
| Deployment transaction | [`0xd560d5e34a3d82cd954d5f3ac6dff6bc0a14164edd2a00b46d1958b53094de88`](https://explorer-studio.genlayer.com/tx/0xd560d5e34a3d82cd954d5f3ac6dff6bc0a14164edd2a00b46d1958b53094de88) |
| Deployer / owner | `0x1be693074c32541919Bba91aC873464A29c09D68` |
| define_milestone transaction | [`0x89efd6c63c6c3dd5fba72ce91f547159daccbec774af4af80f89fe2ec7b57c46`](https://explorer-studio.genlayer.com/tx/0x89efd6c63c6c3dd5fba72ce91f547159daccbec774af4af80f89fe2ec7b57c46) |
| define_milestone result | `READY_FOR_SUBMISSION` |
| adjudicate_delivery transaction | [`0x56909de0eccbc0eacc53a43eea72ab5bd8390c1ef0a9b42a557f0638d0f930b8`](https://explorer-studio.genlayer.com/tx/0x56909de0eccbc0eacc53a43eea72ab5bd8390c1ef0a9b42a557f0638d0f930b8) |
| adjudication result | `ACCEPTED` |
| adjudication score | `92` |
| eligibility | `AWARD_ELIGIBLE` |
| evidence URL evaluated | [`README.md raw content`](https://github.com/0ogodboyo0/milestonejury-genlayer/raw/refs/heads/main/README.md) |

The adjudication transaction is finalized with GenVM execution success and consensus acceptance. The contract return value is `ACCEPTED`; the stored status reports score `92` and `AWARD_ELIGIBLE`. Earlier failed or out-of-scope trial transactions are not used as the final evidence.
