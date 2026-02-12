

# Slot: cluster_id 


_The identifier of the cluster/canonical entity that is considered equivalent to the_

_subject entity mention that an `EntityMentionResolutionResponse` refers to._

__





URI: [ere:cluster_id](https://data.europa.eu/ers/schema/ere/cluster_id)
Alias: cluster_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClusterReference](ClusterReference.md) | A reference to a cluster to which an entity is deemed to belong, with an asso... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:cluster_id |
| native | ere:cluster_id |




## LinkML Source

<details>
```yaml
name: cluster_id
description: 'The identifier of the cluster/canonical entity that is considered equivalent
  to the

  subject entity mention that an `EntityMentionResolutionResponse` refers to.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: cluster_id
owner: ClusterReference
domain_of:
- ClusterReference
range: string
required: true

```
</details>