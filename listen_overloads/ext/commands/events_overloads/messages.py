from __future__ import annotations
from typing import Any, TYPE_CHECKING, List, Protocol

if TYPE_CHECKING:
    from discord import (
        Message,
        RawMessageUpdateEvent as RawMessageUpdateEventPayload,
        RawMessageDeleteEvent as RawMessageDeleteEventPayload,
        RawBulkMessageDeleteEvent as RawBulkMessageDeleteEventPayload,
    )

__all__ = (
    "MessageEvent",
    "MessageEditEvent",
    "BulkMessageDeleteEvent",
    "RawMessageEditEvent",
    "RawMessageDeleteEvent",
    "RawBulkMessageDeleteEvent",
)


# on_message
# on_message_delete
class MessageEvent(Protocol):
    async def __call__(self, message: Message) -> Any:
        ...


# on_message_edit
class MessageEditEvent(Protocol):
    async def __call__(self, before: Message, after: Message) -> Any:
        ...


# on_bulk_message_delete
class BulkMessageDeleteEvent(Protocol):
    async def __call__(self, messages: List[Message]) -> Any:
        ...


# on_raw_message_edit
class RawMessageEditEvent(Protocol):
    async def __call__(self, payload: RawMessageUpdateEventPayload) -> Any:
        ...


# on_raw_message_delete
class RawMessageDeleteEvent(Protocol):
    async def __call__(self, payload: RawMessageDeleteEventPayload) -> Any:
        ...


# on_raw_bulk_message_delete
class RawBulkMessageDeleteEvent(Protocol):
    async def __call__(self, payload: RawBulkMessageDeleteEventPayload) -> Any:
        ...
