# data_fetcher.py
import requests
import config

def fetch_alpha_vantage_data(symbol):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': config.ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    symbol = 'AAPL'  # Example symbol
    av_data = fetch_alpha_vantage_data(symbol)
    print("Alpha Vantage Data:", av_data)
