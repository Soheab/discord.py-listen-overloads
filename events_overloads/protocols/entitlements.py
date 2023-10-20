from __future__ import annotations
from typing import Any, TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from discord import Entitlement

__all__ = ("EntitlementEvent",)


# on_entitlement_create
# on_entitlement_update
# on_entitlement_delete
class EntitlementEvent(Protocol):
    async def __call__(self, entitlement: Entitlement) -> Any:
        ...
