

# Slot: equivalent_to 


_Entity mentions that have been resolved to this canonical entity._





URI: [ere:equivalent_to](https://data.europa.eu/ers/schema/ere/equivalent_to)
Alias: equivalent_to

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CanonicalEntityIdentifier](CanonicalEntityIdentifier.md) | A logical identity construct providing a stable identity anchor |  no  |






## Properties

* Range: [EntityMentionIdentifier](EntityMentionIdentifier.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:equivalent_to |
| native | ere:equivalent_to |




## LinkML Source

<details>
```yaml
name: equivalent_to
description: Entity mentions that have been resolved to this canonical entity.
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: equivalent_to
owner: CanonicalEntityIdentifier
domain_of:
- CanonicalEntityIdentifier
range: EntityMentionIdentifier
required: true
multivalued: true

```
</details>