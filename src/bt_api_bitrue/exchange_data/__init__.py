from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData

_FALLBACK_REST_PATHS = {
    "ping": "GET /api/v1/ping",
    "get_server_time": "GET /api/v1/time",
    "get_exchange_info": "GET /api/v1/exchangeInfo",
    "get_tick": "GET /api/v1/ticker/24hr",
    "get_depth": "GET /api/v1/depth",
    "get_kline": "GET /api/v1/market/kline",
    "get_trades": "GET /api/v1/trades",
    "get_account": "GET /api/v1/account",
    "get_balance": "GET /api/v1/account",
    "make_order": "POST /api/v1/order",
    "cancel_order": "DELETE /api/v1/order",
    "cancel_all_orders": "DELETE /api/v1/openOrders",
    "query_order": "GET /api/v1/order",
    "get_open_orders": "GET /api/v1/openOrders",
    "get_all_orders": "GET /api/v1/allOrders",
    "get_deals": "GET /api/v1/myTrades",
}


class BitrueExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "BITRUE___SPOT"
        self.rest_url = "https://www.bitrue.com"
        self.wss_url = "wss://ws.bitrue.com/kline-api/ws"
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1m",
            "5m": "5m",
            "15m": "15m",
            "30m": "30m",
            "1h": "1h",
            "2h": "2h",
            "4h": "4h",
            "12h": "12h",
            "1d": "1d",
            "1w": "1w",
        }
        self.legal_currency = ["USDT", "BTC", "ETH", "XRP"]

    def get_symbol(self, symbol: str) -> str:
        return symbol.upper().replace("/", "").replace("-", "").replace("_", "")

    def get_period(self, key: str) -> str:
        return self.kline_periods.get(key, key)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        return self.rest_paths[key]

    def get_wss_path(self, channel_type: str, symbol: str | None = None, **kwargs) -> str:
        path = self.wss_paths.get(channel_type, "")
        if symbol and "{symbol}" in str(path):
            path = str(path).replace("{symbol}", self.get_symbol(symbol))
        return path


class BitrueExchangeDataSpot(BitrueExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"


# Backward compatibility alias
BitrueSpotExchangeData = BitrueExchangeDataSpot
