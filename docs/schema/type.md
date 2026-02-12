

# Slot: type 


_The type of the request or result._

__

_As per LinkML specification, `designates_type` is used here in order to allow for this_

_slot to tell the concrete subclass that an instance (such as a JSON object) belongs to._

__

_In other words, a particular request will have `type` set with values like _

_`EntityMentionResolutionRequest` or `EntityResolutionResult`_

__





URI: [ere:type](https://data.europa.eu/ers/schema/ere/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |
| [EREMessage](EREMessage.md) | Root abstraction to represent attributes common to both requests and results |  no  |
| [FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and possibly rebuild t... |  no  |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |  no  |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [FullRebuildResponse](FullRebuildResponse.md) | A response to a `FullRebuildRequest`, confirming that the rebuild process has... |  no  |
| [EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:type |
| native | ere:type |




## LinkML Source

<details>
```yaml
name: type
description: "The type of the request or result.\n\nAs per LinkML specification, `designates_type`\
  \ is used here in order to allow for this\nslot to tell the concrete subclass that\
  \ an instance (such as a JSON object) belongs to.\n\nIn other words, a particular\
  \ request will have `type` set with values like \n`EntityMentionResolutionRequest`\
  \ or `EntityResolutionResult`\n"
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
designates_type: true
alias: type
owner: EREMessage
domain_of:
- EREMessage
range: string
required: true

```
</details>