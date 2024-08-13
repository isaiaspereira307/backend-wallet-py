import json
import requests


def _get_bitcoin_price(url: str, price_key: str) -> float:
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data[price_key])
    except (requests.RequestException, json.JSONDecodeError, KeyError):
        return 0.0
    

def get_bitcoin_price_brl() -> float:
    return _get_bitcoin_price("https://api.bitvalor.com/v1/ticker.json", 'ticker_24h.exchanges.MBT.last')



def get_bitcoin_price_usd() -> float:
    return _get_bitcoin_price("https://api.bitfinex.com/v1/pubticker/btcusd", 'last_price')


def get_bitcoin_price(currency: str) -> float:
    if currency.upper() == 'BRL':
        return get_bitcoin_price_brl()
    elif currency.upper() == 'USD':
        return get_bitcoin_price_usd()
    else:
        return 0.0