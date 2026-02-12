# Enum: DecisionStatus 




_Status of a resolution decision in the curation workflow_



URI: [ere:DecisionStatus](https://data.europa.eu/ers/schema/ere/DecisionStatus)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| AUTOMATIC_CONFIDENT | None | Resolution confidence exceeds threshold; no manual review required |
| PENDING_MANUAL_REVIEW | None | Resolution confidence below threshold; awaiting curator action |
| MANUALLY_REVIEWED | None | Curator has taken an action |




## Slots

| Name | Description |
| ---  | --- |
| [status](status.md) | Current status in the curation workflow |





## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere






## LinkML Source

<details>
```yaml
name: DecisionStatus
description: Status of a resolution decision in the curation workflow
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
permissible_values:
  AUTOMATIC_CONFIDENT:
    text: AUTOMATIC_CONFIDENT
    description: Resolution confidence exceeds threshold; no manual review required
  PENDING_MANUAL_REVIEW:
    text: PENDING_MANUAL_REVIEW
    description: Resolution confidence below threshold; awaiting curator action
  MANUALLY_REVIEWED:
    text: MANUALLY_REVIEWED
    description: Curator has taken an action

```
</details>