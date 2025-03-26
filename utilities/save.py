import pandas as pd

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df = df.drop_duplicates()
    df.to_csv(filename, index=False, encoding='utf-8-sig')