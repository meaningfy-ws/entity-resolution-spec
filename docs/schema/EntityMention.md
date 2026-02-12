

# Class: EntityMention 


_An entity mention is a representation of a real-world entity, as provided by the ERS._

_It contains the entity data, along with metadata like type and format._

__





URI: [ere:EntityMention](https://data.europa.eu/ers/schema/ere/EntityMention)





```mermaid
 classDiagram
    class EntityMention
    click EntityMention href "../EntityMention/"
      EntityMention : content
        
      EntityMention : content_type
        
      EntityMention : identifier
        
          
    
        
        
        EntityMention --> "1" EntityMentionIdentifier : identifier
        click EntityMentionIdentifier href "../EntityMentionIdentifier/"
    

        
      EntityMention : parsed_representation
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [identifier](identifier.md) | 1 <br/> [EntityMentionIdentifier](EntityMentionIdentifier.md) | The identifier (with the ERS-derived components) of the entity mention | direct |
| [content_type](content_type.md) | 1 <br/> [String](String.md) | A string about the MIME format of `content` (e | direct |
| [content](content.md) | 1 <br/> [String](String.md) | A code string representing the entity mention details (eg, RDF or XML descrip... | direct |
| [parsed_representation](parsed_representation.md) | 0..1 <br/> [String](String.md) | JSON representation of the parsed entity data | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | [entity_mention](entity_mention.md) | range | [EntityMention](EntityMention.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:EntityMention |
| native | ere:EntityMention |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EntityMention
description: 'An entity mention is a representation of a real-world entity, as provided
  by the ERS.

  It contains the entity data, along with metadata like type and format.

  '
from_schema: https://data.europa.eu/ers/schema/ere
attributes:
  identifier:
    name: identifier
    description: 'The identifier (with the ERS-derived components) of the entity mention.

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    domain_of:
    - CanonicalEntity
    - EntityMention
    range: EntityMentionIdentifier
    required: true
  content_type:
    name: content_type
    description: 'A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    domain_of:
    - EntityMention
    required: true
  content:
    name: content
    description: 'A code string representing the entity mention details (eg, RDF or
      XML description).

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    domain_of:
    - EntityMention
    required: true
  parsed_representation:
    name: parsed_representation
    description: 'JSON representation of the parsed entity data.

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    domain_of:
    - EntityMention

```
</details>

### Induced

<details>
```yaml
name: EntityMention
description: 'An entity mention is a representation of a real-world entity, as provided
  by the ERS.

  It contains the entity data, along with metadata like type and format.

  '
from_schema: https://data.europa.eu/ers/schema/ere
attributes:
  identifier:
    name: identifier
    description: 'The identifier (with the ERS-derived components) of the entity mention.

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    alias: identifier
    owner: EntityMention
    domain_of:
    - CanonicalEntity
    - EntityMention
    range: EntityMentionIdentifier
    required: true
  content_type:
    name: content_type
    description: 'A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    alias: content_type
    owner: EntityMention
    domain_of:
    - EntityMention
    range: string
    required: true
  content:
    name: content
    description: 'A code string representing the entity mention details (eg, RDF or
      XML description).

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    alias: content
    owner: EntityMention
    domain_of:
    - EntityMention
    range: string
    required: true
  parsed_representation:
    name: parsed_representation
    description: 'JSON representation of the parsed entity data.

      '
    from_schema: https://data.europa.eu/ers/schema/ers
    rank: 1000
    alias: parsed_representation
    owner: EntityMention
    domain_of:
    - EntityMention
    range: string

```
</details>