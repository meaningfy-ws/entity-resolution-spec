# Enum: AuditAction 




_Actions recorded in the audit log_



URI: [ere:AuditAction](https://data.europa.eu/ers/schema/ere/AuditAction)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ACCEPT | None | Accept action performed |
| REJECT | None | Reject action performed |
| ASSIGN | None | Assign to alternative cluster action performed |








## Identifier and Mapping Information






### Schema Source


* from schema: https://data.europa.eu/ers/schema/ere






## LinkML Source

<details>
```yaml
name: AuditAction
description: Actions recorded in the audit log
from_schema: https://data.europa.eu/ers/schema/ere
rank: 1000
permissible_values:
  ACCEPT:
    text: ACCEPT
    description: Accept action performed
  REJECT:
    text: REJECT
    description: Reject action performed
  ASSIGN:
    text: ASSIGN
    description: Assign to alternative cluster action performed

```
</details>