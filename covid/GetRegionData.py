import requests
import json

# path where the headers are stored rather than explicitly available within the code
header_file_path = '/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/covid/headers.json'

with open(header_file_path, 'r') as file:
    header_data = json.load(file)
    # print(header_data)

url = "https://covid-19-statistics.p.rapidapi.com/regions"

response = requests.get(url, headers=header_data)

data = response.json()

region_list = []
for res_data in data['data']:
    region_list.append(res_data)

# writing the data into a json file
# with open("region_data.json", "a") as region_data_file:
#     json.dump(region_list, region_data_file, indent=1)

# retrieving the data from the json file
retrieve_region_file_path = "/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/region_data.json"

with open(retrieve_region_file_path, "r") as read_file:
    rt_data = json.load(read_file)
    # print(rt_data)
    for i, record in enumerate(rt_data, start=0):
        print(f"{i} {record}")
