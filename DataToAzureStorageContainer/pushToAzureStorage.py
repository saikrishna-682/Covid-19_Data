import pandas as pd
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from config import ACCOUNT_NAME, ACCOUNT_KEY, CONTAINER_NAME, DESTINATION_FOLDER


# Connect to Azure Storage
blob_service_client = BlobServiceClient.from_connection_string(f"DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY};EndpointSuffix=core.windows.net")
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

folder_path = "/Users/saikrishnasomavarapu/Documents/pycharm-projects/Covid-19/csv_data/"

folder_files = os.listdir(folder_path)

# Disable displaying the index
pd.set_option('display.expand_frame_repr', False)

for file_names in folder_files:
    file_name = os.path.join(folder_path, file_names)
    file_path_name = file_name.split('.')[0]
    data = pd.read_csv(file_name)
    # Drop rows with any missing values
    data = data.dropna(how='any')
    print(data.to_string(index=False))
    # Upload the file to Azure Storage
    blob_client = container_client.get_blob_client(f"{DESTINATION_FOLDER}/{file_names}")
    with open(file_name, "rb") as data:
        blob_client.upload_blob(data)
    break
