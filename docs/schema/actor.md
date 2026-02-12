

# Slot: actor 


_User identifier who performed the action_





URI: [ere:actor](https://data.europa.eu/ers/schema/ere/actor)
Alias: actor

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
| self | ere:actor |
| native | ere:actor |




## LinkML Source

<details>
```yaml
name: actor
description: User identifier who performed the action
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
alias: actor
owner: AuditLog
domain_of:
- AuditLog
range: string
required: true

```
</details>