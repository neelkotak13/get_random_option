#!/usr/bin/env python3
from yahoo_fin import options, stock_info as si
import random
# commented out bc takes a while to scrape all this data

# get S&P stock tickers
sp500 = si.tickers_sp500()
# get NASDAQ stock tickers
nasdaq = si.tickers_nasdaq()
# get Dow Jones stock tickers
dow = si.tickers_dow()
# get Other stock tickers
others = si.tickers_other()

# Combine all elements into one list
all = sp500 + nasdaq + dow + others
# select random ticker from list
random_ticker = random.choice(all)
# random_ticker = "T"
print(random.choice(["calls","puts"])
