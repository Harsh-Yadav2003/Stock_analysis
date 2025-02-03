import sys
import os
import pandas as pd
from src.config import SYMBOL
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from fastapi import FastAPI, Depends
from src.data.fetcher import fetch_stock_data
from src.analysis.calculator import calculate_daily_returns, get_high_low, calculate_statistics

# -------------------------Swaggar API--------------------#

app = FastAPI()




# -------------------------This function hits url of home page--------------------#


@app.get("/")

def home():
    return {"message": "Stock API is running!"}


# -------------------------This function hits url of Stock price--------------------#



@app.get("/stock/price/{symbol}")

def get_stock_price(symbol: str):
    
    data = fetch_stock_data(symbol)  
    print("Fetched Data:", data) 
    
    if isinstance(data, dict):
        return data
    
    if "close" not in data.columns:
        return {"error": "Close price not available in data"}
    
    return {"latest_price": data["close"].iloc[-1]}



# -------------------------This function hits url of Stock history--------------------#


@app.get("/stock/history/{symbol}")

def get_stock_history(symbol: str, start: str = None, end: str = None):
    data = fetch_stock_data(symbol, start, end)
    if isinstance(data, dict):
        return data
    return data.to_dict(orient="records")


# -------------------------This function hits url of Stock returns--------------------#


@app.get("/stock/analysis/returns/{symbol}")

def get_returns(symbol: str):
    
    data = fetch_stock_data(symbol)    
    print("Fetched Data:\n", data.head() if isinstance(data, pd.DataFrame) else data)
    
    if isinstance(data, dict) or data.empty:
        return {"error": f"No stock data found for {symbol}"}
    
    if "Close" not in data.columns:
        return {"error": "'Close' column missing in stock data"}
    
    returns_df = calculate_daily_returns(data)
    
    if "Date" not in returns_df.columns:
        return {"error": "'Date' column missing in returns data"}

    return returns_df[["Date", "returns"]].to_dict(orient="records")


# -------------------------This function hits url of high_low stocks --------------------#


@app.get("/stock/analysis/high_low/{symbol}/{date}")

def get_high_low_analysis(symbol: str, date: str):
    data = fetch_stock_data(symbol)
    
    if isinstance(data, dict):
        return data
    
    return get_high_low(data, date)


# -------------------------This function hits url of Stock statistics--------------------#


# @app.get("/stock/analysis/stats/{symbol}")

# def get_stats(symbol: str):
#     data = fetch_stock_data(symbol)
#     if isinstance(data, dict):
#         return data
#     return calculate_statistics(data)


@app.get("/stock/analysis/stats/{symbol}")
def get_stats(symbol: str):
    data = fetch_stock_data(symbol)    
    print("Fetched Data:\n", data.head() if isinstance(data, pd.DataFrame) else data)
    if isinstance(data, dict) or data.empty:
        return {"error": f"No stock data found for {symbol}"}
    if "Close" not in data.columns:
        return {"error": "'Close' column missing in stock data"}

    stats = calculate_statistics(data)
    return stats

