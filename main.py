import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('InventoryData.xlsx')
    print(df.head())
