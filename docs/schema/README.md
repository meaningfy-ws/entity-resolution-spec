# ereServiceSchema

A LinkML schema for the ERS/ERE Service

URI: https://data.europa.eu/ers/schema/ere

Name: ereServiceSchema



## Classes

| Class | Description |
| --- | --- |
| [CanonicalEntityIdentifier](CanonicalEntityIdentifier.md) | A logical identity construct providing a stable identity anchor |
| [ClusterReference](ClusterReference.md) | A reference to a cluster to which an entity is deemed to belong, with an asso... |
| [Decision](Decision.md) | Canonical placement of an entity mention to a cluster |
| [EntityMention](EntityMention.md) | An entity mention is a representation of a real-world entity, as provided by ... |
| [EntityMentionIdentifier](EntityMentionIdentifier.md) | A container that groups the attributes needed to identify an entity mention i... |
| [EREMessage](EREMessage.md) | Root abstraction to represent attributes common to both requests and results |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ERERequest](ERERequest.md) | Root class to represent all the requests sent to the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityMentionResolutionRequest](EntityMentionResolutionRequest.md) | An entity resolution request sent to the ERE, containing the entity to be res... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EREResponse](EREResponse.md) | Root class to represent all the responses sent by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityMentionResolutionResponse](EntityMentionResolutionResponse.md) | An entity resolution response returned by the ERE |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EREErrorResponse](EREErrorResponse.md) | Response sent by the ERE when some error/exception occurs while processing a ... |
| [LookupState](LookupState.md) | Tracks the resolution state for entity mentions from a particular source |
| [UserAction](UserAction.md) | Immutable record of a curator action on an entity mention resolution |



## Slots

| Slot | Description |
| --- | --- |
| [about_entity_mention](about_entity_mention.md) | The entity mention being resolved |
| [action_type](action_type.md) | The type of action the curator performed |
| [actor](actor.md) | User ID or identifier of the curator who performed the action |
| [candidates](candidates.md) | The set of cluster reference/score pairs representing the candidate clusters |
| [cluster_id](cluster_id.md) | The identifier of the cluster/canonical entity that is considered equivalent ... |
| [confidence_score](confidence_score.md) | A 0-1 value of how confident the ERE is about the equivalence between the sub... |
| [content](content.md) | A code string representing the entity mention details (eg, RDF or XML descrip... |
| [content_type](content_type.md) | A string about the MIME format of `content` (e |
| [context](context.md) | Optional context reference (e |
| [created_at](created_at.md) | When the decision was first created |
| [current_placement](current_placement.md) | The accepted cluster for this mention (latest from ERE or curator) |
| [entity_mention](entity_mention.md) | The data about the entity to be resolved |
| [entity_mention_id](entity_mention_id.md) | The identifier of the entity mention that has been resolved |
| [entity_type](entity_type.md) | A string representing the entity type (based on CET) |
| [equivalent_to](equivalent_to.md) | Entity mentions that have been resolved to this canonical entity |
| [ere_request_id](ere_request_id.md) | A string representing the unique ID of an ERE request, or the ID of the reque... |
| [error_detail](error_detail.md) | A human readable detailed message about the error that occurred |
| [error_title](error_title.md) | A human readable brief message about the error that occurred |
| [error_trace](error_trace.md) | A string representing a (stack) trace of the error that occurred |
| [error_type](error_type.md) | A string representing the error type, for example the name or the fully quali... |
| [excluded_cluster_ids](excluded_cluster_ids.md) | When this is present, the ERE may use this information to avoid clustering th... |
| [id](id.md) | Unique decision identifier |
| [identifiedBy](identifiedBy.md) | The identification triad of the entity mention |
| [identifier](identifier.md) | Unique identifier for the canonical entity |
| [last_snapshot](last_snapshot.md) | Timestamp of the last resolution operation for this source |
| [metadata](metadata.md) | JSON metadata providing context (e |
| [parsed_representation](parsed_representation.md) | JSON representation of the parsed entity data |
| [proposed_cluster_ids](proposed_cluster_ids.md) | When this is present, the ERE may use this information to try to cluster the ... |
| [request_id](request_id.md) | A string representing the unique ID of the request made to the ERS system |
| [selected_cluster](selected_cluster.md) | The cluster selected by the curator (if action was ACCEPT_TOP |
| [similarity_score](similarity_score.md) | A 0-1 score representing the pairwise comparison between a mention and a clus... |
| [source_id](source_id.md) | The ID or URI of the ERS client that originated the request |
| [timestamp](timestamp.md) | The time when the message was created |
| [type](type.md) | The type of the request or result |
| [updated_at](updated_at.md) | When the decision was last updated (ERE refresh or curator action) |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [UserActionType](UserActionType.md) | Types of curator actions on entity mention resolutions |


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
