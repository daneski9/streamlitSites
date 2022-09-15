import yfinance as yf
import streamlit as st
import pandas as pd
#define the ticker symbol
tickerSymbol = 'BA'
st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of `tickerSymbol`!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

tickerSymbol = 'BA'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)