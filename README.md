# MilestoneJury

**MilestoneJury** is a GenLayer Intelligent Contract for transparent acceptance review of public open-source work. A project owner fixes a natural-language milestone on-chain, then a contributor submits a public GitHub or GitLab delivery URL. GenLayer validators independently fetch the page and reach consensus on whether the work is accepted, requires revision, or is out of scope.

> This contribution is independent from VeriFlow. It does not attest financial evidence, review collateral, or produce an evidence-verification outcome. It performs **milestone-adjudication for public code deliveries** and records a distinct on-chain award-eligibility status.

## On-chain flow

| Step | Public method | Purpose | State change |
|---|---|---|---|
| 1 | `define_milestone(title, criteria)` | Records a one-time, natural-language milestone. | Locks the public criteria for later review. |
| 2 | `adjudicate_delivery(url, summary)` | Fetches a public GitHub page and asks validators to apply the fixed criteria. | Stores consensus decision, completion score, reason, and award eligibility. |
| 3 | `get_status()` | Reads the fixed criteria and latest consensus result without a transaction. | None. |

The verdicts are `ACCEPTED`, `REVISION_REQUESTED`, and `OUT_OF_SCOPE`. Only `ACCEPTED` writes `AWARD_ELIGIBLE`; this gives a future bounty board a neutral, on-chain completion condition without making this proof-of-payment contract responsible for holding user funds.

## GenLayer-native adjudication

The contract uses `gl.nondet.web.get` to retrieve the delivery page, `gl.nondet.exec_prompt` for a constrained structured evaluation, and `gl.vm.run_nondet_unsafe` with a validator function. A validator independently repeats the assessment, must agree with the category, and must score within 12 points before the result can be accepted. This implements the neutral-consensus pattern that GenLayer identifies as suitable for language-based, independently checkable decisions.[1]

The adjudication prompt treats all fetched content as untrusted data, rejects unsupported URLs, preserves pre-agreed criteria in contract storage, and returns only a bounded public result. It deliberately avoids identity, legal, investment, KYC, AML, reputation, ownership, and financial claims.

## Repository structure

| Path | Description |
|---|---|
| `MilestoneJury.py` | Exact Python source deployed as `MilestoneJury_v2.py` in GenLayer Studio, including the runner-version header. |
| `docs/CONTRACT_DESIGN.md` | Contract boundaries, security choices, and test scenario. |
| `docs/DEPLOYMENT.md` | Real Studionet deployment evidence and placeholders for the forthcoming real milestone test. |
| `tests/test_contract_source.py` | Static regression checks for the source’s declared public methods and consensus primitives. |

## Intended real test

The corrected contract was deployed and finalized on GenLayer Studionet at [`0x72a4d24d18B2126D1Bdac3aCDE8B54F578b592E9`](https://explorer-studio.genlayer.com/address/0x72a4d24d18B2126D1Bdac3aCDE8B54F578b592E9). The finalized deployment transaction is available on the [Studio Explorer](https://explorer-studio.genlayer.com/tx/0xd560d5e34a3d82cd954d5f3ac6dff6bc0a14164edd2a00b46d1958b53094de88).

The contract was configured through the finalized [`define_milestone` transaction](https://explorer-studio.genlayer.com/tx/0x89efd6c63c6c3dd5fba72ce91f547159daccbec774af4af80f89fe2ec7b57c46) and the public README evidence was evaluated through the finalized [`adjudicate_delivery` transaction](https://explorer-studio.genlayer.com/tx/0x56909de0eccbc0eacc53a43eea72ab5bd8390c1ef0a9b42a557f0638d0f930b8).

The real adjudication returned `ACCEPTED` with score `92` and `AWARD_ELIGIBLE`. No fabricated activity, content, links, or verdicts belong in this repository.

## References

[1] [GenLayer — When to Use GenLayer](https://docs.genlayer.com/developers/intelligent-contracts/when-to-use-genlayer)

## Owner authorization

The milestone configuration is controlled by the contract deployer. During initialization, the contract stores the deployment caller as `owner`; `define_milestone` rejects every other caller before it can write any criteria. The function also remains one-time only, so the owner cannot replace criteria after they have been recorded.

Relevant implementation in [`MilestoneJury.py`](./MilestoneJury.py):

```python
class MilestoneJury(gl.Contract):
    owner: Address

    def __init__(self):
        self.owner = gl.message.sender_address
        # Other state is initialized here.

    @gl.public.write
    def define_milestone(self, title: str, criteria: str) -> str:
        if gl.message.sender_address != self.owner:
            raise gl.vm.UserError("Only the contract owner can define the milestone")
        if self.title != "":
            raise gl.vm.UserError("Milestone is already defined")
```

This authorization is also covered by the repository source checks and is present in the exact source used for the corrected deployment. The deployed contract address and finalized transaction evidence are recorded in [`docs/DEPLOYMENT.md`](./docs/DEPLOYMENT.md).
