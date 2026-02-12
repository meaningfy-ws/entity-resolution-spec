

# Slot: created_at 



URI: [ere:created_at](https://data.europa.eu/ers/schema/ere/created_at)
Alias: created_at

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Aggregate root representing a resolution decision requiring curation |  no  |
| [AuditLog](AuditLog.md) | Audit trail entry for curation actions |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ere:created_at |
| native | ere:created_at |




## LinkML Source

<details>
```yaml
name: created_at
alias: created_at
domain_of:
- Decision
- AuditLog
range: string

```
</details>