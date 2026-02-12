

# Slot: error_trace 


_A string representing a (stack) trace of the error that occurred._

__

_This is optional and typically used for debugging purposes only, since_

_exposing this kind of server-side information is a security risk._

__





URI: [ere:error_trace](https://data.europa.eu/ers/schema/ere/error_trace)
Alias: error_trace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:error_trace |
| native | ere:error_trace |




## LinkML Source

<details>
```yaml
name: error_trace
description: 'A string representing a (stack) trace of the error that occurred.


  This is optional and typically used for debugging purposes only, since

  exposing this kind of server-side information is a security risk.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: error_trace
owner: EREErrorResponse
domain_of:
- EREErrorResponse
range: string

```
</details>