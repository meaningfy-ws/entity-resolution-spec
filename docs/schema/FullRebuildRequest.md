

# Class: FullRebuildRequest 


_A request to reset all the resolutions computed so far and possibly rebuild them as _

_requests about old entities arrive again (and build new entities from scratch as usually)._

__

_It is expected that the ERE client re-sends all the entities to be resolved again,_

_using `EntityMentionResolutionRequest` messages exactly as the first time the resolutions _

_were built. This implies the a client like the ERS logs/persists the entities it receives_

_to resolve and also saves manual overriding of ERE results._

__

_Moreover:_

_* The ERE must keep track of past `EntityMention` marked as canonical._

_* The ERE must retain requests with `excluded_cluster_ids` and apply them again when the _

_  same entity mention is re-sent after the full rebuild. TODO: see notes about these properties,_

_  on the possible need of withdrawing exclusions._

__





URI: [ere:FullRebuildRequest](https://data.europa.eu/ers/schema/ere/FullRebuildRequest)





```mermaid
 classDiagram
    class FullRebuildRequest
    click FullRebuildRequest href "../FullRebuildRequest/"
      ERERequest <|-- FullRebuildRequest
        click ERERequest href "../ERERequest/"
      
      FullRebuildRequest : ere_request_id
        
      FullRebuildRequest : timestamp
        
      FullRebuildRequest : type
        
      
```





## Inheritance
* [EREMessage](EREMessage.md)
    * [ERERequest](ERERequest.md)
        * **FullRebuildRequest**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [EREMessage](EREMessage.md) |
| [ere_request_id](ere_request_id.md) | 1 <br/> [String](String.md) | A string representing the unique ID of an ERE request, or the ID of the reque... | [EREMessage](EREMessage.md) |
| [timestamp](timestamp.md) | 0..1 <br/> [Datetime](Datetime.md) | The time when the message was created | [EREMessage](EREMessage.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:FullRebuildRequest |
| native | ere:FullRebuildRequest |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FullRebuildRequest
description: "A request to reset all the resolutions computed so far and possibly\
  \ rebuild them as \nrequests about old entities arrive again (and build new entities\
  \ from scratch as usually).\n\nIt is expected that the ERE client re-sends all the\
  \ entities to be resolved again,\nusing `EntityMentionResolutionRequest` messages\
  \ exactly as the first time the resolutions \nwere built. This implies the a client\
  \ like the ERS logs/persists the entities it receives\nto resolve and also saves\
  \ manual overriding of ERE results.\n\nMoreover:\n* The ERE must keep track of past\
  \ `EntityMention` marked as canonical.\n* The ERE must retain requests with `excluded_cluster_ids`\
  \ and apply them again when the \n  same entity mention is re-sent after the full\
  \ rebuild. TODO: see notes about these properties,\n  on the possible need of withdrawing\
  \ exclusions.\n"
from_schema: https://data.europa.eu/ers/schema/ere
is_a: ERERequest

```
</details>

### Induced

<details>
```yaml
name: FullRebuildRequest
description: "A request to reset all the resolutions computed so far and possibly\
  \ rebuild them as \nrequests about old entities arrive again (and build new entities\
  \ from scratch as usually).\n\nIt is expected that the ERE client re-sends all the\
  \ entities to be resolved again,\nusing `EntityMentionResolutionRequest` messages\
  \ exactly as the first time the resolutions \nwere built. This implies the a client\
  \ like the ERS logs/persists the entities it receives\nto resolve and also saves\
  \ manual overriding of ERE results.\n\nMoreover:\n* The ERE must keep track of past\
  \ `EntityMention` marked as canonical.\n* The ERE must retain requests with `excluded_cluster_ids`\
  \ and apply them again when the \n  same entity mention is re-sent after the full\
  \ rebuild. TODO: see notes about these properties,\n  on the possible need of withdrawing\
  \ exclusions.\n"
from_schema: https://data.europa.eu/ers/schema/ere
is_a: ERERequest
attributes:
  type:
    name: type
    description: "The type of the request or result.\n\nAs per LinkML specification,\
      \ `designates_type` is used here in order to allow for this\nslot to tell the\
      \ concrete subclass that an instance (such as a JSON object) belongs to.\n\n\
      In other words, a particular request will have `type` set with values like \n\
      `EntityMentionResolutionRequest` or `EntityResolutionResult`\n"
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    designates_type: true
    alias: type
    owner: FullRebuildRequest
    domain_of:
    - EREMessage
    range: string
    required: true
  ere_request_id:
    name: ere_request_id
    description: 'A string representing the unique ID of an ERE request, or the ID
      of the request a response is about.

      This **is not** the same as `request_id` + `source_id`.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: ere_request_id
    owner: FullRebuildRequest
    domain_of:
    - EREMessage
    range: string
    required: true
  timestamp:
    name: timestamp
    description: 'The time when the message was created. Should be in ISO-8601 format.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: timestamp
    owner: FullRebuildRequest
    domain_of:
    - EREMessage
    range: datetime

```
</details>