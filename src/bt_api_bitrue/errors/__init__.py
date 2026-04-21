from __future__ import annotations

from bt_api_base.error import ErrorTranslator, UnifiedErrorCode


class BitrueErrorTranslator(ErrorTranslator):
    @classmethod
    def translate(cls, error_data: dict) -> UnifiedErrorCode:
        code = error_data.get("code", error_data.get("errorCode"))
        msg = error_data.get("msg", error_data.get("message", error_data.get("error")))
        if code == -2015 or "auth" in str(msg).lower():
            return UnifiedErrorCode.AUTHENTICATION_ERROR
        if code == -1022 or "signature" in str(msg).lower():
            return UnifiedErrorCode.AUTHENTICATION_ERROR
        if code == -1013 or "quantity" in str(msg).lower():
            return UnifiedErrorCode.INVALID_PARAMETER
        if code == -2010 or "balance" in str(msg).lower():
            return UnifiedErrorCode.INSUFFICIENT_BALANCE
        if code == -1021:
            return UnifiedErrorCode.TIMESTAMP_ERROR
        if code == -1003:
            return UnifiedErrorCode.RATE_LIMIT
        if code < 0 and code != -2008:
            return UnifiedErrorCode.UNKNOWN
        return UnifiedErrorCode.UNKNOWN
