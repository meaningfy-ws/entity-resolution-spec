

# Slot: instance_type 


_Type of entity being modified (e.g., Decision)_





URI: [ere:instance_type](https://data.europa.eu/ers/schema/ere/instance_type)
Alias: instance_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AuditLog](AuditLog.md) | Audit trail entry for curation actions |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:instance_type |
| native | ere:instance_type |




## LinkML Source

<details>
```yaml
name: instance_type
description: Type of entity being modified (e.g., Decision)
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: instance_type
owner: AuditLog
domain_of:
- AuditLog
range: string
required: true

```
</details>