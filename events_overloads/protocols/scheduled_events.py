from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord import ScheduledEvent, User


__all__ = (
    "ScheduledEventEvent",
    "ScheduledEventUpdateEvent",
    "ScheduledEventUserEvent",
)


# on_scheduled_event_create
# on_scheduled_event_delete
class ScheduledEventEvent(Protocol):
    async def __call__(self, event: ScheduledEvent) -> Any:
        ...


# on_scheduled_event_update
class ScheduledEventUpdateEvent(Protocol):
    async def __call__(self, before: ScheduledEvent, after: ScheduledEvent) -> Any:
        ...


# on_scheduled_event_user_add
# on_scheduled_event_user_remove
class ScheduledEventUserEvent(Protocol):
    async def __call__(self, event: ScheduledEvent, user: User) -> Any:
        ...
