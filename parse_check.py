import pandas as pd
import numpy as np

# Load one excel file to see its structure
try:
    df_excel = pd.read_excel('2024 Deaths_Statistical Tables.xlsx', sheet_name=0, nrows=20)
    print("2024 Deaths_Statistical Tables.xlsx columns:")
    print(df_excel.columns.tolist()[:10])
except Exception as e:
    print(e)

