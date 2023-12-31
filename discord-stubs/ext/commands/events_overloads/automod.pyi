from __future__ import annotations
from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from discord import AutoModAction, AutoModRule

__all__ = (
    "AutoModRuleEvents",
    "AutoModActionEvent",
)

# on_automod_rule_create
# on_automod_rule_update
# on_automod_rule_delete
class AutoModRuleEvents(Protocol):
    async def __call__(self, rule: AutoModRule) -> Any: ...

# on_automod_action
class AutoModActionEvent(Protocol):
    async def __call__(self, execution: AutoModAction) -> Any: ...
