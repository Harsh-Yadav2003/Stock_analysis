# ---------------------------------testing case yha hai-----------------------------#

import pandas as pd
from src.analysis.calculator import calculate_daily_returns, calculate_statistics
from src.config import SYMBOL

def test_calculate_daily_returns():
    df = pd.DataFrame({"close": [100, 105, 110]})
    df = calculate_daily_returns(df)
    assert round(df["returns"].iloc[1], 2) == 5.00

def test_calculate_statistics():
    df = pd.DataFrame({"close": [100, 200, 300]})
    stats = calculate_statistics(df)
    assert stats["mean"] == 200
    assert stats["median"] == 200
    assert round(stats["std_dev"], 2) == 100