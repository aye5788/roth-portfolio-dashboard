import os

def find_latest_file(prefix, folder="data"):
    files = [f for f in os.listdir(folder) if f.startswith(prefix)]
    files.sort(reverse=True)  # assuming filenames have timestamps
    return os.path.join(folder, files[0]) if files else None

def load_positions():
    path = find_latest_file("Roth_Contributory_IRA-Positions")
    if not path: return None
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df['Market Value'] = df['Market Value'].replace('[\$,]', '', regex=True).astype(float)
    return df

def load_transactions():
    path = find_latest_file("Roth_Contributory_IRA_XXX531_Transactions")
    if not path: return None
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df
