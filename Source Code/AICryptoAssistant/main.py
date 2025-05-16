import streamlit as st
from news_api import get_news
from price_api import get_binance_price
from market_api import get_coin_info
from ollama_chat import ask_ollama

# Configure page
st.set_page_config(page_title="AI Crypto Assistant", layout="centered", initial_sidebar_state="expanded")

st.sidebar.markdown("🚀 **AI Crypto Assistant** helps you:\n- Get live market data\n- View crypto news\n- Ask intelligent questions")

# Main UI
st.title("🤖 AI Crypto Assistant")
st.caption("Powered by Binance, CoinGecko, CryptoPanic, and Ollama")

user_query = st.text_input("Ask about a crypto (e.g., 'Tell me about Ethereum')")

if st.button("Ask") and user_query:
    coin = user_query.split()[-1].lower()

    with st.spinner("🔄 Fetching live data..."):
        news = get_news(coin)
        price = get_binance_price(coin)
        coin_info = get_coin_info(coin)

        if isinstance(coin_info, dict):
            facts = f"""
Coin: {coin_info['name']} ({coin_info['symbol']})
Market Rank: #{coin_info['rank']}
Market Cap: ${coin_info['market_cap']:,.2f}
Price (CoinGecko): ${coin_info['price']:,.2f}
Price (Binance): ${price}
            """
            coin_image = coin_info.get("image", "")
            coin_name = coin_info['name']
            coin_symbol = coin_info['symbol']
        else:
            facts = coin_info
            coin_image = None
            coin_name = None
            coin_symbol = None

        news_text = "\n".join([f"{i+1}. {n}" for i, n in enumerate(news)])

        ai_prompt = f"""
A user asked: "{user_query}"

Here is the latest live market data:

{facts}

Latest news headlines:
{news_text}

Please summarize the market data and the news above, and give the user a clear, helpful answer.
        """

        ai_answer = ask_ollama(ai_prompt)

    if coin_name:
        st.header(f"{coin_name} ({coin_symbol})")
        if coin_image:
            st.image(coin_image, width=64)

    st.subheader("💬 Assistant's Answer")
    st.success(ai_answer)

    with st.expander("📰 Recent News"):
        for item in news:
            st.write("• " + item)

    with st.expander("📈 Market Info"):
        if isinstance(coin_info, dict):
            col1, col2, col3 = st.columns(3)
            col1.metric("Price (CoinGecko)", f"${coin_info['price']:,.2f}")
            col2.metric("Market Cap", f"${coin_info['market_cap']:,.0f}")
            col3.metric("Rank", f"#{coin_info['rank']}")
            st.code(facts)
        else:
            st.error(facts)
