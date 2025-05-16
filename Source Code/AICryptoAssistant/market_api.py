import requests

def get_coin_info(coin_name):
    try:
        search = requests.get(f"https://api.coingecko.com/api/v3/search?query={coin_name}").json()
        if not search['coins']:
            return f"No data found for {coin_name}"
        coin_id = search['coins'][0]['id']
        coin_data = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}").json()
        return {
            "name": coin_data['name'],
            "symbol": coin_data['symbol'].upper(),
            "market_cap": coin_data['market_data']['market_cap']['usd'],
            "rank": coin_data['market_cap_rank'],
            "price": coin_data['market_data']['current_price']['usd'],
            "image": coin_data['image']['thumb']
        }
    except Exception as e:
        return f"CoinGecko error: {e}"
