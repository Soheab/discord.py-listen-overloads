from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord import StageInstance


__all__ = (
    "StageInstanceEvent",
    "StageInstanceUpdateEvent",
)


# on_stage_instance_create
# on_stage_instance_delete
class StageInstanceEvent(Protocol):
    async def __call__(self, stage_instance: StageInstance) -> Any:
        ...


# on_stage_instance_update
class StageInstanceUpdateEvent(Protocol):
    async def __call__(self, before: StageInstance, after: StageInstance) -> Any:
        ...
