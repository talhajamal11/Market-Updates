"""
Python Class that pulls in Market Data from Yahoo Finance

Author: Talha Jamal
Date: 22nd Dec, 2023
"""
import datetime as dt
import pandas as pd
import numpy as np
import yfinance as yf


class MarketDataYFinance:
    """
    This Class is designed to pull Market Data (Pricing and Volume) and calculate return statistics
    Each Attribute below returns the above-mentioned data in a DataFrame
    They perform this task on only one security
    """

    def __init__(self, tic: str, start: str, stop: str) -> None:
        """
        Initialize Class with Ticker and start and stop dates to pull data for
        """
        self.tic = tic
        self.start = dt.datetime.strptime(start, '%Y/%m/%d')
        self.stop = dt.datetime.strptime(stop, '%Y/%m/%d')

    def price_df(self, price_col: str = 'Adj Close') -> pd.DataFrame:
        """This function returns a dataframe for the pricing and volume data for a single 
            ticker. Only Input needed is the Pricing Column from the DataFrame.
            Default is Close Price

        Args:
            price_col (str, optional): Defaults to 'Adj Close'.

        Returns:
            pd.DataFrame: Contains return characteristics
        """
        price_df = yf.download(self.tic, self.start, self.stop)
        price_df["1D_Return"] = price_df[price_col].pct_change()
        price_df["1D_Log_Return"] = np.log(price_df[price_col] / price_df[price_col].shift(1))
        price_df["Cum_Return"] = (1 + (price_df["1D_Return"])).cumprod()
        price_df["Ann_Vol"] = price_df["1D_Log_Return"].rolling(252).std() * np.sqrt(252)

        return price_df
