from typing import TYPE_CHECKING, TypeVar, Callable, Coroutine, Any


CoroT = TypeVar("CoroT")
CoroFunc = Callable[..., Coroutine[Any, Any, CoroT]]

EventT = TypeVar("EventT")
EventCallable = Callable[[EventT], EventT]
