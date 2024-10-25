import numpy as np
import pandas as pd
import requests
import json
from dotenv import load_dotenv
from coordinates import states,latitudes,longitudes
import os
import time
load_dotenv()


API_KEY=os.getenv('API_KEY')
base_url=os.getenv('base_url')
start_date=os.getenv('start_date')
end_date=os.getenv('end_date')
data_path=os.getenv('json_aqi_data_path')

if __name__=='__main__':
    print('****************Data Download Started*************************')
    for index in range(len(latitudes)):
        file_name=data_path+states[index]+'.json'
        if os.path.exists(file_name):
            print(f"Data for {states[index]} already exists. Skipping Download")
            continue
        else:
            print(f"Downloading Data for {states[index]}")
            complete_url = base_url + "lat=" + latitudes[index] + "&lon=" + longitudes[index]+"&start="+start_date+'&end='+end_date+'&appid='+API_KEY
            response = requests.get(complete_url)
            data = response.json()
            with open(file_name, 'w') as f:
                json.dump(data, f)
            print(file_name,' created!!!')
            time.sleep(60)

    print('JSON DATA DOWNLOADED!!!!')