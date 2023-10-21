from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord import Member, VoiceState


__all__ = ("VoiceStateUpdateEvent",)


# on_voice_state_update
class VoiceStateUpdateEvent(Protocol):
    async def __call__(self, member: Member, before: VoiceState, after: VoiceState) -> Any:
        ...
