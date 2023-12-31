from __future__ import annotations
from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from discord import RawAppCommandPermissionsUpdateEvent as RawAppCommandPermissionsUpdateEventPayload, Interaction

__all__ = (
    "RawApplicationCommandPermissionsUpdateEvent",
    "ApplicationCommandCompletionEvent",
)


# on_raw_app_command_permissions_update
class RawApplicationCommandPermissionsUpdateEvent(Protocol):
    async def __call__(self, payload: RawAppCommandPermissionsUpdateEventPayload) -> Any:
        ...


# on_app_command_completion
class ApplicationCommandCompletionEvent(Protocol):
    async def __call__(self, interaction: Interaction[Any]) -> Any:
        ...
