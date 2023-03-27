#!/bin/python

import feedparser, subprocess
from collections import Counter

url = "http://www.nasdaqtrader.com/rss.aspx?feed=tradehalts"

feed = feedparser.parse( url )

halts = []

for entry in feed.entries:
    halts.append( entry.ndaq_issuesymbol )

most_halts = Counter(halts).most_common(3)

stroutput = "Symbols that halted the most:\r\n"

for halt in most_halts:
    stroutput += ( "%s : %s" % (halt[0], halt[1]) )
    stroutput += "\r\n"

subprocess.run( ["notify-send", "-i", "./usd.svg", "-a", "NASDAQ Halts", stroutput])
