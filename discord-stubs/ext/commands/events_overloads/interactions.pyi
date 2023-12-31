from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord import Interaction


__all__ = ("InteractionEvent",)


# on_interaction
class InteractionEvent(Protocol):
    async def __call__(self, interaction: Interaction[Any]) -> Any:
        ...
