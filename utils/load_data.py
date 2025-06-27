import pandas as pd
from pathlib import Path

def load_positions():
    path = Path("data/cleaned_positions.csv")
    if not path.exists():
        return None
    df = pd.read_csv(path)
    
    # Optional: Clean or convert types again if needed
    df.columns = df.columns.str.strip()
    df["Market Value"] = df["Market Value"].replace('[\$,]', '', regex=True).astype(float)
    
    return df

def load_transactions():
    path = Path("data/cleaned_transactions.csv")
    if not path.exists():
        return None
    df = pd.read_csv(path)
    
    # Optional: Clean or convert types again if needed
    df.columns = df.columns.str.strip()
    df["Amount"] = df["Amount"].replace('[\$,]', '', regex=True).astype(float)
    
    return df
