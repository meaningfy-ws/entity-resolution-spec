

# Slot: status 


_Current status in the curation workflow_





URI: [ere:status](https://data.europa.eu/ers/schema/ere/status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Aggregate root representing a resolution decision requiring curation |  no  |






## Properties

* Range: [DecisionStatus](DecisionStatus.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:status |
| native | ere:status |




## LinkML Source

<details>
```yaml
name: status
description: Current status in the curation workflow
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: status
owner: Decision
domain_of:
- Decision
range: DecisionStatus
required: true

```
</details>