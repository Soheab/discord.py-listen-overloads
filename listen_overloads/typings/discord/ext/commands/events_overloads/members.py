from __future__ import annotations
from typing import Any, TYPE_CHECKING, Union, Protocol

if TYPE_CHECKING:
    from discord import (
        Member,
        User,
        Guild,
        RawMemberRemoveEvent as RawMemberRemoveEventPayload,
    )


__all__ = (
    "MemberEvent",
    "RawMemberRemoveEvent",
    "MemberUpdateEvent",
    "UserUpdateEvent",
    "MemberBanEvent",
    "MemberUnbanEvent",
)


# on_member_join
# on_member_remove
class MemberEvent(Protocol):
    async def __call__(self, member: Member) -> Any:
        ...


# on_raw_member_remove
class RawMemberRemoveEvent(Protocol):
    async def __call__(self, payload: RawMemberRemoveEventPayload) -> Any:
        ...


# on_member_update
class MemberUpdateEvent(Protocol):
    async def __call__(self, before: Member, after: Member) -> Any:
        ...


# on_user_update
class UserUpdateEvent(Protocol):
    async def __call__(self, before: User, after: User) -> Any:
        ...


# on_member_ban
class MemberBanEvent(Protocol):
    async def __call__(self, guild: Guild, user: Union[Member, User]) -> Any:
        ...


# on_member_unban
class MemberUnbanEvent(Protocol):
    async def __call__(self, guild: Guild, user: User) -> Any:
        ...


# on_presence_update
# ^ MemberUpdateEvent
