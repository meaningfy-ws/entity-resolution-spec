

# Slot: error_detail 


_A human readable detailed message about the error that occurred._

__

_This corresponds to RFC-9457's `detail`._

__





URI: [ere:error_detail](https://data.europa.eu/ers/schema/ere/error_detail)
Alias: error_detail

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
| self | ere:error_detail |
| native | ere:error_detail |




## LinkML Source

<details>
```yaml
name: error_detail
description: 'A human readable detailed message about the error that occurred.


  This corresponds to RFC-9457''s `detail`.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: error_detail
owner: EREErrorResponse
domain_of:
- EREErrorResponse
range: string

```
</details>