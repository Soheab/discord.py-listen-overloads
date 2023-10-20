from __future__ import annotations
import asyncio
from http import client

from typing import TYPE_CHECKING, Any, Callable, Protocol, TypeVar, Union

import discord

from .event_decorator import overloaded_event_decorator

if TYPE_CHECKING:
    from ._types import CoroFunc, EventT

    from .events_enum import Event, PossibleEvents, PossibleEventsWithOn


class EventDeco(Protocol):
    def __call__(
        self,
        name: Union[
            Event, PossibleEvents, PossibleEventsWithOn
        ] = discord.utils.MISSING,
    ) -> CoroFunc:
        ...


class OverloadedEventDecorator(Protocol):
    def __call__(
        self, func: Callable[[EventDeco], EventDeco]
    ) -> Callable[[CoroFunc], CoroFunc]:
        ...


class ClientWithListen(discord.Client):
    if TYPE_CHECKING:
        listen = overloaded_event_decorator  # type: ignore

    def __init__(self, *, intents: discord.Intents, **options: Any) -> None:
        super().__init__(intents=intents, **options)
        self.extra_events = {}

    def dispatch(self, event_name: str, /, *args: Any, **kwargs: Any) -> None:
        # super() will resolve to Client
        super().dispatch(event_name, *args, **kwargs)  # type: ignore
        ev = "on_" + event_name
        for event in self.extra_events.get(ev, []):
            self._schedule_event(event, ev, *args, **kwargs)  # type: ignore

    def add_listener(
        self, func: CoroFunc, /, name: str = discord.utils.MISSING
    ) -> None:
        """The non decorator alternative to :meth:`.listen`.

        .. versionchanged:: 2.0

            ``func`` parameter is now positional-only.

        Parameters
        -----------
        func: :ref:`coroutine <coroutine>`
            The function to call.
        name: :class:`str`
            The name of the event to listen for. Defaults to ``func.__name__``.

        Example
        --------

        .. code-block:: python3

            async def on_ready(): pass
            async def my_message(message): pass

            bot.add_listener(on_ready)
            bot.add_listener(my_message, 'on_message')

        """
        name = func.__name__ if name is discord.utils.MISSING else name

        if not asyncio.iscoroutinefunction(func):
            raise TypeError("Listeners must be coroutines")

        if name in self.extra_events:
            self.extra_events[name].append(func)
        else:
            self.extra_events[name] = [func]

    def remove_listener(
        self, func: CoroFunc, /, name: str = discord.utils.MISSING
    ) -> None:
        """Removes a listener from the pool of listeners.

        .. versionchanged:: 2.0

            ``func`` parameter is now positional-only.

        Parameters
        -----------
        func
            The function that was used as a listener to remove.
        name: :class:`str`
            The name of the event we want to remove. Defaults to
            ``func.__name__``.
        """

        name = func.__name__ if name is discord.utils.MISSING else name

        if name in self.extra_events:
            try:
                self.extra_events[name].remove(func)
            except ValueError:
                pass


client = ClientWithListen(intents=discord.Intents())


@client.listen("on_message")
async def lol():
    ...
