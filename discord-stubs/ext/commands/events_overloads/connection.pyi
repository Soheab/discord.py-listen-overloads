from __future__ import annotations
from typing import Any, Protocol

__all__ = (
    "ConnectEvent",
    "DisconnectEvent",
    "ShardEvent",
)


# on_connect
class ConnectEvent(Protocol):
    async def __call__(self) -> Any:
        ...


# on_disconnect
class DisconnectEvent(Protocol):
    async def __call__(self) -> Any:
        ...


# on_shard_connect
# on_shard_disconnect
class ShardEvent(Protocol):
    async def __call__(self, shard_id: int) -> Any:
        ...
