# ------------------pandas or symbol ko import kiya config ki file se--------------#
import pandas as pd
from src.config import SYMBOL

# -----------------All three analysis features mentioned in project pdf-------------------#

def calculate_daily_returns(df: pd.DataFrame):
    df["returns"] = df["close"].pct_change() * 100  # Fixed column name
    return df

def get_high_low(df: pd.DataFrame, date: str):
    day_data = df.loc[df["Date"] == date]  # Ensure correct filtering
    if not day_data.empty:
        return {"high": day_data["High"].values[0], "low": day_data["Low"].values[0]}
    return {"error": "No data available for this date"}

def calculate_statistics(df: pd.DataFrame):
    stats = {
        "mean": df["close"].mean(),
        "median": df["close"].median(),
        "std_dev": df["close"].std()
    }
    return stats
