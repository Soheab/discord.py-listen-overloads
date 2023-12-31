from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord import Role

__all__ = (
    "GuildRoleEvent",
    "GuildRoleUpdateEvent",
)


# on_guild_role_create
# on_guild_role_delete
class GuildRoleEvent(Protocol):
    async def __call__(self, role: Role) -> Any:
        ...


# on_guild_role_update
class GuildRoleUpdateEvent(Protocol):
    async def __call__(self, before: Role, after: Role) -> Any:
        ...
