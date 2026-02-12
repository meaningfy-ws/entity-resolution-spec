

# Slot: source_id 


_The ID or URI of the ERS client that originated the request. This identifies an application or a _

_person accessing the ERS system._

__





URI: [ere:source_id](https://data.europa.eu/ers/schema/ere/source_id)
Alias: source_id

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
| self | ere:source_id |
| native | ere:source_id |




## LinkML Source

<details>
```yaml
name: source_id
description: "The ID or URI of the ERS client that originated the request. This identifies\
  \ an application or a \nperson accessing the ERS system.\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: source_id
owner: EntityMentionIdentifier
domain_of:
- EntityMentionIdentifier
range: string
required: true

```
</details>