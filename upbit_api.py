#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install pyupbit


# In[85]:


import time
import pyupbit
import datetime

access = ""
secret = ""

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autoTrade start")
btc_mp = 0
eth_mp = 0

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(hours=15)
        print(now)
        print(start_time)
        print(end_time)
        #print(btc_mp)
        #print(eth_mp)

        if start_time <= now < end_time:
            krw = get_balance("KRW")
            print(krw)
            btc = get_balance("BTC")
            print(btc)
            eth = get_balance("ETH")
            print(eth)
            if krw > 50000:
                if btc_mp == 0:
                    upbit.buy_market_order("KRW-BTC", 50000)
                    btc_mp = 1
                    print(btc_mp)
                elif eth_mp == 0:
                    upbit.buy_market_order("KRW-ETH", 50000)
                    eth_mp = 1
                    print(eth_mp)
        
    except Exception as e:
        print(e)
        time.sleep(1)


# In[ ]:





# In[ ]:




