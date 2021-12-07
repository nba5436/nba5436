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
xrp_mp = 0

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC") - datetime.timedelta(minutes=30)
        end_time = start_time + datetime.timedelta(minutes=1)
        
        df = pyupbit.get_ohlcv("KRW-ETH", count=1)
        
        print(now)
        print(start_time)
        print(end_time)

        if now > end_time:
            btc_mp = 0
            eth_mp = 0
            xrp_mp = 0
            
        if start_time <= now < end_time:
            krw = get_balance("KRW")
            print(krw)
            if krw > 5000:
                if xrp_mp == 0:
                    if float(df['open']) > float(df['close']):
                        upbit.buy_market_order("KRW-XRP", 365297)
                        xrp_mp = 1
                        print(xrp_mp)
                    else:
                        upbit.buy_market_order("KRW-XRP", 182648)
                        xrp_mp = 1
                        print(xrp_mp)
                #if btc_mp == 0:
                #    upbit.buy_market_order("KRW-BTC", 50000)
                #    btc_mp = 1
                #    print(btc_mp)
                #if eth_mp == 0:
                #    upbit.buy_market_order("KRW-ETH", 50000)
                #    eth_mp = 1
                #    print(eth_mp)
        
    except Exception as e:
        print(e)
        time.sleep(1)
