import pandas as pd

# question: https://stackoverflow.com/questions/77346745/how-to-print-the-counts-for-multiple-columns-separately-from-a-csv-file
# test data
data = {'Source': ['A', 'B', 'A', 'C', 'B'],
        'Destination': ['X', 'Y', 'X', 'Z', 'Y'],
        'Protocol': ['HTTP', 'HTTPS', 'FTP', 'HTTP', 'FTP']}
df = pd.DataFrame(data)

def count_unique_column_values(df, col):
    return df[[col]].value_counts(ascending=False) #count columns values

