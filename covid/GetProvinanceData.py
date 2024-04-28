import requests
import json
import time

header_path = "/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/covid/headers.json"

with open(header_path, 'r') as json_file:
    header = json.load(json_file)

url = "https://covid-19-statistics.p.rapidapi.com/provinces"
params = {"iso": "CHN"}
response = requests.get(url, headers=header, params=params)

# print(response.json())

data = response.json()

CHN_Province = []

for res_data in data['data']:
    Province = res_data['province']
    latitude = res_data['lat']
    longitude = res_data['long']
    # print(f"{Province}, {latitude}, {longitude} ")
    province_data = {
        "province": Province,
        "lat": latitude,
        "long": longitude
    }
    CHN_Province.append(province_data)

# CHN_pro_json = json.dumps(CHN_Province)
# print(CHN_pro_json)

# with open("province_CHN.json", 'w') as p_file:
#     json.dump(CHN_Province, p_file, indent=1)

region_list = []


