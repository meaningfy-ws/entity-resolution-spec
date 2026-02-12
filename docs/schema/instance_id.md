

# Slot: instance_id 


_Identifier of the modified entity_





URI: [ere:instance_id](https://data.europa.eu/ers/schema/ere/instance_id)
Alias: instance_id

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
| self | ere:instance_id |
| native | ere:instance_id |




## LinkML Source

<details>
```yaml
name: instance_id
description: Identifier of the modified entity
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: instance_id
owner: AuditLog
domain_of:
- AuditLog
range: string
required: true

```
</details>