'''
Dataset selection:
Use: https://github.com/swapniljariwala/nsepy
Source OCLHV data for NSE stocks (INFY,TCS) between 2015-2016. Data level - Daily.
Source OCLHV data for NIFTY IT index. Data level - Daily.

'''

from nsepy import *
from datetime import date

def get_data():
	data_infy = get_history(symbol="INFY", start=date(2015,1,1), end=date(2015,12,31))
	data_tcs = get_history(symbol="TCS", start=date(2015,1,1), end=date(2015,12,31))

	niftyit = get_history(symbol="NIFTY IT", start=date(2015,1,1), end=date(2015,12,31),index=True)
	#print(data)

	data_tcs.to_csv("data_tcs.csv")
	print("NSE stocks TCS collected")
	data_infy.to_csv("data_infy.csv")
	print("NSE stocks INFY collected")
	niftyit.to_csv("niftyit.csv")
	print("Data for NIFTY IT index collected")