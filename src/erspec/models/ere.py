from __future__ import annotations 

from datetime import (
    datetime
)
from enum import Enum 
from typing import (
    Literal,
    Optional
)

from pydantic import (
    Field
)

from .core import (
    ClusterReference,
    EntityMention,
    EntityMentionIdentifier
)

from erspec.models.pydantic_model import PydanticModel


metamodel_version = "None"
version = "0.1.0"


class EntityType(str, Enum):
    """
    Types of entities that can be resolved
    """
    ORGANISATION = "ORGANISATION"
    """
    An organization entity
    """
    PROCEDURE = "PROCEDURE"
    """
    A procurement procedure entity
    """


class DecisionStatus(str, Enum):
    """
    Status of a resolution decision in the curation workflow
    """
    AUTOMATIC_CONFIDENT = "AUTOMATIC_CONFIDENT"
    """
    Resolution confidence exceeds threshold; no manual review required
    """
    PENDING_MANUAL_REVIEW = "PENDING_MANUAL_REVIEW"
    """
    Resolution confidence below threshold; awaiting curator action
    """
    MANUALLY_REVIEWED = "MANUALLY_REVIEWED"
    """
    Curator has taken an action
    """


class DecisionAction(str, Enum):
    """
    Action taken on a decision by the curator
    """
    ACCEPT_TOP = "ACCEPT_TOP"
    """
    Curator accepted the top candidate
    """
    ACCEPT_ALTERNATIVE = "ACCEPT_ALTERNATIVE"
    """
    Curator selected an alternative candidate
    """
    REJECT_ALL = "REJECT_ALL"
    """
    Curator rejected all candidates
    """


class AuditAction(str, Enum):
    """
    Actions recorded in the audit log
    """
    ACCEPT = "ACCEPT"
    """
    Accept action performed
    """
    REJECT = "REJECT"
    """
    Reject action performed
    """
    ASSIGN = "ASSIGN"
    """
    Assign to alternative cluster action performed
    """



class EREMessage(PydanticModel):
    """Root abstraction to represent attributes common to both requests and results.
This is modelled as a mixin in LinkML (so that it can't be instantiated directly)."""
    type: Literal["EREMessage"] = Field(default="EREMessage", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class ERERequest(EREMessage):
    """Root class to represent all the requests sent to the ERE."""
    type: Literal["ERERequest"] = Field(default="ERERequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EREResponse(EREMessage):
    """Root class to represent all the responses sent by the ERE."""
    type: Literal["EREResponse"] = Field(default="EREResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EntityMentionResolutionRequest(ERERequest):
    """An entity resolution request sent to the ERE, containing the entity to be resolved."""
    entity_mention: EntityMention = Field(default=..., description="""The data about the entity to be resolved. Note that, at least for the moment, we don't support
batch requests, so this property is single-valued.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    excluded_cluster_ids: Optional[list[str]] = Field(default=[], description="""When this is present, the resolution must not bin the entity mention into any of the
listed clusters. This can be used to reject a previous resolution proposed by the ERE.

The exact reaction to this is implementation dependent. In the simplest case, the ERE
might just create a singleton cluster with this entity as member. In a more advanced 
case, it might recompute the similarity with more advanced algorithms or use updated
data.

TODO: Can this be revised? What does it happen if an exclusion was made by mistake?
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionRequest']} })
    type: Literal["EntityMentionResolutionRequest"] = Field(default="EntityMentionResolutionRequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EntityMentionResolutionResponse(EREResponse):
    """An entity resolution response returned by the ERE.

This is basically a list of candidate clusters to which the entity is deemed to be equivalent.

Note that, for the moment, we don't support batch requests. In future, we might support requests
with multiple subjects in the `EntityMention` content (eg, RDF with multiple subjects), in which case 
we might need to return multiple `EntityMentionResolutionResponse` messages, each with additional 
properties such as `entityIndex` and `totalEntities`."""
    entity_mention_id: EntityMentionIdentifier = Field(default=..., description="""The identifier of the entity mention that has been resolved.

This isn't strictly needed, since the `ere_request_id` already links the response to 
the request's entity mention. Yet, it's reported for convenience.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionResponse']} })
    candidates: list[ClusterReference] = Field(default=..., description="""The set of cluster reference/score pairs representing the candidate clusters
that the entity mention in the original request could align to (be equivalent to).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'EntityMentionResolutionResponse']} })
    type: Literal["EntityMentionResolutionResponse"] = Field(default="EntityMentionResolutionResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class EREErrorResponse(EREResponse):
    """Response sent by the ERE when some error/exception occurs while processing a request.
For instance, this may happen if the request is malformed or some internal error happens.

The attributes of this class are based on [RFC-9457](https://datatracker.ietf.org/doc/html/rfc9457)."""
    error_type: str = Field(default=..., description="""A string representing the error type, eg, the FQN of the raised exception.

This corresponds to RFC-9457's `type`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    error_title: Optional[str] = Field(default=None, description="""A human readable brief message about the error that occurred.

This corresponds to RFC-9457's `title`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    error_detail: Optional[str] = Field(default=None, description="""A human readable detailed message about the error that occurred.

This corresponds to RFC-9457's `detail`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    error_trace: Optional[str] = Field(default=None, description="""A string representing a (stack) trace of the error that occurred.

This is optional and typically used for debugging purposes only, since
exposing this kind of server-side information is a security risk.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREErrorResponse']} })
    type: Literal["EREErrorResponse"] = Field(default="EREErrorResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class FullRebuildRequest(ERERequest):
    """A request to reset all the resolutions computed so far and possibly rebuild them as 
requests about old entities arrive again (and build new entities from scratch as usually).

It is expected that the ERE client re-sends all the entities to be resolved again,
using `EntityMentionResolutionRequest` messages exactly as the first time the resolutions 
were built. This implies the a client like the ERS logs/persists the entities it receives
to resolve and also saves manual overriding of ERE results.

Moreover:
* The ERE must keep track of past `EntityMention` marked as canonical.
* The ERE must retain requests with `excluded_cluster_ids` and apply them again when the 
  same entity mention is re-sent after the full rebuild. TODO: see notes about these properties,
  on the possible need of withdrawing exclusions."""
    type: Literal["FullRebuildRequest"] = Field(default="FullRebuildRequest", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })


class FullRebuildResponse(EREResponse):
    """A response to a `FullRebuildRequest`, confirming that the rebuild process has started.

As for all the requests, this carries the `ere_request_id`, which matches the full rebuild 
request being acknowledged."""
    type: Literal["FullRebuildResponse"] = Field(default="FullRebuildResponse", description="""The type of the request or result.

As per LinkML specification, `designates_type` is used here in order to allow for this
slot to tell the concrete subclass that an instance (such as a JSON object) belongs to.

In other words, a particular request will have `type` set with values like 
`EntityMentionResolutionRequest` or `EntityResolutionResult`
""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['EREMessage']} })
    ere_request_id: str = Field(default=..., description="""A string representing the unique ID of an ERE request, or the ID of the request a response is about.
This **is not** the same as `request_id` + `source_id`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })
    timestamp: Optional[datetime ] = Field(default=None, description="""The time when the message was created. Should be in ISO-8601 format.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EREMessage']} })

