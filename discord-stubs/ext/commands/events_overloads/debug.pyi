from __future__ import annotations
from typing import Any, Union, Protocol

__all__ = (
    "ErrorEvent",
    "SocketEventTypeEvent",
    "SocketRawReceiveEvent",
    "SocketRawSendEvent",
)


# on_error
class ErrorEvent(Protocol):
    async def __call__(self, event: str, *args: Any, **kwargs: Any) -> Any:
        ...


# on_socket_event_type
class SocketEventTypeEvent(Protocol):
    async def __call__(
        self,
        event: str,
    ) -> Any:
        ...


# on_socket_raw_receive
class SocketRawReceiveEvent(Protocol):
    async def __call__(
        self,
        msg: str,
    ) -> Any:
        ...


# on_socket_raw_send
class SocketRawSendEvent(Protocol):
    async def __call__(
        self,
        payload: Union[bytes, str],
    ) -> Any:
        ...
