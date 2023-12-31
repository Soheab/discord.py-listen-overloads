"""
This type stub file was generated by pyright.
"""

from typing import ClassVar, Literal, Optional, TYPE_CHECKING, Tuple, Union
from .enums import ComponentType
from .partial_emoji import PartialEmoji
from .types.components import ActionRow as ActionRowPayload, ButtonComponent as ButtonComponentPayload, Component as ComponentPayload, SelectMenu as SelectMenuPayload, SelectOption as SelectOptionPayload, TextInput as TextInputPayload
from .emoji import Emoji

"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
if TYPE_CHECKING:
    ActionRowChildComponentType = Union['Button', 'SelectMenu', 'TextInput']
__all__ = ('Component', 'ActionRow', 'Button', 'SelectMenu', 'SelectOption', 'TextInput')
class Component:
    """Represents a Discord Bot UI Kit Component.

    Currently, the only components supported by Discord are:

    - :class:`ActionRow`
    - :class:`Button`
    - :class:`SelectMenu`
    - :class:`TextInput`

    This class is abstract and cannot be instantiated.

    .. versionadded:: 2.0
    """
    __slots__: Tuple[str, ...] = ...
    __repr_info__: ClassVar[Tuple[str, ...]]
    def __repr__(self) -> str:
        ...
    
    @property
    def type(self) -> ComponentType:
        """:class:`ComponentType`: The type of component."""
        ...
    
    def to_dict(self) -> ComponentPayload:
        ...
    


class ActionRow(Component):
    """Represents a Discord Bot UI Kit Action Row.

    This is a component that holds up to 5 children components in a row.

    This inherits from :class:`Component`.

    .. versionadded:: 2.0

    Attributes
    ------------
    children: List[Union[:class:`Button`, :class:`SelectMenu`, :class:`TextInput`]]
        The children components that this holds, if any.
    """
    __slots__: Tuple[str, ...] = ...
    __repr_info__: ClassVar[Tuple[str, ...]] = ...
    def __init__(self, data: ActionRowPayload, /) -> None:
        ...
    
    @property
    def type(self) -> Literal[ComponentType.action_row]:
        """:class:`ComponentType`: The type of component."""
        ...
    
    def to_dict(self) -> ActionRowPayload:
        ...
    


class Button(Component):
    """Represents a button from the Discord Bot UI Kit.

    This inherits from :class:`Component`.

    .. note::

        The user constructible and usable type to create a button is :class:`discord.ui.Button`
        not this one.

    .. versionadded:: 2.0

    Attributes
    -----------
    style: :class:`.ButtonStyle`
        The style of the button.
    custom_id: Optional[:class:`str`]
        The ID of the button that gets received during an interaction.
        If this button is for a URL, it does not have a custom ID.
    url: Optional[:class:`str`]
        The URL this button sends you to.
    disabled: :class:`bool`
        Whether the button is disabled or not.
    label: Optional[:class:`str`]
        The label of the button, if any.
    emoji: Optional[:class:`PartialEmoji`]
        The emoji of the button, if available.
    """
    __slots__: Tuple[str, ...] = ...
    __repr_info__: ClassVar[Tuple[str, ...]] = ...
    def __init__(self, data: ButtonComponentPayload, /) -> None:
        ...
    
    @property
    def type(self) -> Literal[ComponentType.button]:
        """:class:`ComponentType`: The type of component."""
        ...
    
    def to_dict(self) -> ButtonComponentPayload:
        ...
    


class SelectMenu(Component):
    """Represents a select menu from the Discord Bot UI Kit.

    A select menu is functionally the same as a dropdown, however
    on mobile it renders a bit differently.

    .. note::

        The user constructible and usable type to create a select menu is
        :class:`discord.ui.Select` not this one.

    .. versionadded:: 2.0

    Attributes
    ------------
    type: :class:`ComponentType`
        The type of component.
    custom_id: Optional[:class:`str`]
        The ID of the select menu that gets received during an interaction.
    placeholder: Optional[:class:`str`]
        The placeholder text that is shown if nothing is selected, if any.
    min_values: :class:`int`
        The minimum number of items that must be chosen for this select menu.
        Defaults to 1 and must be between 0 and 25.
    max_values: :class:`int`
        The maximum number of items that must be chosen for this select menu.
        Defaults to 1 and must be between 1 and 25.
    options: List[:class:`SelectOption`]
        A list of options that can be selected in this menu.
    disabled: :class:`bool`
        Whether the select is disabled or not.
    channel_types: List[:class:`.ChannelType`]
        A list of channel types that are allowed to be chosen in this select menu.
    """
    __slots__: Tuple[str, ...] = ...
    __repr_info__: ClassVar[Tuple[str, ...]] = ...
    def __init__(self, data: SelectMenuPayload, /) -> None:
        ...
    
    def to_dict(self) -> SelectMenuPayload:
        ...
    


class SelectOption:
    """Represents a select menu's option.

    These can be created by users.

    .. versionadded:: 2.0

    Parameters
    -----------
    label: :class:`str`
        The label of the option. This is displayed to users.
        Can only be up to 100 characters.
    value: :class:`str`
        The value of the option. This is not displayed to users.
        If not provided when constructed then it defaults to the
        label. Can only be up to 100 characters.
    description: Optional[:class:`str`]
        An additional description of the option, if any.
        Can only be up to 100 characters.
    emoji: Optional[Union[:class:`str`, :class:`Emoji`, :class:`PartialEmoji`]]
        The emoji of the option, if available.
    default: :class:`bool`
        Whether this option is selected by default.

    Attributes
    -----------
    label: :class:`str`
        The label of the option. This is displayed to users.
        Can only be up to 100 characters.
    value: :class:`str`
        The value of the option. This is not displayed to users.
        If not provided when constructed then it defaults to the
        label. Can only be up to 100 characters.
    description: Optional[:class:`str`]
        An additional description of the option, if any.
        Can only be up to 100 characters.
    default: :class:`bool`
        Whether this option is selected by default.
    """
    __slots__: Tuple[str, ...] = ...
    def __init__(self, *, label: str, value: str = ..., description: Optional[str] = ..., emoji: Optional[Union[str, Emoji, PartialEmoji]] = ..., default: bool = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    @property
    def emoji(self) -> Optional[PartialEmoji]:
        """Optional[:class:`.PartialEmoji`]: The emoji of the option, if available."""
        ...
    
    @emoji.setter
    def emoji(self, value: Optional[Union[str, Emoji, PartialEmoji]]) -> None:
        ...
    
    @classmethod
    def from_dict(cls, data: SelectOptionPayload) -> SelectOption:
        ...
    
    def to_dict(self) -> SelectOptionPayload:
        ...
    


class TextInput(Component):
    """Represents a text input from the Discord Bot UI Kit.

    .. note::
        The user constructible and usable type to create a text input is
        :class:`discord.ui.TextInput` not this one.

    .. versionadded:: 2.0

    Attributes
    ------------
    custom_id: Optional[:class:`str`]
        The ID of the text input that gets received during an interaction.
    label: :class:`str`
        The label to display above the text input.
    style: :class:`TextStyle`
        The style of the text input.
    placeholder: Optional[:class:`str`]
        The placeholder text to display when the text input is empty.
    value: Optional[:class:`str`]
        The default value of the text input.
    required: :class:`bool`
        Whether the text input is required.
    min_length: Optional[:class:`int`]
        The minimum length of the text input.
    max_length: Optional[:class:`int`]
        The maximum length of the text input.
    """
    __slots__: Tuple[str, ...] = ...
    __repr_info__: ClassVar[Tuple[str, ...]] = ...
    def __init__(self, data: TextInputPayload, /) -> None:
        ...
    
    @property
    def type(self) -> Literal[ComponentType.text_input]:
        """:class:`ComponentType`: The type of component."""
        ...
    
    def to_dict(self) -> TextInputPayload:
        ...
    
    @property
    def default(self) -> Optional[str]:
        """Optional[:class:`str`]: The default value of the text input.

        This is an alias to :attr:`value`.
        """
        ...
    

