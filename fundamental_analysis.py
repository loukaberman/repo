# fundamental_analysis.py
import requests
import config

def fetch_company_overview(symbol):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'OVERVIEW',
        'symbol': symbol,
        'apikey': config.ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def calculate_pe_ratio(data):
    try:
        pe_ratio = float(data['PERatio'])
    except (KeyError, ValueError):
        pe_ratio = None
    return pe_ratio

def calculate_ev_ebitda(data):
    try:
        ev = float(data['EnterpriseValue'])
        ebitda = float(data['EBITDA'])
        ev_ebitda = ev / ebitda
    except (KeyError, ValueError, ZeroDivisionError):
        ev_ebitda = None
    return ev_ebitda

def calculate_roa(data):
    try:
        net_income = float(data['NetIncomeTTM'])
        total_assets = float(data['TotalAssets'])
        roa = (net_income / total_assets) * 100
    except (KeyError, ValueError, ZeroDivisionError):
        roa = None
    return roa

if __name__ == "__main__":
    symbol = 'AAPL'  # Example symbol
    overview_data = fetch_company_overview(symbol)
    pe_ratio = calculate_pe_ratio(overview_data)
    ev_ebitda = calculate_ev_ebitda(overview_data)
    roa = calculate_roa(overview_data)
    
    print(f"Fundamental Analysis for {symbol}:")
    print(f"P/E Ratio: {pe_ratio}")
    print(f"EV/EBITDA: {ev_ebitda}")
    print(f"ROA: {roa}")
