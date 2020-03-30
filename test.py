#!/usr/bin/env python3
import random, io, math
from yahoo_fin import options, stock_info as si

current_price = round(si.get_live_price("T"))

for i in range(0,1000):

    #random_strike_price = round(random.uniform(current_price, current_price*3)) + (random.randrange(0, 51, 50)/100)
    random_strike_price = round(random.uniform(0, current_price)) + (random.randrange(0, 51, 50)/100)



    print(random_strike_price)
#print(str(random.randrange(0,round(si.get_live_price("T")*3)+1,1) + random.randrange(0, 96, 5)/10))
