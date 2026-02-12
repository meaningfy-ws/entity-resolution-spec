

# Slot: error_type 


_A string representing the error type, eg, the FQN of the raised exception._

__

_This corresponds to RFC-9457's `type`._

__





URI: [ere:error_type](https://data.europa.eu/ers/schema/ere/error_type)
Alias: error_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:error_type |
| native | ere:error_type |




## LinkML Source

<details>
```yaml
name: error_type
description: 'A string representing the error type, eg, the FQN of the raised exception.


  This corresponds to RFC-9457''s `type`.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: error_type
owner: EREErrorResponse
domain_of:
- EREErrorResponse
range: string
required: true

```
</details>