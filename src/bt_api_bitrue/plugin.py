"""Module-level docstring."""
# generated, verify register call

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from bt_api_base.plugins.protocol import PluginInfo

from bt_api_bitrue.registry_registration import register
from bt_api_bitrue import __version__

if TYPE_CHECKING:
    from bt_api_base.registry import ExchangeRegistry


def register_plugin(registry: ExchangeRegistry, runtime_factory: Any) -> PluginInfo:
    """register_plugin function"""
    register()

    return PluginInfo(
        name="bt_api_bitrue",
        version=__version__,
        core_requires=">=0.15,<1.0",
        supported_exchanges=("BITRUE___SPOT",),
        supported_asset_types=("SPOT",),
    )
