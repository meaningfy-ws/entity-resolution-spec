

# Slot: request_id 


_A string representing the unique ID of the request made to the ERS system. In general, this is unique_

_only within the scope of the source and the entity type, ie, within `sourceId` and `entityType`. _

__

_Moreover, this is **not** the same as `ereRequestId`, which instead, is internal to the ERE and is _

_used to match responses to requests._

__





URI: [ere:request_id](https://data.europa.eu/ers/schema/ere/request_id)
Alias: request_id

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
| self | ere:request_id |
| native | ere:request_id |




## LinkML Source

<details>
```yaml
name: request_id
description: "A string representing the unique ID of the request made to the ERS system.\
  \ In general, this is unique\nonly within the scope of the source and the entity\
  \ type, ie, within `sourceId` and `entityType`. \n\nMoreover, this is **not** the\
  \ same as `ereRequestId`, which instead, is internal to the ERE and is \nused to\
  \ match responses to requests.\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: request_id
owner: EntityMentionIdentifier
domain_of:
- EntityMentionIdentifier
range: string
required: true

```
</details>