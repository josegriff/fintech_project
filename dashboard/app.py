import streamlit as st
import pandas as pd
import yfinance as yf

# --- Data Fetching ---
@st.cache_data(ttl=300)
def fetch_stock_data(tickers):
    data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        data.append({
            "Company": info["longName"],
            "Ticker": ticker,
            "Price ($)": info["currentPrice"],
            "Market Cap ($)": info["marketCap"],
            "52W High": info["fiftyTwoWeekHigh"],
            "52W Low": info["fiftyTwoWeekLow"]
        })
    return pd.DataFrame(data)

TICKERS = ["AAPL", "MSFT", "GOOGL", "TSLA"]
df = fetch_stock_data(TICKERS)

# --- Sidebar ---
st.sidebar.title("Dashboard Controls")
selected_ticker = st.sidebar.selectbox(
    "Select a stock",
    TICKERS
)

# --- Main Dashboard ---
st.title("FinTech Dashboard")
st.write("Live market data powered by Yahoo Finance.")

# --- Market Overview ---
st.header("Market Overview")
col1, col2, col3, col4 = st.columns(4)

for i, ticker in enumerate(TICKERS):
    row = df[df["Ticker"] == ticker].iloc[0]
    delta = f"{((row['Price ($)'] - row['52W Low']) / row['52W Low'] * 100):.1f}% from 52W low"
    [col1, col2, col3, col4][i].metric(
        label=row["Company"].split()[0],
        value=f"${row['Price ($)']:.2f}",
        delta=delta
    )

# --- Data Table ---
st.header("Full Market Data")
st.dataframe(df)

# --- Chart ---
st.header("Price Comparison")
st.bar_chart(df.set_index("Ticker")["Price ($)"])

# --- Selected Stock Detail ---
st.header(f"Stock Detail: {selected_ticker}")
selected_row = df[df["Ticker"] == selected_ticker].iloc[0]
st.metric("Current Price", f"${selected_row['Price ($)']:.2f}")
st.metric("52 Week High", f"${selected_row['52W High']:.2f}")
st.metric("52 Week Low", f"${selected_row['52W Low']:.2f}")
st.metric("Market Cap", f"${selected_row['Market Cap ($)']:,.0f}")
