import requests

# Map CoinGecko IDs or names to Binance symbols
COIN_SYMBOLS = {
    "bitcoin": "BTCUSDT",
    "ethereum": "ETHUSDT",
    "solana": "SOLUSDT",
    "dogecoin": "DOGEUSDT",
    # Add more as needed
}

def get_binance_price(coin_name):
    try:
        symbol = COIN_SYMBOLS.get(coin_name.lower())
        if not symbol:
            return f"Price fetch error: Unsupported symbol '{coin_name}'"

        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        res = requests.get(url).json()

        if 'price' not in res:
            return f"Price fetch error: {res.get('msg', 'No price returned')}"

        return float(res['price'])
    except Exception as e:
        return f"Price fetch error: {e}"
