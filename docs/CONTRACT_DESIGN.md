# MilestoneJury Contract Design

## Purpose and separation

MilestoneJury handles the **acceptance of public open-source delivery work** against a fixed milestone. It is not an evidence-attestation system. The contract’s state transition is from a defined milestone to a consensus-backed completion decision and `AWARD_ELIGIBLE` flag.

| Dimension | MilestoneJury | Prior VeriFlow contribution |
|---|---|---|
| Domain | Open-source milestone delivery | Public collateral-evidence review |
| Input | Fixed delivery criteria, code-hosting URL, contributor summary | Evidence URL and asset/issuer subject |
| Consensus output | Completion decision, score, award eligibility | Evidence-verification decision and confidence |
| On-chain consequence | A bounty-ready completion condition | A standalone attestation record |
| Allowed source | Public GitHub/GitLab delivery page | General public HTTPS evidence page |

## Safety boundaries

The initial release contains no money transfer, escrow custody, token issuance, identity verification, or legal determination. The contract does not use a claimed contributor identity as evidence. It accepts only public GitHub URLs so validators can inspect comparable material.

Fetched web content is explicitly isolated as untrusted data. The prompt says to ignore instructions inside the page and to ground its result only in material demonstrably present on that page. The result schema and length bounds prevent opaque free-form outputs from being stored on-chain.

## Consistency design

Each adjudication executes the leader assessment and a validator assessment. The validator must return exactly the same decision category and a completion score within 12 points. If the criterion does not hold, consensus does not accept the candidate result.

## Studio test scenario

Use criteria that describe a real, observable delivery. For example, configure a milestone requiring a public repository README to document a specific feature and setup steps. Then submit a genuinely relevant public repository or pull-request URL with a short factual summary. A result of `REVISION_REQUESTED` or `OUT_OF_SCOPE` is still a technically valid finalized contract interaction; the verdict must never be invented or changed to improve a submission.
