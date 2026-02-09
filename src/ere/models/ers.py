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

from .core import (
    ClusterReference,
    EntityMentionIdentifier
)

from ere.models.pydantic_model import PydanticModel


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



class Decision(PydanticModel):
    """Aggregate root representing a resolution decision requiring curation.
Captures the state and outcome of entity mention resolution."""
    id: str = Field(default=..., description="""Unique identifier for the decision""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    aboutEntityMention: EntityMentionIdentifier = Field(default=..., description="""Reference to the entity mention being resolved""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    status: DecisionStatus = Field(default=..., description="""Current status in the curation workflow""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    action: Optional[DecisionAction] = Field(default=None, description="""Action taken by curator (if any)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    acceptedCandidate: Optional[ClusterReference] = Field(default=None, description="""The cluster reference accepted for this entity mention""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    candidates: list[ClusterReference] = Field(default=..., description="""All cluster references proposed by ERE, ordered by confidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['EntityMentionResolutionResponse', 'Decision']} })
    createdAt: datetime  = Field(default=..., description="""Timestamp when the decision was created""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    updatedAt: Optional[datetime ] = Field(default=None, description="""Timestamp when the decision was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })


class AuditLog(PydanticModel):
    """Audit trail entry for curation actions"""
    id: str = Field(default=..., description="""Unique identifier for the audit entry""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    actor: str = Field(default=..., description="""User identifier who performed the action""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditLog']} })
    action: AuditAction = Field(default=..., description="""The action performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })
    instanceType: str = Field(default=..., description="""Type of entity being modified (e.g., Decision)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditLog']} })
    instanceId: str = Field(default=..., description="""Identifier of the modified entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditLog']} })
    changes: Optional[str] = Field(default=None, description="""JSON representation of action-specific context""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuditLog']} })
    createdAt: datetime  = Field(default=..., description="""Timestamp when the action was performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'AuditLog']} })

