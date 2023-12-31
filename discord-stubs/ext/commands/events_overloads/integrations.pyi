from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord import (
        Integration,
        RawIntegrationDeleteEvent as RawIntegrationDeleteEventObject,
    )
    from discord.abc import GuildChannel


__all__ = (
    "IntegrationEvent",
    "WebhooksUpdateEvent",
    "RawIntegrationDeleteEvent",
)


# on_integration_create
# on_integration_update
class IntegrationEvent(Protocol):
    async def __call__(self, integration: Integration) -> Any:
        ...


# on_guild_integrations_update
# ^ GuildEvent


# on_webhooks_update
class WebhooksUpdateEvent(Protocol):
    async def __call__(self, channel: GuildChannel) -> Any:
        ...


# on_raw_integration_delete
class RawIntegrationDeleteEvent(Protocol):
    async def __call__(self, payload: RawIntegrationDeleteEventObject) -> Any:
        ...
