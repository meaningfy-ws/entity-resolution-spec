

# Class: ClusterReference 


_A reference to a cluster to which an entity is deemed to belong, with an associated confidence score._

__

_A cluster is a set of entity mentions that have been determined to refer to the same real-world entity._

_Each cluster has a unique clusterId._

__

_A cluster reference is used to report the association between an entity mention and a cluster _

_of equivalence._

__





URI: [ere:ClusterReference](https://data.europa.eu/ers/schema/ere/ClusterReference)





```mermaid
 classDiagram
    class ClusterReference
    click ClusterReference href "../ClusterReference/"
      ClusterReference : cluster_id
        
          
    
        
        
        ClusterReference --> "1" CanonicalEntityIdentifier : cluster_id
        click CanonicalEntityIdentifier href "../CanonicalEntityIdentifier/"
    

        
      ClusterReference : confidence_score
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cluster_id](cluster_id.md) | 1 <br/> [CanonicalEntityIdentifier](CanonicalEntityIdentifier.md) | The identifier of the cluster/canonical entity that is considered equivalent ... | direct |
| [confidence_score](confidence_score.md) | 1 <br/> [Float](Float.md) | A 0-1 value of how confident the ERE is about the equivalence between the sub... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | [candidates](candidates.md) | range | [ClusterReference](ClusterReference.md) |
| [Decision](Decision.md) | [accepted_candidate](accepted_candidate.md) | range | [ClusterReference](ClusterReference.md) |
| [Decision](Decision.md) | [candidates](candidates.md) | range | [ClusterReference](ClusterReference.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:ClusterReference |
| native | ere:ClusterReference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ClusterReference
description: "A reference to a cluster to which an entity is deemed to belong, with\
  \ an associated confidence score.\n\nA cluster is a set of entity mentions that\
  \ have been determined to refer to the same real-world entity.\nEach cluster has\
  \ a unique clusterId.\n\nA cluster reference is used to report the association between\
  \ an entity mention and a cluster \nof equivalence.\n"
from_schema: https://data.europa.eu/ers/schema/ere
attributes:
  cluster_id:
    name: cluster_id
    description: 'The identifier of the cluster/canonical entity that is considered
      equivalent to the

      subject entity mention that an `EntityMentionResolutionResponse` refers to.

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    domain_of:
    - ClusterReference
    range: CanonicalEntityIdentifier
    required: true
  confidence_score:
    name: confidence_score
    description: 'A 0-1 value of how confident the ERE is about the equivalence between
      the subject entity mention

      and the target canonical entity.

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    domain_of:
    - ClusterReference
    range: float
    required: true
    minimum_value: 0.0
    maximum_value: 1.0

```
</details>

### Induced

<details>
```yaml
name: ClusterReference
description: "A reference to a cluster to which an entity is deemed to belong, with\
  \ an associated confidence score.\n\nA cluster is a set of entity mentions that\
  \ have been determined to refer to the same real-world entity.\nEach cluster has\
  \ a unique clusterId.\n\nA cluster reference is used to report the association between\
  \ an entity mention and a cluster \nof equivalence.\n"
from_schema: https://data.europa.eu/ers/schema/ere
attributes:
  cluster_id:
    name: cluster_id
    description: 'The identifier of the cluster/canonical entity that is considered
      equivalent to the

      subject entity mention that an `EntityMentionResolutionResponse` refers to.

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    alias: cluster_id
    owner: ClusterReference
    domain_of:
    - ClusterReference
    range: CanonicalEntityIdentifier
    required: true
  confidence_score:
    name: confidence_score
    description: 'A 0-1 value of how confident the ERE is about the equivalence between
      the subject entity mention

      and the target canonical entity.

      '
    from_schema: https://data.europa.eu/ers/schema/ers
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