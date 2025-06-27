import streamlit as st
import pandas as pd
from utils.load_data import load_positions, load_transactions

st.set_page_config(page_title="Roth IRA Dashboard", layout="wide")

st.title("📊 Roth IRA Portfolio Dashboard")

# --- Load data ---
positions_df = load_positions()
transactions_df = load_transactions()

# --- Display Positions ---
st.header("🧾 Current Holdings")
if positions_df is not None and not positions_df.empty:
    st.dataframe(positions_df, use_container_width=True)
else:
    st.warning("No position data available.")

# --- Display Transactions ---
st.header("📜 Transaction History")
if transactions_df is not None and not transactions_df.empty:
    st.dataframe(transactions_df, use_container_width=True)
else:
    st.warning("No transaction data available.")

# --- Summary Metrics ---
if positions_df is not None and "Market Value" in positions_df.columns:
    st.header("📈 Portfolio Summary")

    total_value = positions_df["Market Value"].sum()
    top_positions = positions_df.sort_values("Market Value", ascending=False).head(5)

    col1, col2 = st.columns(2)
    col1.metric("Total Market Value", f"${total_value:,.2f}")
    col2.metric("Number of Holdings", len(positions_df))

    st.subheader("Top 5 Holdings by Market Value")
    st.dataframe(top_positions[["Symbol", "Description", "Market Value"]], use_container_width=True)

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Roth IRA Dashboard")

