from __future__ import annotations
from typing import Any, TYPE_CHECKING, Sequence, Protocol

if TYPE_CHECKING:
    from discord import Guild, Emoji, GuildSticker, AuditLogEntry, Invite


__all__ = (
    "GuildEvent",
    "GuildUpdateEvent",
    "GuildEmojisUpdateEvent",
    "GuildStickersUpdateEvent",
    "AuditLogEntryCreateEvent",
    "InviteEvent",
)


# on_guild_available
# on_guild_unavailable
# on_guild_join
# on_guild_remove
class GuildEvent(Protocol):
    async def __call__(self, guild: Guild) -> Any:
        ...


# on_guild_update
class GuildUpdateEvent(Protocol):
    async def __call__(self, before: Guild, after: Guild) -> Any:
        ...


# on_guild_emojis_update
class GuildEmojisUpdateEvent(Protocol):
    async def __call__(self, guild: Guild, before: Sequence[Emoji], after: Sequence[Emoji]) -> Any:
        ...


# on_guild_stickers_update
class GuildStickersUpdateEvent(Protocol):
    async def __call__(
        self,
        guild: Guild,
        before: Sequence[GuildSticker],
        after: Sequence[GuildSticker],
    ) -> Any:
        ...


# on_audit_log_entry_create
class AuditLogEntryCreateEvent(Protocol):
    async def __call__(self, entry: AuditLogEntry) -> Any:
        ...


# on_invite_create
# on_invite_delete
class InviteEvent(Protocol):
    async def __call__(self, invite: Invite) -> Any:
        ...
