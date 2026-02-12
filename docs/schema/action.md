

# Slot: action 



URI: [ere:action](https://data.europa.eu/ers/schema/ere/action)
Alias: action

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
| self | ere:action |
| native | ere:action |




## LinkML Source

<details>
```yaml
name: action
alias: action
domain_of:
- Decision
- AuditLog
range: string

```
</details>