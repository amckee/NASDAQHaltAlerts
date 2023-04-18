#!/bin/python

import feedparser, dbus
from collections import Counter
import datetime

url = "http://www.nasdaqtrader.com/rss.aspx?feed=tradehalts"
feed = feedparser.parse( url )

halts = []

for entry in feed.entries:
    haltdate = datetime.datetime.strptime(entry.ndaq_haltdate, '%m/%d/%Y')
    if haltdate.date() == datetime.datetime.today().date():
        halts.append( entry.ndaq_issuesymbol )

most_halts = Counter(halts).most_common(5)

stroutput = "Symbols that halted the most:\r\n"

for halt in most_halts:
    if halt[1] > 1:
        stroutput += ( "%s : %s" % (halt[0], halt[1]) )
        stroutput += "\r\n"

if len( most_halts ) > 0:
    obj = dbus.SessionBus().get_object("org.freedesktop.Notifications", "/org/freedesktop/Notifications")
    obj = dbus.Interface(obj, "org.freedesktop.Notifications")
    obj.Notify("NASDAQ Halts", 0, "", "NASDAQ Halts", stroutput, [], {"urgency": 1}, 5000)
