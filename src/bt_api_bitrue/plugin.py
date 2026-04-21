from __future__ import annotations

from bt_api_base.plugins.protocol import PluginInfo
from bt_api_bitrue.exchange_data import BitrueExchangeDataSpot
from bt_api_bitrue.feeds.live_bitrue.spot import BitrueRequestDataSpot


def get_plugin_info() -> PluginInfo:
    return PluginInfo(
        name="bitrue",
        display_name="Bitrue",
        version="0.1.0",
        supported_asset_types=["SPOT"],
        feed_classes=[BitrueRequestDataSpot],
        exchange_data_classes=[BitrueExchangeDataSpot],
    )
