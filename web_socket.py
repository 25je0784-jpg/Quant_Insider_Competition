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

socket.connect()
socket.subscribe(["1755244"], data_type="orderbook")
socket.keep_running()