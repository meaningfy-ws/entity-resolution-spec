from __future__ import annotations 

from datetime import (
    datetime
)
from enum import Enum 
from typing import (
    Optional
)

from pydantic import (
    Field
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



class CanonicalEntityIdentifier(PydanticModel):
    """A logical identity construct providing a stable identity anchor.
Represents a cluster of equivalent entity mentions."""
    identifier: str = Field(default=..., description="""Unique identifier for the canonical entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntityIdentifier', 'EntityMention']} })
    equivalent_to: list[EntityMentionIdentifier] = Field(default=..., description="""Entity mentions that have been resolved to this canonical entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntityIdentifier']} })


class EntityMention(PydanticModel):
    """An entity mention is a representation of a real-world entity, as provided by the ERS.
It contains the entity data, along with metadata like type and format."""
    identifier: EntityMentionIdentifier = Field(default=..., description="""The identifier (with the ERS-derived components) of the entity mention.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CanonicalEntityIdentifier', 'EntityMention']} })
    content_type: str = Field(default=..., description="""A string about the MIME format of `content` (e.g. text/turtle, application/ld+json)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    content: str = Field(default=..., description="""A code string representing the entity mention details (eg, RDF or XML description).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })
    parsed_representation: Optional[str] = Field(default=None, description="""JSON representation of the parsed entity data.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMention']} })


class EntityMentionIdentifier(PydanticModel):
    """A container that groups the attributes needed to identify an entity mention in a resolution request
or response.

As per ERS architectural decision, in the whole ERS and ERE systems, there is always a deterministic
method to build a canonical identifier from the combination of `sourceId`, `requestId` and `entityType`
(eg, string concatenation plus some prefix). Similarly, a cluster ID (mentioned in various places in 
in this hereby ERE service schema) can be built from an entity that is initially the only cluster member."""
    source_id: str = Field(default=..., description="""The ID or URI of the ERS client that originated the request. This identifies an application or a 
person accessing the ERS system.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifier']} })
    request_id: str = Field(default=..., description="""A string representing the unique ID of the request made to the ERS system. In general, this is unique
only within the scope of the source and the entity type, ie, within `sourceId` and `entityType`. 

Moreover, this is **not** the same as `ereRequestId`, which instead, is internal to the ERE and is 
used to match responses to requests.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifier']} })
    entity_type: str = Field(default=..., description="""A string representing the entity type (based on CET). This is typically a URI.

Note that this is at this level, and not at `EntityMention`, since, as said above, 
it's needed to identify the entity, even when its content is not present. For the same
reason, it's used both for `EREResolutionRequest` and `EREResolutionResponse` messages.,
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionIdentifier']} })


class ClusterReference(PydanticModel):
    """A reference to a cluster to which an entity is deemed to belong, with an associated confidence score.

A cluster is a set of entity mentions that have been determined to refer to the same real-world entity.
Each cluster has a unique clusterId.

A cluster reference is used to report the association between an entity mention and a cluster 
of equivalence."""
    cluster_id: str = Field(default=..., description="""The identifier of the cluster/canonical entity that is considered equivalent to the
subject entity mention that an `EntityMentionResolutionResponse` refers to.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClusterReference']} })
    confidence_score: float = Field(default=..., description="""A 0-1 value of how confident the ERE is about the equivalence between the subject entity mention
and the target canonical entity.
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['ClusterReference']} })


class Decision(PydanticModel):
    """Aggregate root representing a resolution decision requiring curation.
Captures the state and outcome of entity mention resolution."""
    id: str = Field(default=..., description="""Unique identifier for the decision""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    about_entity_mention: EntityMentionIdentifier = Field(default=..., description="""Reference to the entity mention being resolved""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    status: DecisionStatus = Field(default=..., description="""Current status in the curation workflow""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    action: Optional[DecisionAction] = Field(default=None, description="""Action taken by curator""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    accepted_candidate: Optional[ClusterReference] = Field(default=None, description="""The cluster reference accepted for this entity mention""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    candidates: list[ClusterReference] = Field(default=..., description="""All cluster references proposed by ERE, ordered by confidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'EntityMentionResolutionResponse']} })
    created_at: datetime  = Field(default=..., description="""Timestamp when the decision was created""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    updated_at: Optional[datetime ] = Field(default=None, description="""Timestamp when the decision was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })


class AuditLog(PydanticModel):
    """Audit trail entry for curation actions"""
    id: str = Field(default=..., description="""Unique identifier for the audit entry""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    actor: str = Field(default=..., description="""User identifier who performed the action""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditLog']} })
    action: AuditAction = Field(default=..., description="""The action performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    instance_type: str = Field(default=..., description="""Type of entity being modified (e.g., Decision)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditLog']} })
    instance_id: str = Field(default=..., description="""Identifier of the modified entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditLog']} })
    changes: Optional[str] = Field(default=None, description="""JSON representation of action-specific context""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditLog']} })
    created_at: datetime  = Field(default=..., description="""Timestamp when the action was performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })

