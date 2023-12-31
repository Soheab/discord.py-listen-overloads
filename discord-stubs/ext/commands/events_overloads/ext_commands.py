from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord.ext.commands import CommandError, Context

__all__ = ("EntitlementEvent",)


# on_command_error
class CommandError(Protocol):
    async def __call__(
        self,
        ctx: Context[Any],
        error: CommandError,
    ) -> Any:
        ...


# on_command
# on_command_completion
class OnCommand(Protocol):
    async def __call__(
        self,
        ctx: Context[Any],
    ) -> Any:
        ...
