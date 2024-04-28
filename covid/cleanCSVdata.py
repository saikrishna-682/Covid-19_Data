import csv
import pandas as pd
import os

folder_path = "/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/csv_data/"

folder_files = os.listdir(folder_path)

# Disable displaying the index
pd.set_option('display.expand_frame_repr', False)

for file_names in folder_files:
    file_name = os.path.join(folder_path, file_names)
    data = pd.read_csv(file_name)
    # Drop rows with any missing values
    data = data.dropna(how='any')
    print(data.to_string(index=False))
    break




'''
NOTES::
The line data = data.dropna(how='any') drops all rows that have at least one missing value (NaN) in any column.
If you want to drop rows only if all columns have missing values, you can use how='all' instead
'''