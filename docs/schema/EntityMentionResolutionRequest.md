

# Class: EntityMentionResolutionRequest 


_An entity resolution request sent to the ERE, containing the entity to be resolved._

__





URI: [ere:EntityMentionResolutionRequest](https://data.europa.eu/ers/schema/ere/EntityMentionResolutionRequest)





```mermaid
 classDiagram
    class EntityMentionResolutionRequest
    click EntityMentionResolutionRequest href "../EntityMentionResolutionRequest/"
      ERERequest <|-- EntityMentionResolutionRequest
        click ERERequest href "../ERERequest/"
      
      EntityMentionResolutionRequest : entity_mention
        
          
    
        
        
        EntityMentionResolutionRequest --> "1" EntityMention : entity_mention
        click EntityMention href "../EntityMention/"
    

        
      EntityMentionResolutionRequest : ere_request_id
        
      EntityMentionResolutionRequest : excluded_cluster_ids
        
      EntityMentionResolutionRequest : timestamp
        
      EntityMentionResolutionRequest : type
        
      
```





## Inheritance
* [EREMessage](EREMessage.md)
    * [ERERequest](ERERequest.md)
        * **EntityMentionResolutionRequest**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [entity_mention](entity_mention.md) | 1 <br/> [EntityMention](EntityMention.md) | The data about the entity to be resolved | direct |
| [excluded_cluster_ids](excluded_cluster_ids.md) | * <br/> [String](String.md) | When this is present, the resolution must not bin the entity mention into any... | direct |
| [type](type.md) | 1 <br/> [String](String.md) | The type of the request or result | [EREMessage](EREMessage.md) |
| [ere_request_id](ere_request_id.md) | 1 <br/> [String](String.md) | A string representing the unique ID of an ERE request, or the ID of the reque... | [EREMessage](EREMessage.md) |
| [timestamp](timestamp.md) | 0..1 <br/> [Datetime](Datetime.md) | The time when the message was created | [EREMessage](EREMessage.md) |











## Examples

| Value |
| --- |
| {
  "type": "EntityMentionResolutionRequest",
  "entity_mention": { 
    "identifier": {
      "request_id": "324fs3r345vx",
      "source_id": "TEDSWS",
      "entity_type": "http://www.w3.org/ns/org#Organization"
    },
    "content": "epd:ent005 a org:Organization; ...   cccev:telephone \"+44 1924306780\" .",
    "content_type": "text/turtle"
  },
  "timestamp": "2026-01-14T12:34:56Z",
  // As said, we need this internal ID and it can be auto-generated (eg, with UUIDs)
  "ere_request_id": "324fs3r345vx:01"
}
 |
| {
  "type": "EntityMentionResolutionRequest",
  "entity_mention": { 
    "identifier": {
      "request_id": "324fs3r345vxab",
      "source_id": "TEDSWS",
      "entity_type": "http://www.w3.org/ns/org#Organization",
    },
    "content": "epd:ent005 a org:Organization; ...   cccev:telephone \"+44 1924306780\" .",
    "content_type": "text/turtle"
  },
  "excluded_cluster_ids": [
    "324fs3r345vx-bb45we",
    "324fs3r345vx-cc67ui"
  ],
  "timestamp": "2026-01-14T12:40:56Z",
  "ere_request_id": "324fs3r345vxab:01"
}
 |

## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:EntityMentionResolutionRequest |
| native | ere:EntityMentionResolutionRequest |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EntityMentionResolutionRequest
description: 'An entity resolution request sent to the ERE, containing the entity
  to be resolved.

  '
examples:
- value: "{\n  \"type\": \"EntityMentionResolutionRequest\",\n  \"entity_mention\"\
    : { \n    \"identifier\": {\n      \"request_id\": \"324fs3r345vx\",\n      \"\
    source_id\": \"TEDSWS\",\n      \"entity_type\": \"http://www.w3.org/ns/org#Organization\"\
    \n    },\n    \"content\": \"epd:ent005 a org:Organization; ...   cccev:telephone\
    \ \\\"+44 1924306780\\\" .\",\n    \"content_type\": \"text/turtle\"\n  },\n \
    \ \"timestamp\": \"2026-01-14T12:34:56Z\",\n  // As said, we need this internal\
    \ ID and it can be auto-generated (eg, with UUIDs)\n  \"ere_request_id\": \"324fs3r345vx:01\"\
    \n}\n"
  description: a regular request
- value: "{\n  \"type\": \"EntityMentionResolutionRequest\",\n  \"entity_mention\"\
    : { \n    \"identifier\": {\n      \"request_id\": \"324fs3r345vxab\",\n     \
    \ \"source_id\": \"TEDSWS\",\n      \"entity_type\": \"http://www.w3.org/ns/org#Organization\"\
    ,\n    },\n    \"content\": \"epd:ent005 a org:Organization; ...   cccev:telephone\
    \ \\\"+44 1924306780\\\" .\",\n    \"content_type\": \"text/turtle\"\n  },\n \
    \ \"excluded_cluster_ids\": [\n    \"324fs3r345vx-bb45we\",\n    \"324fs3r345vx-cc67ui\"\
    \n  ],\n  \"timestamp\": \"2026-01-14T12:40:56Z\",\n  \"ere_request_id\": \"324fs3r345vxab:01\"\
    \n}\n"
  description: a re-rebuild request (ie, carrying a rejection list)
from_schema: https://data.europa.eu/ers/schema/ere
is_a: ERERequest
attributes:
  entity_mention:
    name: entity_mention
    description: 'The data about the entity to be resolved. Note that, at least for
      the moment, we don''t support

      batch requests, so this property is single-valued.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    domain_of:
    - EntityMentionResolutionRequest
    range: EntityMention
    required: true
  excluded_cluster_ids:
    name: excluded_cluster_ids
    description: "When this is present, the resolution must not bin the entity mention\
      \ into any of the\nlisted clusters. This can be used to reject a previous resolution\
      \ proposed by the ERE.\n\nThe exact reaction to this is implementation dependent.\
      \ In the simplest case, the ERE\nmight just create a singleton cluster with\
      \ this entity as member. In a more advanced \ncase, it might recompute the similarity\
      \ with more advanced algorithms or use updated\ndata.\n\nTODO: Can this be revised?\
      \ What does it happen if an exclusion was made by mistake?\n"
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    domain_of:
    - EntityMentionResolutionRequest
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: EntityMentionResolutionRequest
description: 'An entity resolution request sent to the ERE, containing the entity
  to be resolved.

  '
examples:
- value: "{\n  \"type\": \"EntityMentionResolutionRequest\",\n  \"entity_mention\"\
    : { \n    \"identifier\": {\n      \"request_id\": \"324fs3r345vx\",\n      \"\
    source_id\": \"TEDSWS\",\n      \"entity_type\": \"http://www.w3.org/ns/org#Organization\"\
    \n    },\n    \"content\": \"epd:ent005 a org:Organization; ...   cccev:telephone\
    \ \\\"+44 1924306780\\\" .\",\n    \"content_type\": \"text/turtle\"\n  },\n \
    \ \"timestamp\": \"2026-01-14T12:34:56Z\",\n  // As said, we need this internal\
    \ ID and it can be auto-generated (eg, with UUIDs)\n  \"ere_request_id\": \"324fs3r345vx:01\"\
    \n}\n"
  description: a regular request
- value: "{\n  \"type\": \"EntityMentionResolutionRequest\",\n  \"entity_mention\"\
    : { \n    \"identifier\": {\n      \"request_id\": \"324fs3r345vxab\",\n     \
    \ \"source_id\": \"TEDSWS\",\n      \"entity_type\": \"http://www.w3.org/ns/org#Organization\"\
    ,\n    },\n    \"content\": \"epd:ent005 a org:Organization; ...   cccev:telephone\
    \ \\\"+44 1924306780\\\" .\",\n    \"content_type\": \"text/turtle\"\n  },\n \
    \ \"excluded_cluster_ids\": [\n    \"324fs3r345vx-bb45we\",\n    \"324fs3r345vx-cc67ui\"\
    \n  ],\n  \"timestamp\": \"2026-01-14T12:40:56Z\",\n  \"ere_request_id\": \"324fs3r345vxab:01\"\
    \n}\n"
  description: a re-rebuild request (ie, carrying a rejection list)
from_schema: https://data.europa.eu/ers/schema/ere
is_a: ERERequest
attributes:
  entity_mention:
    name: entity_mention
    description: 'The data about the entity to be resolved. Note that, at least for
      the moment, we don''t support

      batch requests, so this property is single-valued.

      '
    from_schema: https://data.europa.eu/ers/schema/ere
    rank: 1000
    alias: entity_mention
    owner: EntityMentionResolutionRequest
    domain_of:
    - EntityMentionResolutionRequest
    range: EntityMention
    required: true
  excluded_cluster_ids:
    name: excluded_cluster_ids
    description: "When this is present, the resolution must not bin the entity mention\
      \ into any of the\nlisted clusters. This can be used to reject a previous resolution\
      \ proposed by the ERE.\n\nThe exact reaction to this is implementation dependent.\
      \ In the simplest case, the ERE\nmight just create a singleton cluster with\
      \ this entity as member. In a more advanced \ncase, it might recompute the similarity\
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
    owner: EntityMentionResolutionRequest
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
    owner: EntityMentionResolutionRequest
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
    owner: EntityMentionResolutionRequest
    domain_of:
    - EREMessage
    range: datetime

```
</details>