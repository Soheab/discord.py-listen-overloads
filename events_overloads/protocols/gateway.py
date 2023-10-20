from __future__ import annotations
from typing import Any, Protocol

__all__ = ("ReadyEvent",)


# on_ready
class ReadyEvent(Protocol):
    async def __call__(self) -> Any:
        ...


# on_shard_ready
# on_shard_resumed
# ^ ShardEvent
