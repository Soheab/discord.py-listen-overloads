# discord.py-listen-overloads
A stubs package for [discord.py](https://discordpy.readthedocs.io/en/stable/index.html) that adds overloads to the ``@commands.Bot.listen`` decorator.

## Installation
```bash
python -m pip install discord.py-listen-overloads
```
Or the development version:
```bash
python -m pip install "discord.py-listen-overloads @ git+https://github.com/Soheab/discord.py-listen-overloads"
```
The versions depends on the latest stable release of [discord.py on PyPi](https://pypi.org/project/discord.py/).

For example if the discord.py version on PyPi is ``2.5.1`` then running the first command will also install ``discord.py-listen-overloads==2.5.1`` and the development version will probably be ``2.6.0a``.

You can also install this stub for specific discord.py version by adding ``==the.version.here`` from version ``2.3.2`` to the first command.


## Example

### Before:
```py
bot = commands.Bot(**kwargs)

@bot.listen("on_typing")  # no errors
async def on_typing_event(channel):
    ...

@bot.listen("non_extisting_event")  # no errors
async def non_extisting_event(random: bool):
    ...

reveal_type(on_typing_event)
# Type of "on_typing_event" is "(channel: Unknown) -> Coroutine[Any, Any, None]"
reveal_type(non_extisting_event)
# Type of "non_extisting_event" is "(random: bool) -> Coroutine[Any, Any, None]"
```

### After:
```py
bot = commands.Bot(**kwargs)

@bot.listen("on_typing") # <--
# - Argument of type "(channel: Unknown) -> Coroutine[Any, Any, None]" cannot be assigned to parameter of type "TypingEvent"
#  Type "(channel: Unknown) -> Coroutine[Any, Any, None]" cannot be assigned to type "(channel: Messageable, user: Member | User, when: datetime) -> Coroutine[Any, Any, Any]"
#    Function accepts too many positional parameters; expected 1 but received 3
async def on_typing_event(channel):
    ...

@bot.listen("non_extisting_event")  # <--
# DISCLAIMER: the error can be different for you but similar.
# - Argument of type "Literal['non_extisting_event']" cannot be assigned to parameter "name" of type "Literal['on_command', 'on_command_completion']" in function "listen"
#  Type "Literal['non_extisting_event']" cannot be assigned to type "Literal['on_command', 'on_command_completion']"
#    "Literal['non_extisting_event']" cannot be assigned to type "Literal['on_command']"
#    "Literal['non_extisting_event']" cannot be assigned to type "Literal['on_command_completion']"
async def non_extisting_event(random: bool):
    ...

reveal_type(on_typing_event)
# Type of "on_typing_event" is "TypingEvent"
```
So now we know that the ``on_typing`` is an existing event but ``non_extisting_event`` is not. that is takes 3 parameters and all their types. Here 
is the correct correct version that shouldn't error:
```py
from typing import Any

import datetime


@bot.listen("on_typing")  # no errors
async def on_typing_event(channel: discord.abc.Messageable, user: discord.Member | discord.User, when: datetime.datetime) -> Any:
    ...
```

Custom events are not supported unfortunately since that would defeat the whole point of such package.

## Why?
Idk you're reading this.

But like isn't cool to be able to use events without having to pull up docs for it?

## Contact
You can contact me on Discord at ``Soheab_`` or mention me in the discord.py [server](https://discord.gg/dpy). Also welcome to open an issue/pull-request on this repo for anything.

## Credits
This package is heavily inpsired by [bryanforbes's](https://github.com/bryanforbes) package called [discord.py-stubs](https://github.com/bryanforbes/discord.py-stubs). It provides stubs for the whole library from versions 1.3.4.0 to the last 1.x release (1.7.3).