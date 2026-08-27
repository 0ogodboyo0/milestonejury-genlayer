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

The contract was deployed and finalized on GenLayer Studionet at [`0x42c60cC74e76C69b90c2a30285c7fb2f9dD12228`](https://explorer-studio.genlayer.com/address/0x42c60cC74e76C69b90c2a30285c7fb2f9dD12228). The finalized deployment transaction is available on the [Studio Explorer](https://explorer-studio.genlayer.com/tx/0x5218757c46445875a70674fae25c09682a1a36ac69da8aab3a0fdb39c35b2caf).

The next real interaction must configure a genuine milestone and submit a public GitHub page that genuinely relates to those criteria. Its Explorer links and final result will be added to `docs/DEPLOYMENT.md`. No fabricated activity, content, links, or verdicts belong in this repository.

## References

[1] [GenLayer — When to Use GenLayer](https://docs.genlayer.com/developers/intelligent-contracts/when-to-use-genlayer)
