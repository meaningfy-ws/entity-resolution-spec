Feature: ERE/ERS request publishing — what ERE receives on its channel

  This feature defines what requests ERE can expect to receive on the ERE request channel,
  covering the standard resolution flow and the re-evaluation flow triggered by curator actions.


Scenario: A standard resolution request appears on the ERE request channel after an entity mention is submitted

  When an originator submits a new entity mention to ERS, ERS publishes a resolution request
  to the ERE request channel. ERE can rely on the request being correlated to the entity mention
  triad and carrying the entity mention content.

  Contract reference: see src/resources/schemas/ere-service-schema.yaml (EntityMentionResolutionRequest)

Given
  A valid entity mention with a known triad (source_id, request_id, entity_type) is submitted to ERS
When
  ERS processes the submission
Then
  A resolution request of type `EntityMentionResolutionRequest` appears on the ERE request channel
And
  The request is correlated to the submitted entity mention triad
And
  The request carries the entity mention content


Scenario: When ERE does not respond in time, no follow-up request is published automatically

  When ERS does not receive a response from ERE within the execution window (default: 30s),
  it issues a provisional draft identifier internally and returns it to the originator.
  No additional request is published to the ERE request channel at this point — ERE will not be
  notified of the timeout. A resolution request carrying `proposed_cluster_ids` only arrives later
  if a curator subsequently submits a placement recommendation for the provisional assignment
  (see Scenario 3).

Given
  A valid entity mention is submitted to ERS
And
  ERE does not respond within the ERS execution window
When
  The ERS execution window expires
Then
  No follow-up request is published to the ERE request channel
And
  ERE may later receive a resolution request carrying `proposed_cluster_ids` if a curator acts
  on the provisional assignment — but not before


Scenario Outline: A re-evaluation request appears on the ERE request channel after a curator submits a recommendation

  When a curator submits a re-evaluation recommendation for a previously resolved entity mention,
  ERS publishes a re-evaluation request to the ERE request channel. The curator interaction is the
  triggering context; the subject under test is the request that ERE receives.

  Contract reference: see src/resources/schemas/ere-service-schema.yaml (EntityMentionResolutionRequest)

Given
  An entity mention E has previously been resolved and a cluster assignment is available
And
  A curator has submitted a {recommendation_type} recommendation for E
When
  ERS publishes the resulting re-evaluation request
Then
  A re-evaluation request appears on the ERE request channel
And
  The request carries the {recommendation_type} interaction type

  Examples:
    | recommendation_type |
    | placement           |
    | exclusion           |
