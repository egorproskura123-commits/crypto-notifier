import requests


def get_price(coin):

    prices = {
        "BTC": "BTCUSDT",
        "ETH": "ETHUSDT",
        "SOL": "SOLUSDT",
        "XRP": "XRPUSDT"
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