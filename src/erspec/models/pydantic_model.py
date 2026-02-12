from dataclasses import dataclass
from typing import Any, Optional, TypeVar, cast

from pydantic import BaseModel, ConfigDict, Field


class PydanticModel(BaseModel):
    """Base model class with core configurations for all domain models."""

    object_description: Optional[str] = Field(
        default=None,
        exclude=True,
        description="Optional descriptive text for the model instance.",
    )

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
        frozen=False,
        arbitrary_types_allowed=False,
        use_enum_values=True,
        str_strip_whitespace=False,
        validate_default=True,
        populate_by_name=True,
        ser_json_bytes="base64",
    )


@dataclass(frozen=True)
class _GetFields:
    _model: type[BaseModel]

    def __getattr__(self, item: str) -> Any:
        if item in self._model.model_fields:
            return item
        return getattr(self._model, item)


TModel = TypeVar("TModel", bound=PydanticModel)


def fields(model: type[TModel], /) -> TModel:
    """Type-safe field name accessor for Pydantic models."""
    return cast(TModel, _GetFields(model))
