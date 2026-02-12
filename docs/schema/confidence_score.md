

# Slot: confidence_score 


_A 0-1 value of how confident the ERE is about the equivalence between the subject entity mention_

_and the target canonical entity._

__





URI: [ere:confidence_score](https://data.europa.eu/ers/schema/ere/confidence_score)
Alias: confidence_score

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClusterReference](ClusterReference.md) | A reference to a cluster to which an entity is deemed to belong, with an asso... |  no  |






## Properties

* Range: [Float](Float.md)

* Required: True

* Minimum Value: 0

* Maximum Value: 1




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:confidence_score |
| native | ere:confidence_score |




## LinkML Source

<details>
```yaml
name: confidence_score
description: 'A 0-1 value of how confident the ERE is about the equivalence between
  the subject entity mention

  and the target canonical entity.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: confidence_score
owner: ClusterReference
domain_of:
- ClusterReference
range: float
required: true
minimum_value: 0.0
maximum_value: 1.0

```
</details>