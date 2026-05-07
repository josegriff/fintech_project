import streamlit as st
import pandas as pd

# --- Sidebar ---
st.sidebar.title("Dashboard Controls")
selected_asset = st.sidebar.selectbox(
    "Select an asset to highlight",
    ["Bitcoin", "Apple", "Tesla", "Gold"]
)

# --- Main Dashboard ---
st.title("FinTech Dashboard")
st.write("Welcome to my financial dashboard.")

st.header("Market Overview")
st.metric(label="Bitcoin Price", value="$65,432", delta="+2.4%")
st.metric(label="S&P 500", value="5,204", delta="-0.8%")

st.header("Portfolio Performance")

data = {
    "Asset": ["Bitcoin", "Apple", "Tesla", "Gold"],
    "Value ($)": [12500, 8300, 4200, 6100],
    "Change (%)": [2.4, 1.1, -3.2, 0.5]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.header("Portfolio Breakdown")
st.bar_chart(df.set_index("Asset")["Value ($)"])

# --- Selected Asset Detail ---
st.header(f"Selected Asset: {selected_asset}")
asset_data = df[df["Asset"] == selected_asset]
st.write(asset_data)
