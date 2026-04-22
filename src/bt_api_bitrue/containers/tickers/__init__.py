from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base._compat import Self
from bt_api_base.containers.tickers.ticker import TickerData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_string


class BitrueTickerData(TickerData):
    def __init__(
        self,
        ticker_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(ticker_info, has_been_json_encoded)
        self.exchange_name = "BITRUE"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.ticker_data: dict[str, Any] | None = (
            ticker_info if has_been_json_encoded and isinstance(ticker_info, dict) else None
        )
        self.ticker_symbol_name: str | None = None
        self.server_time: float | None = None
        self.last_price: float | None = None
        self.bid_price: float | None = None
        self.ask_price: float | None = None
        self.bid_volume: float | None = None
        self.ask_volume: float | None = None
        self.volume: float | None = None
        self.high: float | None = None
        self.low: float | None = None
        self.has_been_init_data = False

    def init_data(self) -> Self:
        if not self.has_been_json_encoded:
            self.ticker_data = json.loads(self.ticker_info)
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        data = self.ticker_data or {}
        if isinstance(data, dict):
            self.ticker_symbol_name = from_dict_get_string(data, "symbol")
            self.server_time = from_dict_get_float(data, "timestamp")
            self.last_price = from_dict_get_float(data, "lastPrice") or from_dict_get_float(
                data, "price",
            )
            self.bid_price = from_dict_get_float(data, "bidPrice") or from_dict_get_float(
                data, "bid",
            )
            self.ask_price = from_dict_get_float(data, "askPrice") or from_dict_get_float(
                data, "ask",
            )
            self.bid_volume = from_dict_get_float(data, "bidQty")
            self.ask_volume = from_dict_get_float(data, "askQty")
            self.volume = from_dict_get_float(data, "volume")
            self.high = from_dict_get_float(data, "highPrice") or from_dict_get_float(data, "high")
            self.low = from_dict_get_float(data, "lowPrice") or from_dict_get_float(data, "low")

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_last_price(self) -> float | None:
        self.init_data()
        return self.last_price

    def get_bid_price(self) -> float | None:
        self.init_data()
        return self.bid_price

    def get_ask_price(self) -> float | None:
        self.init_data()
        return self.ask_price

    def get_bid_volume(self) -> float | None:
        self.init_data()
        return self.bid_volume

    def get_ask_volume(self) -> float | None:
        self.init_data()
        return self.ask_volume

    def get_high(self) -> float | None:
        self.init_data()
        return self.high

    def get_low(self) -> float | None:
        self.init_data()
        return self.low

    def get_volume(self) -> float | None:
        self.init_data()
        return self.volume

    def get_all_data(self) -> dict[str, Any]:
        self.init_data()
        return {
            "exchange_name": self.exchange_name,
            "symbol_name": self.symbol_name,
            "asset_type": self.asset_type,
            "local_update_time": self.local_update_time,
            "ticker_symbol_name": self.ticker_symbol_name,
            "server_time": self.server_time,
            "bid_price": self.bid_price,
            "ask_price": self.ask_price,
            "bid_volume": self.bid_volume,
            "ask_volume": self.ask_volume,
            "last_price": self.last_price,
            "volume": self.volume,
            "high": self.high,
            "low": self.low,
        }

    def __str__(self) -> str:
        self.init_data()
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()


class BitrueRequestTickerData(BitrueTickerData):
    pass


class BitrueWssTickerData(BitrueTickerData):
    pass
