Feature: ERE/ERS outcome integration — ERE-observable guarantees

  This feature defines what guarantees ERE can rely on when it emits resolution outcomes to ERS.
  It does not describe ERS-internal processing; it focuses on what ERE can observe or assume
  about how ERS handles its responses.


Scenario: Submitting the same outcome a second time produces no error

  ERE is permitted to re-send the same clustering outcome (duplicates can occur; the transport gives no delivery guarantee). ERS must
  accept duplicate outcomes silently.

Given
  ERE has already emitted a valid clustering outcome for an entity mention E
When
  ERE emits the same clustering outcome for E a second time
Then
  ERS accepts the message without raising an error
And
  The system continues to process subsequent outcomes normally


Scenario: An outcome for a mention that was never submitted is silently discarded

  ERE may emit outcomes that ERS has no record of (e.g. stale or cross-environment messages).
  ERS discards such outcomes without producing an error response, so ERE need not handle
  failure notifications for these cases.

Given
  No resolution request for entity mention E has ever been submitted to ERS
When
  ERE emits a clustering outcome for E
Then
  ERS discards the outcome without raising an error
And
  No error message is sent back to ERE


Scenario: An ERE-initiated reclustering outcome is accepted

  ERE may proactively emit reclustering outcomes (with `ere_request_id` using the
  `ereNotification:` prefix) without a prior ERS request. ERS must accept such outcomes.

Given
  ERE emits a reclustering outcome for an entity mention E with an `ere_request_id`
  using the `ereNotification:` prefix
When
  The outcome is delivered to the ERS response channel
Then
  ERS accepts the outcome without raising an error and subsequently updates its internal state
