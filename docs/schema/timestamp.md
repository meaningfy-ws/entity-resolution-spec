

# Slot: timestamp 


_The time when the message was created. Should be in ISO-8601 format._

__





URI: [ere:timestamp](https://data.europa.eu/ers/schema/ere/timestamp)
Alias: timestamp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |  no  |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |
| [ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |  no  |
| [EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |  no  |
| [EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |  no  |
| [EREMessage](EREMessage.md) | Root abstraction to represent attributes common to both requests and results |  no  |
| [FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and possibly rebuild t... |  no  |
| [FullRebuildResponse](FullRebuildResponse.md) | A response to a `FullRebuildRequest`, confirming that the rebuild process has... |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:timestamp |
| native | ere:timestamp |




## LinkML Source

<details>
```yaml
name: timestamp
description: 'The time when the message was created. Should be in ISO-8601 format.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: timestamp
owner: EREMessage
domain_of:
- EREMessage
range: datetime

```
</details>