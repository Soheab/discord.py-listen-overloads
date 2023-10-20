from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Literal,
    Protocol,
    TypeVar,
    Union,
    overload,
)

import discord


if TYPE_CHECKING:
    from .events_enum import PossibleEventsWithOn, PossibleEvents, Event
    from .protocols.channels import TypingEvent

    from datetime import datetime

    from discord import User, Member
    from discord.abc import Messageable

    UserOrMember = Union[User, Member]


@overload
def event(
    name: Literal["on_typing", "typing", Event.Typing]
) -> Callable[[TypingEvent], TypingEvent]:
    ...


def event(
    name: Union[Event, PossibleEventsWithOn, PossibleEvents] = discord.utils.MISSING
) -> Callable[[CoroFunc], CoroFunc]:
    def decorator(func: CoroFunc) -> CoroFunc:
        return func

    return decorator


@event("on_typing")
async def detect_typing() -> None:
    reveal_type(when)
    pass
