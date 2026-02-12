

# Slot: about_entity_mention 


_Reference to the entity mention being resolved_





URI: [ere:about_entity_mention](https://data.europa.eu/ers/schema/ere/about_entity_mention)
Alias: about_entity_mention

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Aggregate root representing a resolution decision requiring curation |  no  |






## Properties

* Range: [EntityMentionIdentifier](EntityMentionIdentifier.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:about_entity_mention |
| native | ere:about_entity_mention |




## LinkML Source

<details>
```yaml
name: about_entity_mention
description: Reference to the entity mention being resolved
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: about_entity_mention
owner: Decision
domain_of:
- Decision
range: EntityMentionIdentifier
required: true

```
</details>