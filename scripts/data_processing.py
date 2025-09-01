import pandas as pd
import glob
import os

def csv_import(filename):
    df = pd.read_csv(filename, sep=';', header=9, decimal=',')
    df = df.drop(columns='Unnamed: 22')
    return df

def outlier_processing(value, upper_bounds, lower_bounds, mean):
    if value > upper_bounds:
        return mean
    elif value < lower_bounds:
        return mean
    else:
        return value

def fill_values(df):
    numeric_cols = df.select_dtypes(include='number').columns
    ffill = df[numeric_cols].ffill()
    bfill = df[numeric_cols].bfill()
    mean_fill = (bfill + ffill) / 2

    Q3 = df[numeric_cols].quantile(0.75)
    Q1 = df[numeric_cols].quantile(0.25)

    IQR = Q3 - Q1
    lower_bound = Q1 - (IQR * 1.5)
    upper_bound = Q3 + (IQR * 1.5)
    mean = df[numeric_cols].median()


    for col in numeric_cols:
        df[col] = df[col].fillna(mean_fill[col])
        df[col] = df[col].apply(lambda x: outlier_processing(x, upper_bound[col], lower_bound[col], mean[col]))

    df['Data Medicao'] = pd.to_datetime(df['Data Medicao'])
    df['month']= df['Data Medicao'].dt.month
    df['year']= df['Data Medicao'].dt.year

    group = df.groupby(['month', 'year'])

    for column in df.columns:
        df[column] = df[column].fillna(group[column].transform('mean'))

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    return df

def concat_files():
    path = 'data/raw/meteorological_stations'
    files = glob.glob(os.path.join(path, '*.csv'))

    dfs = []
    for file in files:
        df = csv_import(file)
        df = fill_values(df)
        dfs.append(df)
    df_final = pd.concat(dfs, ignore_index=True)
    return df_final

def process_data():
    df = concat_files()
    df.to_csv('data/clean/processed_met_data.csv', index=False)
    return df