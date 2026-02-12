# Enum: DecisionAction 




_Action taken on a decision by the curator_



URI: [ere:DecisionAction](https://data.europa.eu/ers/schema/ere/DecisionAction)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ACCEPT_TOP | None | Curator accepted the top candidate |
| ACCEPT_ALTERNATIVE | None | Curator selected an alternative candidate |
| REJECT_ALL | None | Curator rejected all candidates |




## Slots

| Name | Description |
| ---  | --- |
| [action](action.md) | Action taken by curator |





## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere






## LinkML Source

<details>
```yaml
name: DecisionAction
description: Action taken on a decision by the curator
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
permissible_values:
  ACCEPT_TOP:
    text: ACCEPT_TOP
    description: Curator accepted the top candidate
  ACCEPT_ALTERNATIVE:
    text: ACCEPT_ALTERNATIVE
    description: Curator selected an alternative candidate
  REJECT_ALL:
    text: REJECT_ALL
    description: Curator rejected all candidates

```
</details>