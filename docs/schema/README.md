# ereServiceSchema

A LinkML schema for the ERS/ERE Service

URI: https://data.europa.eu/ers/schema/ere

Name: ereServiceSchema



## Classes

| Class | Description |
| --- | --- |
| [AuditLog](AuditLog.md) | Audit trail entry for curation actions |
| [CanonicalEntity](CanonicalEntity.md) | A logical identity construct providing a stable identity anchor |
| [ClusterReference](ClusterReference.md) | A reference to a cluster to which an entity is deemed to belong, with an asso... |
| [Decision](Decision.md) | Aggregate root representing a resolution decision requiring curation |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity, as provided by ... |
| [EntityMentionIdentifier](EntityMentionIdentifier.md) | A container that groups the attributes needed to identify an entity mention i... |
| [EREMessage](EREMessage.md) | Root abstraction to represent attributes common to both requests and results |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FullRebuildRequest](FullRebuildRequest.md) | A request to reset all the resolutions computed so far and possibly rebuild t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FullRebuildResponse](FullRebuildResponse.md) | A response to a `FullRebuildRequest`, confirming that the rebuild process has... |



## Slots

| Slot | Description |
| --- | --- |
| [about_entity_mention](about_entity_mention.md) | Reference to the entity mention being resolved |
| [accepted_candidate](accepted_candidate.md) | The cluster reference accepted for this entity mention |
| [action](action.md) | Action taken by curator |
| [actor](actor.md) | User identifier who performed the action |
| [candidates](candidates.md) | The set of cluster reference/score pairs representing the candidate clusters |
| [changes](changes.md) | JSON representation of action-specific context |
| [cluster_id](cluster_id.md) | The identifier of the cluster/canonical entity that is considered equivalent ... |
| [confidence_score](confidence_score.md) | A 0-1 value of how confident the ERE is about the equivalence between the sub... |
| [content](content.md) | A code string representing the entity mention details (eg, RDF or XML descrip... |
| [content_type](content_type.md) | A string about the MIME format of `content` (e |
| [created_at](created_at.md) | Timestamp when the decision was created |
| [entity_mention](entity_mention.md) | The data about the entity to be resolved |
| [entity_mention_id](entity_mention_id.md) | The identifier of the entity mention that has been resolved |
| [entity_type](entity_type.md) | A string representing the entity type (based on CET) |
| [equivalent_to](equivalent_to.md) | Entity mentions that have been resolved to this canonical entity |
| [ere_request_id](ere_request_id.md) | A string representing the unique ID of an ERE request, or the ID of the reque... |
| [error_detail](error_detail.md) | A human readable detailed message about the error that occurred |
| [error_title](error_title.md) | A human readable brief message about the error that occurred |
| [error_trace](error_trace.md) | A string representing a (stack) trace of the error that occurred |
| [error_type](error_type.md) | A string representing the error type, eg, the FQN of the raised exception |
| [excluded_cluster_ids](excluded_cluster_ids.md) | When this is present, the resolution must not bin the entity mention into any... |
| [id](id.md) | Unique identifier for the decision |
| [identifier](identifier.md) | Unique identifier for the canonical entity |
| [instance_id](instance_id.md) | Identifier of the modified entity |
| [instance_type](instance_type.md) | Type of entity being modified (e |
| [parsed_representation](parsed_representation.md) | JSON representation of the parsed entity data |
| [request_id](request_id.md) | A string representing the unique ID of the request made to the ERS system |
| [source_id](source_id.md) | The ID or URI of the ERS client that originated the request |
| [status](status.md) | Current status in the curation workflow |
| [timestamp](timestamp.md) | The time when the message was created |
| [type](type.md) | The type of the request or result |
| [updated_at](updated_at.md) | Timestamp when the decision was last updated |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AuditAction](AuditAction.md) | Actions recorded in the audit log |
| [DecisionAction](DecisionAction.md) | Action taken on a decision by the curator |
| [DecisionStatus](DecisionStatus.md) | Status of a resolution decision in the curation workflow |
| [EntityType](EntityType.md) | Types of entities that can be resolved |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
