import pandas as pd

with open('input.json', encoding='utf-8') as f:
    df = pd.read_json(f)

df.to_csv('input.csv', encoding='utf-8-sig', index=False)