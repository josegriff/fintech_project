import yfinance as yf
import pandas as pd

# Define the stocks we want
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA"]

# Build a list to store results
data = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    data.append({
        "Company": info["longName"],
        "Ticker": ticker,
        "Price ($)": info["currentPrice"],
        "Market Cap": info["marketCap"],
        "52W High": info["fiftyTwoWeekHigh"],
        "52W Low": info["fiftyTwoWeekLow"]
    })

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)
