import pandas as pd
from pathlib import Path

def load_positions(path="data/Roth_Contributory_IRA-Positions-2025-06-27-090102.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df['Market Value'] = df['Market Value'].replace('[\$,]', '', regex=True).astype(float)
    return df

def load_transactions(path="data/Roth_Contributory_IRA_XXX531_Transactions_20250627-130048.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df
