#!/usr/bin/env python3
import random, io, math, time
from yahoo_fin import options, stock_info as si

start_time = time.time()
# option chain, will be used for printing option chain info
option_chain = ""

'''
1. get tickers info
2. get random ticker
2. get random expiration dates
3. get random strike price
3. randomly decide call or put options
4. print ticker, call/put, expiration date
'''

sp500 = si.tickers_sp500()
nasdaq = si.tickers_nasdaq()
dow = si.tickers_dow()
# others = si.tickers_other()

all = sp500 + nasdaq + dow

# remove below line if you uncomment above
# random_ticker = "T"
# setting random strike price to inital value 0
random_strike_price = 0
# exp_dates = []
random_ticker = ""
# random_ticker = random.choice(all)
# exp_dates = options.get_expiration_dates(random_ticker)

# get expiration dates, rerun of randomly chosen stock does not have options
while True:
    random_ticker = random.choice(all)
    exp_dates = options.get_expiration_dates(random_ticker)
    if(len(exp_dates) != 0):
        break

# print("\n" + str(exp_dates))
random_date = random.choice(exp_dates)

# get current price, will be used to make OTM call/put calculation
current_price = si.get_live_price(random_ticker)

# randomly select calls or puts
random_option_type = random.choice(["Call","Put"])
if(random_option_type == "Call"):
    # random OTM call strike price
    random_strike_price = round(random.uniform(current_price, current_price*3)) + (random.randrange(0, 51, 50)/100)
    try:
        option_chain = options.get_calls(random_ticker, date=random_date)
    except:
        pass
else:
    #random OTM put strike price
    random_strike_price = round(random.uniform(0, current_price)) + (random.randrange(0, 51, 50)/100)
    try:
        option_chain = options.get_puts(random_ticker, date=random_date)
    except:
        pass
# make number a multiple of 5 if it's not
# print(str(random.randrange(0,round(si.get_live_price(random_ticker)/3)+1,1) + random.randrange(0, 96, 5)/10))

print("Ticker: {0}\n{1}: ${2} {3}, literally can't go tits up".format(random_ticker, random_date, str(round(random_strike_price,2)), random_option_type))
print("--- %s seconds ---" % (time.time() - start_time))
#print(option_chain)
#for line in option_chain:
    #print(line)
