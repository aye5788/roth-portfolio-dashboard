import streamlit as st
import pandas as pd

from utils.load_data import load_positions, load_transactions

st.set_page_config(page_title="Roth IRA Dashboard", layout="wide")

st.title("📊 Roth IRA Portfolio Dashboard")

# Load data
positions_df = load_positions()
transactions_df = load_transactions()

# Layout: Metrics
st.subheader("Summary Metrics")

if positions_df is not None:
    total_value = positions_df['Market Value'].sum()
    st.metric(label="Total Portfolio Value", value=f"${total_value:,.2f}")

if transactions_df is not None:
    total_contributions = transactions_df.loc[transactions_df['Amount'] > 0, 'Amount'].sum()
    total_withdrawals = transactions_df.loc[transactions_df['Amount'] < 0, 'Amount'].sum()
    st.metric(label="Total Contributions", value=f"${total_contributions:,.2f}")
    st.metric(label="Total Withdrawals", value=f"${abs(total_withdrawals):,.2f}")

st.markdown("---")

# Layout: Data Preview
st.subheader("📄 Current Positions")
if positions_df is not None:
    st.dataframe(positions_df)

st.subheader("📜 Transaction History")
if transactions_df is not None:
    st.dataframe(transactions_df.sort_values("Date", ascending=False))

# Optional charting section
if transactions_df is not None:
    st.markdown("### 🕒 Contributions Over Time")
    monthly_contributions = (
        transactions_df[transactions_df['Amount'] > 0]
        .groupby(transactions_df['Date'].dt.to_period("M"))
        ['Amount'].sum()
        .to_timestamp()
    )
    st.bar_chart(monthly_contributions)

