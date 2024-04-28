import s3fs
import json
import time
import os
import pandas as pd
import snowflake
snow_connection = snowflake.connector.connect(
    user='snowflake24',
    password='snowFlake@2024',
    account='JCOJZNB.RR31951',
    warehouse='COMPUTE_WH',
    database='province_region',
    schema='province'
)

cursor = snow_connection.cursor()

folder_path = "/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/province_data/"
files = os.listdir(folder_path)

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    print(file_path)
    region_name = file_name.split('.')[0]
    time.sleep(1)
    with open(file_path, 'r') as province_files:
        data = json.load(province_files)
        df = pd.DataFrame(data)

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {region_name}_table(
        name string,
        province string,
        lat decimal,
        long decimal
    )
    """
    cursor.execute(create_table_query)
    snow_connection.commit()

    # insert_data_query = f"""
    # INSERT INTO {region_name}_table (name, province, lat, long)
    # VALUES (?, ?, ?, ?)
    # """
    # cursor.executemany(insert_data_query, df[['name', 'province', 'lat', 'long']].values.tolist())
    # snow_connection.commit()

cursor.close()
snow_connection.close()