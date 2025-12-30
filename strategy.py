from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.trading.trading_data import NubraTrader
from nubra_python_sdk.ticker import websocketdata

nubra = InitNubraSdk(NubraEnv.UAT)
trader = NubraTrader(nubra, version="V2")
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


inventory = 0
inventory_limit = 600
base_spread = 20


def on_market_update(data):
    global inventory
    best_bid = data.bids[0].price
    best_ask = data.asks[0].price
    mid_price = (best_bid + best_ask) / 2

    skew = -inventory * 0.5

    my_bid = mid_price - (base_spread / 2) + skew
    my_ask = mid_price + (base_spread / 2) + skew

    print(f"Quoting Bid: {my_bid} | Ask: {my_ask} | Inv: {inventory}")


socket.subscribe([1755244], data_type="DEPTH", callback=on_market_update)
socket.connect()