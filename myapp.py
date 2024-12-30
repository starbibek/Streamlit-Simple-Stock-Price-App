import yfinance as yf
import pandas as pd
import streamlit as st
import requests

st.write(
    """
         # Simple Stock Price App
         
         Get the stock closing price and volume from input!
         
         """
)

chooseBy = st.radio(label="Type", options=["Company", "Ticker Symbol"])

search = st.text_input(f"{chooseBy.title()}")
tickerSymbol = ""

# Checking for type choosen and handling
if chooseBy.title() == "Company" and search != "":
    fetch = requests.get(f"https://stock-symbol-lookup-api.onrender.com/{search}")
    tickerSymbol = fetch.json().get("stock_symbol", "")
else:
    tickerSymbol = search


if tickerSymbol != "":
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end="2020-5-31")
    st.write("Closing Price")
    st.line_chart(tickerDf.Close)
    st.write("Volume Price")
    st.line_chart(tickerDf.Volume)
