from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord import (
        Thread,
        ThreadMember,
        RawThreadDeleteEvent as RawThreadDeleteEventPayload,
        RawThreadUpdateEvent as RawThreadUpdateEventPayload,
        RawThreadMembersUpdate as RawThreadMembersUpdatePayload,
    )


__all__ = (
    "ThreadEvent",
    "ThreadUpdateEvent",
    "RawThreadUpdateEvent",
    "RawThreadDeleteEvent",
    "ThreadMemberEvent",
    "RawThreadMemberRemoveEvent",
)


# on_thread_create
# on_thread_join
# on_thread_remove
# on_thread_delete
class ThreadEvent(Protocol):
    async def __call__(self, thread: Thread) -> Any:
        ...


# on_thread_update
class ThreadUpdateEvent(Protocol):
    async def __call__(self, before: Thread, after: Thread) -> Any:
        ...


# on_raw_thread_update
class RawThreadUpdateEvent(Protocol):
    async def __call__(self, payload: RawThreadUpdateEventPayload) -> Any:
        ...


# on_raw_thread_delete
class RawThreadDeleteEvent(Protocol):
    async def __call__(self, payload: RawThreadDeleteEventPayload) -> Any:
        ...


# on_thread_member_join
# on_thread_member_remove
class ThreadMemberEvent(Protocol):
    async def __call__(self, member: ThreadMember) -> Any:
        ...


# on_raw_thread_member_remove
class RawThreadMemberRemoveEvent(Protocol):
    async def __call__(self, payload: RawThreadMembersUpdatePayload) -> Any:
        ...
