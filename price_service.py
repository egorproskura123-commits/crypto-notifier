import requests


def get_price(coin):

    prices = {
        "BTCUSDT": "BTCUSDT",
        "ETHUSDT": "ETHUSDT",
        "SOLUSDT": "SOLUSDT",
        "XRPUSDT": "XRPUSDT"
    }

    symbol = prices[coin]

    url = "https://api.binance.com/api/v3/ticker/price"

    response = requests.get(
        url,
        params={
            "symbol": symbol
        }
    )

    data = response.json()

    return float(data["price"])