

# Slot: error_title 


_A human readable brief message about the error that occurred._

__

_This corresponds to RFC-9457's `title`._

__





URI: [ere:error_title](https://data.europa.eu/ers/schema/ere/error_title)
Alias: error_title

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
| self | ere:error_title |
| native | ere:error_title |




## LinkML Source

<details>
```yaml
name: error_title
description: 'A human readable brief message about the error that occurred.


  This corresponds to RFC-9457''s `title`.

  '
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: error_title
owner: EREErrorResponse
domain_of:
- EREErrorResponse
range: string

```
</details>