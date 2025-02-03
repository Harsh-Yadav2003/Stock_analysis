import pandas as pd
import yfinance as yf
from src.config import SYMBOL

def fetch_stock_data(symbol: str, start: str = None, end: str = None):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="max" if not start else None, start=start, end=end)
        if data.empty:
            return {"error": "No data available"}
        return data.reset_index()  # Ensuring date is included
    except Exception as e:
        return {"error": str(e)}
