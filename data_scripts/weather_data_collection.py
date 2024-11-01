import json
import requests
import os
from dotenv import load_dotenv
from coordinates import states, latitudes, longitudes

load_dotenv()

API_KEY=os.getenv('api_key')
aqi_base_url=os.getenv('aqi_base_url')
start_date=os.getenv('Start_date')
end_date=os.getenv('End_date')
json_weather_data_path=os.getenv('json_weather_data_path')
hour=os.getenv('hr')
if __name__=='__main__':
    print('****************Data Download Started*************************')

    if not os.path.exists(json_weather_data_path):
        os.makedirs(json_weather_data_path)
        print(f"Created directory: {json_weather_data_path}")

    for index in range(len(latitudes)):
        file_name=json_weather_data_path+states[index]+'.json'
        if os.path.exists(file_name):
            print(f"Data for {states[index]} already exists. Skipping Download")
            continue
        else:
            print(f"Downloading Data for {states[index]}")
            complete_url = base_url + "lat=" + latitudes[index] + "&lon=" + longitudes[index] + "&type="+ hour + '&start=' + start_date + '&end=' + end_date +'&appid='+api_key
            response = requests.get(complete_url)
            data = response.json()
            with open(file_name, 'w') as f:
                json.dump(data, f)
            print(file_name,' created!!!')

    print('JSON DATA DOWNLOADED!!!!')