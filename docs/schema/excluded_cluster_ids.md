

# Slot: excluded_cluster_ids 


_When this is present, the resolution must not bin the entity mention into any of the_

_listed clusters. This can be used to reject a previous resolution proposed by the ERE._

__

_The exact reaction to this is implementation dependent. In the simplest case, the ERE_

_might just create a singleton cluster with this entity as member. In a more advanced _

_case, it might recompute the similarity with more advanced algorithms or use updated_

_data._

__

_TODO: Can this be revised? What does it happen if an exclusion was made by mistake?_

__





URI: [ere:excluded_cluster_ids](https://data.europa.eu/ers/schema/ere/excluded_cluster_ids)
Alias: excluded_cluster_ids

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:excluded_cluster_ids |
| native | ere:excluded_cluster_ids |




## LinkML Source

<details>
```yaml
name: excluded_cluster_ids
description: "When this is present, the resolution must not bin the entity mention\
  \ into any of the\nlisted clusters. This can be used to reject a previous resolution\
  \ proposed by the ERE.\n\nThe exact reaction to this is implementation dependent.\
  \ In the simplest case, the ERE\nmight just create a singleton cluster with this\
  \ entity as member. In a more advanced \ncase, it might recompute the similarity\
  \ with more advanced algorithms or use updated\ndata.\n\nTODO: Can this be revised?\
  \ What does it happen if an exclusion was made by mistake?\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: excluded_cluster_ids
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: string
multivalued: true

```
</details>