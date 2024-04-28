import requests
import json
import time

header_path = "/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/covid/headers.json"

with open(header_path, 'r') as json_file:
    header = json.load(json_file)

url = "https://covid-19-statistics.p.rapidapi.com/provinces"

region_list = []
# reading a file
with open("/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/region_data.json", "r") as file_read:
    data = json.load(file_read)
    # print(data)
    for res_data in data:
        ISO = res_data['iso']
        # print(f"{ISO}")
        region_list.append(ISO)

# Iterating over the regions data
region_province = []
for region_data in region_list:
    print(region_data)
    region = {"iso": region_data}
    response_url = requests.get(url, headers=header, params=region)
    res_province_data = response_url.json()
    # time.sleep(3)
    # Initialize the region_province list for each region
    region_province = []
    with open(f"/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/province_data/province_{region_data}.json", 'w') as region_json_file:
        for resp in res_province_data['data']:
            re_p = {
                "city": resp['name'],
                "province": resp['province'],
                "lat": resp['lat'],
                "long": resp['long']
            }

            region_province.append(re_p)
            # print(region_province)
        json.dump(region_province, region_json_file, indent=1)

# print(region_province)
