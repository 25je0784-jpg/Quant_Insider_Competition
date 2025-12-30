import threading
from nubra_python_sdk.ticker import websocketdata
from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv


nubra = InitNubraSdk(NubraEnv.UAT)
def on_market_data(msg):
    print(f"[MarketData] {msg}")

def on_index_data(msg):
    print(f"[INDEX] {msg}")

def on_option_data(msg):
    print(f"[OPTION] {msg}")

def on_orderbook_data(msg):
    print("[Orderbook] ", msg)

def on_ohlcv_data(msg):
    print(f"[OHLCV] {msg}")

def on_greeks_data(msg):
    print(f"[Greeks] {msg}")

def on_connect(msg):
    print("[status]", msg)

def on_close(reason):
    print(f"Closed: {reason}")

def on_error(err):
    print(f"Error: {err}")

socket = websocketdata.NubraDataSocket(
    client=nubra,
    on_market_data=on_market_data,
    on_index_data=on_index_data,
    on_option_data=on_option_data,
    on_orderbook_data=on_orderbook_data,
    on_ohlcv_data=on_ohlcv_data,
    on_greeks_data=on_greeks_data,
    on_connect=on_connect,
    on_close=on_close,
    on_error=on_error,
    )
def run_websocket():
    socket.connect()
    socket.subscribe(["1755244"], data_type="orderbook")
    socket.keep_running()

websocket_thread = threading.Thread(target=run_websocket)
websocket_thread.daemon = True
websocket_thread.start()
from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.trading.trading_data import NubraTrader
from nubra_python_sdk.trading.trading_enum import (
    OrderSideEnum,
    OrderTypeEnumV2,
    ValidityTypeEnumV2,
    PriceTypeEnumV2
)

nubra = InitNubraSdk(NubraEnv.UAT)

trade = NubraTrader(nubra, version= "V2")

result = trade.create_order({
    "ref_id": 1755244,
    "order_type": "ORDER_TYPE_STOPLOSS",
    "order_qty": 75,
    "order_side": "ORDER_SIDE_BUY",
    "order_delivery_type": "ORDER_DELIVERY_TYPE_CNC",
    "validity_type" : "DAY",
    "price_type": "LIMIT",
    "order_price": 35500,
    "exchange": "NSE",
    "tag": "order_test",
    "algo_params": {
    "trigger_price": 30000
 }
})


