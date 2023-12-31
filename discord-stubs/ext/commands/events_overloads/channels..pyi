from __future__ import annotations
from typing import TYPE_CHECKING, Any, Protocol, Union

if TYPE_CHECKING:
    from discord.abc import GuildChannel, Messageable
    from discord import (
        GroupChannel,
        Member,
        User,
        RawTypingEvent as RawTypingEventPayload,
    )
    from datetime import datetime

__all__ = (
    "GuildChannelCreateDeleteEvent",
    "GuildChannelUpdateEvent",
    "GuildChannelPinsUpdateEvent",
    "PrivateChannelUpdateEvent",
    "PrivateChannelPinsUpdateEvent",
    "TypingEvent",
    "RawTypingEvent",
)

# on_guild_channel_delete
# on_guild_channel_create
class GuildChannelCreateDeleteEvent(Protocol):
    async def __call__(self, channel: GuildChannel) -> Any: ...

# on_guild_channel_update
class GuildChannelUpdateEvent(Protocol):
    async def __call__(self, before: GuildChannel, after: GuildChannel) -> Any: ...

# on_guild_channel_pins_update
class GuildChannelPinsUpdateEvent(Protocol):
    async def __call__(self, channel: GuildChannel, last_pin: datetime) -> Any: ...

# on_private_channel_update
class PrivateChannelUpdateEvent(Protocol):
    async def __call__(self, before: GroupChannel, after: GroupChannel) -> Any: ...

# on_private_channel_pins_update
class PrivateChannelPinsUpdateEvent(Protocol):
    async def __call__(self, channel: GroupChannel, last_pin: datetime) -> Any: ...

# on_typing
class TypingEvent(Protocol):
    async def __call__(self, channel: Messageable, user: Union[Member, User], when: datetime) -> Any: ...

# on_raw_typing
class RawTypingEvent(Protocol):
    async def __call__(self, payload: RawTypingEventPayload) -> Any: ...
