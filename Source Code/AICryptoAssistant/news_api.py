import feedparser
import requests
from datetime import datetime

# Primary: Cointelegraph RSS Feed
def fetch_cointelegraph_news(coin_name, max_articles=5):
    try:
        feed_url = "https://cointelegraph.com/rss"
        feed = feedparser.parse(feed_url)

        coin_name_lower = coin_name.lower()
        headlines = []

        for entry in feed.entries:
            if (
                coin_name_lower in entry.title.lower()
                or coin_name_lower in entry.summary.lower()
                or coin_name_lower in entry.link.lower()
            ):
                published = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M')
                headlines.append(f"{published} — {entry.title} ({entry.link})")
                if len(headlines) >= max_articles:
                    break

        return headlines
    except Exception as e:
        return [f"Error fetching Cointelegraph news: {e}"]

# Fallback: CryptoCompare News API
def fetch_cryptocompare_news(coin_name, max_articles=5):
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        res = requests.get(url).json()
        articles = res.get("Data", [])
        coin_name_lower = coin_name.lower()

        headlines = []
        for article in articles:
            if coin_name_lower in article["title"].lower() or coin_name_lower in article["body"].lower():
                published = datetime.utcfromtimestamp(article["published_on"]).strftime('%Y-%m-%d %H:%M')
                headlines.append(f"{published} — {article['title']} ({article['url']})")
                if len(headlines) >= max_articles:
                    break

        return headlines
    except Exception as e:
        return [f"Error fetching CryptoCompare news: {e}"]

# Unified function with fallback
def get_news(coin_name):
    primary_news = fetch_cointelegraph_news(coin_name)
    if not primary_news:
        return fetch_cryptocompare_news(coin_name)
    return primary_news
