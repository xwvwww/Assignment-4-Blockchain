# 🧠 AI Crypto Assistant
An AI-powered Streamlit web app that provides live insights into the crypto market using real-time off-chain data.

# 🚀 Objective
Build an AI Assistant that:

* Answers user questions about the cryptocurrency market.

* Aggregates live data from multiple trusted sources.

* Uses an LLM (via Ollama) to provide intelligent summaries.

# 📊 Features
* Natural Language Query
  Ask questions like:

  * “What’s the latest news about Ethereum?”

  * “What’s the current price and market cap of Solana?”

* Live Data Aggregation
  On each query, the app fetches:

  * News from a crypto news API.

  * Price data from Binance.

  * Market data (ranking, market cap) from CoinGecko.

* AI-Powered Summaries
  The app uses an LLM (through Ollama) to:

  * Analyze and summarize current price, market stats, and news.

  * Provide helpful, human-readable responses.

# 🔧 Requirements

1. Install Dependecies
```bash
 pip install -r requirements.txt
```

2. Run Ollama
```bash
 ollama run llama3
```

3. Run Streamlit
```bash
 streamlit run main.py
```

# 📁 File Structure
```bash
ai-crypto-assistant/
│
├── app.py                # Main Streamlit app
├── news_api.py           # News data fetching
├── price_api.py          # Exchange price data
├── market_api.py         # CoinGecko market data
├── ollama_chat.py        # Handles LLM communication
├── requirements.txt
└── README.md
```


## License

This project is licensed under the MIT License - see the LICENSE file for details.



