

# Slot: entity_type 


_A string representing the entity type (based on CET). This is typically a URI._

__

_Note that this is at this level, and not at `EntityMention`, since, as said above, _

_it's needed to identify the entity, even when its content is not present. For the same_

_reason, it's used both for `EREResolutionRequest` and `EREResolutionResponse` messages.,_

__





URI: [ere:entity_type](https://data.europa.eu/ers/schema/ere/entity_type)
Alias: entity_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionIdentifier](EntityMentionIdentifier.md) | A container that groups the attributes needed to identify an entity mention i... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:entity_type |
| native | ere:entity_type |




## LinkML Source

<details>
```yaml
name: entity_type
description: "A string representing the entity type (based on CET). This is typically\
  \ a URI.\n\nNote that this is at this level, and not at `EntityMention`, since,\
  \ as said above, \nit's needed to identify the entity, even when its content is\
  \ not present. For the same\nreason, it's used both for `EREResolutionRequest` and\
  \ `EREResolutionResponse` messages.,\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: entity_type
owner: EntityMentionIdentifier
domain_of:
- EntityMentionIdentifier
range: string
required: true

```
</details>