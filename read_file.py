import pandas as pd
import feather

def read_file(path):
    if '.csv' in path:
        data = pd.read_csv(path)
    elif '.xlsx' in path:
        data = pd.read_excel(path)
    elif '.feather' in path:
        data = feather.read_dataframe(path)
    return data

path = input('Path for the file to read : ')
data = read_file(path)