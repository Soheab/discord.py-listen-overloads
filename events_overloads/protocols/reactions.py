from __future__ import annotations
from typing import Any, TYPE_CHECKING, Union, List, Protocol

if TYPE_CHECKING:
    from discord import (
        Reaction,
        User,
        Member,
        Message,
        RawReactionActionEvent as RawReactionActionEventPayload,
        RawReactionClearEmojiEvent as RawReactionClearEmojiEventPayload,
        RawReactionClearEvent as RawReactionClearEventPayload,
    )

__all__ = (
    "ReactionEvent",
    "ReactionClearEvent",
    "ReactionClearEmojiEvent",
    "RawReactionActionEvent",
    "RawReactionClearEvent",
    "RawReactionClearEmojiEvent",
)


# on_reaction_add
# on_reaction_remove
class ReactionEvent(Protocol):
    async def __call__(self, reaction: Reaction, user: Union[Member, User]) -> Any:
        ...


# on_reaction_clear
class ReactionClearEvent(Protocol):
    async def __call__(self, message: Message, reactions: List[Reaction]) -> Any:
        ...


# on_reaction_clear_emoji
class ReactionClearEmojiEvent(Protocol):
    async def __call__(self, reaction: Reaction) -> Any:
        ...


# on_raw_reaction_add
# on_raw_reaction_remove
class RawReactionActionEvent(Protocol):
    async def __call__(self, payload: RawReactionActionEventPayload) -> Any:
        ...


# on_raw_reaction_clear
class RawReactionClearEvent(Protocol):
    async def __call__(self, payload: RawReactionClearEventPayload) -> Any:
        ...


# on_raw_reaction_clear_emoji
class RawReactionClearEmojiEvent(Protocol):
    async def __call__(self, payload: RawReactionClearEmojiEventPayload) -> Any:
        ...
