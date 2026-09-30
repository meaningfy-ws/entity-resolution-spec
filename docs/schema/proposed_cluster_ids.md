

# Slot: proposed_cluster_ids 


_When this is present, the ERE may use this information to try to cluster the entity in one of _

_the listed clusters._

__

_In particular, this is used to forward a curator's placement recommendation for an entity_

_that was already resolved: the cluster it is currently placed in, or one of the candidate_

_clusters of the latest resolution. When an initial request is not answered within the ERS_

_time budget, no follow-up request is sent: the provisional identifier that ERS issues is_

_derived with the same rule the ERE uses for a new singleton cluster._

__

_Whatever, the case, the ERE **has no obligation** to fulfil the proposal, how it reacts to _

_this list is implementation dependent, and the ERE remains the ultimate authority to provide _

_the final resolution decision._

__





URI: [ere:proposed_cluster_ids](https://data.europa.eu/ers/schema/ere/proposed_cluster_ids)
Alias: proposed_cluster_ids

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
| self | ere:proposed_cluster_ids |
| native | ere:proposed_cluster_ids |




## LinkML Source

<details>
```yaml
name: proposed_cluster_ids
description: "When this is present, the ERE may use this information to try to cluster\
  \ the entity in one of \nthe listed clusters.\n\nIn particular, this is used to\
  \ forward a curator's placement recommendation for an entity\nthat was already resolved:\
  \ the cluster it is currently placed in, or one of the candidate\nclusters of the\
  \ latest resolution. When an initial request is not answered within the ERS\ntime\
  \ budget, no follow-up request is sent: the provisional identifier that ERS issues\
  \ is\nderived with the same rule the ERE uses for a new singleton cluster.\n\nWhatever,\
  \ the case, the ERE **has no obligation** to fulfil the proposal, how it reacts\
  \ to \nthis list is implementation dependent, and the ERE remains the ultimate authority\
  \ to provide \nthe final resolution decision.\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: proposed_cluster_ids
owner: EntityMentionResolutionRequest
domain_of:
- EntityMentionResolutionRequest
range: string
multivalued: true

```
</details>