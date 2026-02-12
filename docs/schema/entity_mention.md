

# Slot: entity_mention 


_The data about the entity to be resolved. Note that, at least for the moment, we don't support_

_batch requests, so this property is single-valued._

__





URI: [ere:entity_mention](https://data.europa.eu/ers/schema/ere/entity_mention)
Alias: entity_mention

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






## Properties

* Range: [EntityMention](EntityMention.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:entity_mention |
| native | ere:entity_mention |




## LinkML Source

<details>
```yaml
name: entity_mention
description: 'The data about the entity to be resolved. Note that, at least for the
  moment, we don''t support

  batch requests, so this property is single-valued.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: entity_mention
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: EntityMention
required: true

```
</details>