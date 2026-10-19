import pandas as pd

try:
    df = pd.read_csv('foodset.csv')
    print("CSV loaded successfully!")
    print(df.head())
except FileNotFoundError:
    print("CSV not found.")