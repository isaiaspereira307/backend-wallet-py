import json
import requests

def get_bitcoin_price_brl() -> float:
    try:
        response = requests.get("https://api.bitvalor.com/v1/ticker.json")
        response.raise_for_status()
        data = response.json()
        return data['ticker_24h']['exchanges']['MBT']['last']
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        print(f"Error fetching Bitcoin price: {e}")
        return 0.0


def get_bitcoin_price_usd() -> float:
    try:
        response = requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
        response.raise_for_status() 
        data = response.json()
        return float(data['last_price'])
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        print(f"Error fetching Bitcoin price: {e}")
        return 0.0

def btc_to_brl(btc_amount: float) -> str:
    try:
        price_in_brl = get_bitcoin_price_brl()
        value_in_brl = price_in_brl * btc_amount
        formatted_value = "{0:.2f}".format(value_in_brl)
        return formatted_value
    except Exception as e:
        print(f"Error converting BTC to BRL: {e}")
        return "0.00"


def btc_to_usd(btc_amount: float) -> str:
    try:
        price_in_usd = get_bitcoin_price_usd()
        value_in_usd = price_in_usd * btc_amount
        formatted_value = "{0:.2f}".format(value_in_usd)
        return formatted_value
    except Exception as e:
        print(f"Error converting BTC to USD: {e}")
        return "0.00"