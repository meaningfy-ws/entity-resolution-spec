

# Slot: entity_mention_id 


_The identifier of the entity mention that has been resolved._

__

_This isn't strictly needed, since the `ere_request_id` already links the response to _

_the request's entity mention. Yet, it's reported for convenience._

__





URI: [ere:entity_mention_id](https://data.europa.eu/ers/schema/ere/entity_mention_id)
Alias: entity_mention_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |






## Properties

* Range: [EntityMentionIdentifier](EntityMentionIdentifier.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:entity_mention_id |
| native | ere:entity_mention_id |




## LinkML Source

<details>
```yaml
name: entity_mention_id
description: "The identifier of the entity mention that has been resolved.\n\nThis\
  \ isn't strictly needed, since the `ere_request_id` already links the response to\
  \ \nthe request's entity mention. Yet, it's reported for convenience.\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: entity_mention_id
owner: EntityMentionResolutionResponse
domain_of:
- EntityMentionResolutionResponse
range: EntityMentionIdentifier
required: true

```
</details>