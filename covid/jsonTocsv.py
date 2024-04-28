import os.path
import time
import pandas as pd
import json
import csv

file_path = "/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/province_data/"
file_dir = os.listdir(file_path)
for file_name in file_dir:
    file = os.path.join(file_path, file_name)
    print(file)  # full file path where the json data is located
    region_name = file_name.split('.')[0]
    with open(file, 'r') as json_file:
        # data = json.load(json_file)
        data = pd.read_json(json_file)
        # printing the raw data in a list
        # print(data)

        csv_data = data.to_csv(index=False)
        # print(csv_data)
        print(len(csv_data))
        # time.sleep(1)
        if len(csv_data) > 100:
            # print(csv_data)
            with open(f"/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/csv_data/region_{region_name}",'w') as files:
                files.write(csv_data)
        else:
            print(f"{region_name} has less records")

