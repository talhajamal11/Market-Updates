"""
Script to generate images for top 10 daily, weekly, monthly and yearly performance

Written by: Talha Jamal @ 24/12/2023
"""
import time
_start = time.time()
import datetime as dt
import os
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#Create directory to store today's plots
_today = dt.datetime.today().strftime('%Y-%m-%d')
directory = f'/Users/talhajamal/Desktop/Code/Daily_Market_Update/data/{_today}'

# Create the directory if it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Get SP500 Tickers
sp500 = pd.read_csv('/Users/talhajamal/Desktop/Code/Daily_Market_Update/data/sp500.csv')
SP500_TICKERS = ','.join(sp500['Symbol']).replace(',',' ')

# 2 Year Data
data = yf.download(SP500_TICKERS, period='2y')

# Performance Metrics
performance_metrics = {
    '1d': data['Adj Close'].pct_change(fill_method=None).tail(1) * 100,
    '1w': data['Adj Close'].pct_change(fill_method=None, periods=5).tail(1) * 100,
    '1m': data['Adj Close'].pct_change(fill_method=None, periods=21).tail(1) * 100,
    '1y': data['Adj Close'].pct_change(fill_method=None, periods=252).tail(1) * 100
}

# Find top 10 performing stocks for each period
top_performers = {period: metric.iloc[0].nlargest(10) \
    for period, metric in performance_metrics.items()}

one_day_performance = top_performers['1d']
one_week_performance = top_performers['1w']
one_month_performance = top_performers['1m']
one_year_performance = top_performers['1y']

# Plot of best performing stocks over 1 Day
for ticker, ret in one_day_performance.items():
    #print(ticker, ret)
    plt.plot(data['Adj Close'][ticker].pct_change().tail(2) * 100, label=ticker)
plt.title('Daily Returns on '+_today)
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Daily Return')
plt.legend(loc='upper left', ncol=2)
plt.tight_layout()
_FILENAME = '1D_performance.png'
_full_path = os.path.join(directory, _FILENAME)
plt.savefig(_full_path)
#plt.show()
plt.clf()

# Plot of best performing stocks over 1 Week
for ticker, ret in one_week_performance.items():
    #print(ticker, ret)
    plt.plot(data['Adj Close'][ticker].pct_change(periods=5).tail(5) * 100, label=ticker)
plt.title('Weekly Returns on ' + _today)
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Weekly Return')
plt.legend(loc='upper right', ncol=2)
plt.tight_layout()
_FILENAME = '1W_performance.png'
_full_path = os.path.join(directory, _FILENAME)
plt.savefig(_full_path)
#plt.show()
plt.clf()

# Plot of best performing stocks over 1 Month
for ticker, ret in one_month_performance.items():
    #print(ticker, ret)
    plt.plot(data['Adj Close'][ticker].pct_change(periods=22).tail(22) * 100, label=ticker)
plt.title('Monthly Returns on '+_today)
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Monthly Return')
plt.legend(loc='lower right', ncol=2)
plt.tight_layout()
_FILENAME = '1M_performance.png'
_full_path = os.path.join(directory, _FILENAME)
plt.savefig(_full_path)
#plt.show()
plt.clf()

# Plot of best performing stocks over 1 Year
for ticker, ret in one_year_performance.items():
    #print(ticker, ret)
    plt.plot(data['Adj Close'][ticker].pct_change(periods=252).tail(252) * 100, label=ticker)
plt.title('Yearly Returns on '+_today)
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Yearly Return')
plt.legend(loc='upper left', ncol=2)
plt.tight_layout()
_FILENAME = '1Y_performance.png'
_full_path = os.path.join(directory, _FILENAME)
plt.savefig(_full_path)
#plt.show()
plt.clf()

_stop = time.time()
print(_stop - _start)
