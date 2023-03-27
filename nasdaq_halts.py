#!/bin/python

import os,requests,pandas,json

url = "https://www.nasdaqtrader.com/RPCHandler.axd"

headers = {
    'content-type': 'application/json',
    'authority': 'www.nasdaqtrader.com',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.nasdaqtrader.com/Trader.aspx?id=TradeHalts',
    'accept-language': 'en-US,en;q=0.9',
    }

data = {'id': 6,
    'method':'BL_TradeHalt.GetTradeHalts',
    "params":"[]",
    "version":"1.1"
    }

r = requests.post(url, data=json.dumps(data), headers=headers)

if r.status_code == 200:
    from bs4 import BeautifulSoup
    src = BeautifulSoup( r.text, "lxml" )
    