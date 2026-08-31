# MilestoneJury Deployment Evidence

This document records the corrected owner-guarded deployment and the real finalized execution evidence for MilestoneJury.

| Evidence item | Verified value |
|---|---|
| Network | GenLayer Studionet |
| Contract address | [`0x72a4d24d18B2126D1Bdac3aCDE8B54F578b592E9`](https://explorer-studio.genlayer.com/address/0x72a4d24d18B2126D1Bdac3aCDE8B54F578b592E9) |
| Deployer / owner | `0x1be693074c32541919Bba91aC873464A29c09D68` |
| Deployment transaction | [`0xd560d5e34a3d82cd954d5f3ac6dff6bc0a14164edd2a00b46d1958b53094de88`](https://explorer-studio.genlayer.com/tx/0xd560d5e34a3d82cd954d5f3ac6dff6bc0a14164edd2a00b46d1958b53094de88) |
| `define_milestone` transaction | [`0x89efd6c63c6c3dd5fba72ce91f547159daccbec774af4af80f89fe2ec7b57c46`](https://explorer-studio.genlayer.com/tx/0x89efd6c63c6c3dd5fba72ce91f547159daccbec774af4af80f89fe2ec7b57c46) |
| `define_milestone` result | `READY_FOR_SUBMISSION` |
| `adjudicate_delivery` transaction | [`0x56909de0eccbc0eacc53a43eea72ab5bd8390c1ef0a9b42a557f0638d0f930b8`](https://explorer-studio.genlayer.com/tx/0x56909de0eccbc0eacc53a43eea72ab5bd8390c1ef0a9b42a557f0638d0f930b8) |
| Adjudication result | `ACCEPTED` |
| Score | `92` |
| Eligibility | `AWARD_ELIGIBLE` |
| Evidence URL evaluated | [`README.md raw content`](https://github.com/0ogodboyo0/milestonejury-genlayer/raw/refs/heads/main/README.md) |

## Verification notes

The deployed source is the owner-guarded `MilestoneJury.py` in this repository. During initialization, the deployer is stored as `owner`; `define_milestone` rejects other callers and remains one-time only. The successful adjudication transaction is finalized with GenVM execution success and consensus acceptance, and the contract return value is `ACCEPTED`.

Earlier failed or out-of-scope trial transactions are not used as final evidence. The repository, deployment, milestone configuration, adjudication, and final result above refer to the same corrected contract and public source.
