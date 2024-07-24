# technical_analysis.py
import requests
import config
import pandas as pd

def fetch_historical_data(symbol):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': config.ALPHA_VANTAGE_API_KEY,
        'outputsize': 'compact'  # 'compact' for last 100 data points, 'full' for full-length data
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if 'Time Series (Daily)' in data:
        time_series = data['Time Series (Daily)']
        df = pd.DataFrame.from_dict(time_series, orient='index', dtype='float')
        df.index = pd.to_datetime(df.index)
        df.sort_index(inplace=True)
        return df
    else:
        print("Error: 'Time Series (Daily)' not found in the response")
        print("Response from Alpha Vantage:", data)
        return None

def calculate_moving_averages(df, window):
    return df['4. close'].rolling(window=window).mean()

def calculate_rsi(df, periods=14):
    delta = df['4. close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    short_ema = df['4. close'].ewm(span=short_window, adjust=False).mean()
    long_ema = df['4. close'].ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_window, adjust=False).mean()
    return macd, signal

if __name__ == "__main__":
    symbol = 'AAPL'  # Example symbol
    df = fetch_historical_data(symbol)
    
    if df is not None:
        # Calculate technical indicators
        df['50_MA'] = calculate_moving_averages(df, 50)
        df['200_MA'] = calculate_moving_averages(df, 200)
        df['RSI'] = calculate_rsi(df)
        df['MACD'], df['MACD_Signal'] = calculate_macd(df)
        
        print(df.tail())  # Print the last few rows of the dataframe to see the calculated indicators
